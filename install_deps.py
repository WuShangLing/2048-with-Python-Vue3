import subprocess
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")


def run(cmd, cwd=None):
    print(f"\n[CMD] {cmd}")
    proc = subprocess.run(cmd, cwd=cwd, shell=True)
    if proc.returncode != 0:
        print(f"[ERROR] 命令失败：{cmd}")
        sys.exit(1)


def install_python_deps():
    print("\n========== 安装 Python 后端依赖 ==========")

    req_path = os.path.join(BACKEND_DIR, "requirements.txt")

    if not os.path.exists(req_path):
        print("[WARN] 未找到 requirements.txt，已创建默认依赖文件。")
        with open(req_path, "w", encoding="utf8") as f:
            f.write("fastapi\nuvicorn\npydantic\nanyio\nstarlette\n")

    run(f"pip install -r requirements.txt", cwd=BACKEND_DIR)

    print("[OK] 后端依赖安装完成。")


def install_node_deps():
    print("\n========== 安装前端 npm 依赖 ==========")

    node_modules = os.path.join(FRONTEND_DIR, "node_modules")

    if os.path.exists(node_modules):
        print("[SKIP] node_modules 已存在，跳过 npm install。")
    else:
        run("npm install", cwd=FRONTEND_DIR)
        print("[OK] 前端依赖安装完成。")


def main():
    print("==========================================")
    print("       2048 一键安装依赖器")
    print("==========================================\n")

    install_python_deps()
    install_node_deps()

    print("\n==========================================")
    print("     ✔✔ 所有依赖安装完成，可以运行游戏！")
    print("==========================================")
    print("下一步：双击 run_prod.py 启动项目。")


if __name__ == "__main__":
    main()
