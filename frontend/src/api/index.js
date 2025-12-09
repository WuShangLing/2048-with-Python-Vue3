import axios from "axios"

const api = axios.create({
  baseURL: "/api",
})

// 初始化棋盘
export const initBoard = () => api.get("/init")

// 移动
export const moveBoard = (dir) => api.post(`/move/${dir}`)

// 获取排行榜
export const fetchLeaderboard = () => api.get("/leaderboard")

// 获取全局最高分
export const fetchBestScore = () => api.get("/best_score")

// 提交成绩（名字和分数）
export const submitScoreApi = (player, score) =>
  api.post("/submit_score", null, {
    params: { player, score },
  })
