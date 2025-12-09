import { ref, computed } from "vue"
import { initBoard, moveBoard, fetchLeaderboard, fetchBestScore, submitScoreApi } from "../api"

export function useGameLogic() {

  // ---------------------------
  // 状态
  // ---------------------------
  const board = ref([])
  const anim = ref([])
  const score = ref(0)
  const bestScore = ref(0)
  const leaderboard = ref([])

  const showGameOver = ref(false)
  const showWin = ref(false)
  const showName = ref(false)

  const playerName = ref("")

  // ---------------------------
  // 动画矩阵生成
  // ---------------------------
  const makeAnim = () =>
    Array.from({ length: 4 }, () =>
      Array.from({ length: 4 }, () => ({ isNew: false, isMerged: false }))
    )

  const applyAnim = (oldB, newB) => {
    const a = makeAnim()
    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 4; j++) {
        const o = oldB?.[i]?.[j] ?? 0
        const n = newB[i][j]
        if (o === 0 && n > 0) a[i][j].isNew = true
        if (n > o && o > 0) a[i][j].isMerged = true
      }
    }
    anim.value = a
    setTimeout(() => (anim.value = makeAnim()), 260)
  }

  // ---------------------------
  // 数据加载
  // ---------------------------
  const loadLeaderboard = async () => {
    const res = await fetchLeaderboard()
    leaderboard.value = res.data.leaderboard.map(([p, s]) => ({ player: p, score: s }))
  }

  const loadBestScore = async () => {
    const res = await fetchBestScore()
    bestScore.value = res.data.best_score || 0
  }

  // ---------------------------
  // 初始化游戏
  // ---------------------------
  const restart = async () => {
    const res = await initBoard()
    board.value = res.data.board
    score.value = res.data.score
    anim.value = makeAnim()

    showGameOver.value = false
    showWin.value = false
    showName.value = false

    await loadLeaderboard()
    await loadBestScore()
  }

  // ---------------------------
  // 移动
  // ---------------------------
  const move = async (dir) => {
    const oldB = board.value
    const res = await moveBoard(dir)

    board.value = res.data.board
    score.value = res.data.score

    applyAnim(oldB, board.value)

    if (res.data.win) showWin.value = true
    if (res.data.game_over) showGameOver.value = true
  }

  // ---------------------------
  // 提前结束
  // ---------------------------
  const endGame = () => {
    showGameOver.value = true
  }

  // ---------------------------
  // 成绩提交
  // ---------------------------
  const submitScore = async () => {
    let name = playerName.value.trim()
    if (!name) name = "Caramel"

    if (!/^[A-Za-z0-9]+$/.test(name)) {
      alert("名字只能包含字母数字")
      return
    }

    await submitScoreApi(name, score.value)

    await loadLeaderboard()
    await loadBestScore()

    showName.value = false
    alert("提交成功！")
  }

  const openSubmit = () => showName.value = true
  const closeSubmit = () => showName.value = false
  const continueAfterWin = () => showWin.value = false

  return {
    board,
    anim,
    score,
    bestScore,
    leaderboard,
    leaderboardTop3: computed(() => leaderboard.value.slice(0, 3)),

    showGameOver,
    showWin,
    showName,
    playerName,

    restart,
    move,
    endGame,

    openSubmit,
    closeSubmit,
    submitScore,
    continueAfterWin,
  }
}
