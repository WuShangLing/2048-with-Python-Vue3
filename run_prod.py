import subprocess
import threading
import time
import socket
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

FRONTEND_URL = "http://127.0.0.1:5173"


# 检查端口是否开放
def is_port_open(host, port):
    try:
        s = socket.create_connection((host, port), timeout=0.5)
        s.close()
        return True
    except:
        return False


# 使用 Windows start 命令打开浏览器（100% 成功）
def open_browser_cmd():
    os.system(f'start "" "{FRONTEND_URL}"')


def start_backend():
    print("[INFO] Starting FastAPI backend...")
    subprocess.Popen([
        sys.executable, "-m", "uvicorn",
        "app.main:app",
        "--host", "0.0.0.0",
        "--port", "8000",
    ], cwd=BACKEND_DIR)


def start_frontend():
    print("[INFO] Starting frontend (npm run dev)...")
    subprocess.Popen("npm run dev", cwd=FRONTEND_DIR, shell=True)


def check_environment():
    # 检查 node
    try:
        subprocess.check_output(["node", "--version"])
    except:
        print("[ERROR] Node.js not installed.")
        sys.exit()

    # 检查 python
    try:
        subprocess.check_output(["python", "--version"])
    except:
        print("[ERROR] Python not installed.")
        sys.exit()

    print("[OK] Environment OK\n")


def main():
    print("========== 2048 Production Launcher ==========\n")

    check_environment()

    # 后端与前端并行启动
    threading.Thread(target=start_frontend, daemon=True).start()
    threading.Thread(target=start_backend, daemon=True).start()

    time.sleep(1)
    open_browser_cmd()

    print("[INFO] Starting services... Please wait.")
    print("[INFO] Close this window to stop all services.\n")

if __name__ == "__main__":
    main()
