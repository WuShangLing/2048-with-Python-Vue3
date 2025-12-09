from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import copy
import sqlite3
import time
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- 2048 逻辑 -------------------
def new_board():
    board = [[0] * 4 for _ in range(4)]
    add_tile(board)
    add_tile(board)
    return board

def add_tile(board):
    empty = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty:
        x, y = random.choice(empty)
        board[x][y] = 4 if random.random() < 0.1 else 2

def merge(row):
    row = [x for x in row if x != 0]
    score_gain = 0

    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            score_gain += row[i]
            row[i + 1] = 0

    row = [x for x in row if x != 0]
    return row + [0] * (4 - len(row)), score_gain

def move(board, direction):
    old = copy.deepcopy(board)
    score_gain_total = 0

    if direction == "left":
        new = []
        for r in board:
            m, gain = merge(r)
            new.append(m)
            score_gain_total += gain
        board = new

    elif direction == "right":
        new = []
        for r in board:
            m, gain = merge(r[::-1])
            m = m[::-1]
            new.append(m)
            score_gain_total += gain
        board = new

    elif direction == "up":
        t = list(map(list, zip(*board)))
        new = []
        for r in t:
            m, gain = merge(r)
            new.append(m)
            score_gain_total += gain
        board = list(map(list, zip(*new)))

    elif direction == "down":
        t = list(map(list, zip(*board)))
        new = []
        for r in t:
            m, gain = merge(r[::-1])
            m = m[::-1]
            new.append(m)
            score_gain_total += gain
        board = list(map(list, zip(*new)))

    if board != old:
        add_tile(board)

    return board, score_gain_total

def check_game_over(board):
    # 有空格：未结束
    if any(0 in row for row in board):
        return False

    # 有可合并的相邻块：未结束
    for i in range(4):
        for j in range(4):
            if i + 1 < 4 and board[i][j] == board[i + 1][j]:
                return False
            if j + 1 < 4 and board[i][j] == board[i][j + 1]:
                return False

    return True

def check_win(board):
    return any(2048 in row for row in board)

# ------------------ SQLite 排行榜 ---------------------

DB = "leaderboard.db"

def get_conn():
    return sqlite3.connect(DB)

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    # 每个玩家只保留一条记录（最高分）
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player TEXT UNIQUE,
            score INTEGER,
            created INTEGER
        )
        """
    )
    conn.commit()
    conn.close()

init_db()

def get_global_best_score():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT MAX(score) FROM scores")
    row = cur.fetchone()
    conn.close()
    return row[0] if row and row[0] is not None else 0

@app.post("/submit_score")
def submit_score(player: str = "Caramel", score: int = 0):
    # 名字只允许大小写字母和数字，空或非法则用 Caramel
    if not player:
        player = "Caramel"
    if not re.fullmatch(r"[A-Za-z0-9]+", player):
        player = "Caramel"

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT score FROM scores WHERE player = ?", (player,))
    row = cur.fetchone()

    now_ts = int(time.time())

    if row is None:
        # 新玩家，插入
        cur.execute(
            "INSERT INTO scores (player, score, created) VALUES (?, ?, ?)",
            (player, score, now_ts),
        )
    else:
        old_score = row[0]
        if score > old_score:
            # 更新为更高成绩
            cur.execute(
                "UPDATE scores SET score = ?, created = ? WHERE player = ?",
                (score, now_ts, player),
            )
        # 如果新分数没更高，就不动

    conn.commit()
    conn.close()

    return {"msg": "ok", "player": player}

@app.get("/leaderboard")
def leaderboard():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT player, score FROM scores ORDER BY score DESC, created ASC LIMIT 10"
    )
    data = cur.fetchall()
    conn.close()
    # 返回列表：[["name",123],...]
    return {"leaderboard": data}

@app.get("/best_score")
def best_score():
    return {"best_score": get_global_best_score()}

# ------------------ 游戏状态 API ----------------------

current_board = new_board()
current_score = 0

@app.get("/init")
def api_init():
    global current_board, current_score
    current_board = new_board()
    current_score = 0
    return {
        "board": current_board,
        "score": current_score,
    }

@app.post("/move/{direction}")
def api_move(direction: str):
    global current_board, current_score
    new_board, gain = move(current_board, direction)
    current_score += gain
    current_board = new_board

    return {
        "board": current_board,
        "score": current_score,
        "game_over": check_game_over(current_board),
        "win": check_win(current_board),
    }

@app.get("/")
def home():
    return {"msg": "FastAPI Running!"}
