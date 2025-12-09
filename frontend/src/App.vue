<template>
  <div class="container">
    <h1>2048 - FastAPI + Vite + Vue3</h1>

    <!-- 上方：说明书 + 排行榜 -->
    <div class="info-row">
      <HelpCard />
      <RankCard :list="leaderboardTop3" />
    </div>

    <!-- 操作按钮 -->
    <ControlButtons
      @restart="restart"
      @end="endGame"
    />

    <!-- 分数 -->
    <ScoreBar
      :score="score"
      :bestScore="bestScore"
    />

    <!-- 棋盘 -->
    <GameBoard
      :board="board"
      :anim="anim"
      @move="move"
    />

    <!-- 游戏结束弹窗 -->
    <ModalGameOver
      v-if="showGameOver"
      :score="score"
      @submit="openSubmit"
      @restart="restart"
    />

    <!-- 胜利弹窗 -->
    <ModalWin
      v-if="showWin"
      :score="score"
      @submit="openSubmit"
      @continue="continueAfterWin"
      @restart="restart"
    />

    <!-- 名字输入 -->
    <ModalName
      v-if="showName"
      v-model="playerName"
      @confirm="submitScore"
      @cancel="closeSubmit"
    />

    <footer class="footer">Made by Caramel</footer>
  </div>
</template>


<script setup>
import HelpCard from "./components/HelpCard.vue"
import RankCard from "./components/RankCard.vue"
import ScoreBar from "./components/ScoreBar.vue"
import ControlButtons from "./components/ControlButtons.vue"
import GameBoard from "./components/GameBoard.vue"
import ModalGameOver from "./components/ModalGameOver.vue"
import ModalWin from "./components/ModalWin.vue"
import ModalName from "./components/ModalName.vue"
import { onMounted } from "vue"
import { useGameLogic } from "./composables/useGameLogic"

const {
  board,
  anim,
  score,
  bestScore,
  leaderboard,
  leaderboardTop3,

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
} = useGameLogic()

onMounted(() => {
  restart()
})
</script>


<style>
body {
  margin: 0;
  background: #faf8f4;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial;
}

.container {
  max-width: 950px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.info-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 18px;
  margin-bottom: 20px;
}

.footer {
  margin-top: 30px;
  color: #888;
}
</style>
