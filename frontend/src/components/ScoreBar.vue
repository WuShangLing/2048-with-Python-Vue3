<template>
  <div class="score-bar">
    <div class="score-box">
      <div class="label">当前分数</div>
      <div class="value">{{ score }}</div>
    </div>

    <div class="score-box best">
      <div class="label">最高分</div>
      <div class="value">{{ bestScore }}</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  score: { type: Number, required: true },
  bestScore: { type: Number, required: true }
})
</script>

<style scoped>
.score-bar {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin: 10px 0 20px;
}

.score-box {
  background: #fffdf7;
  padding: 10px 16px;
  border-radius: 12px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  min-width: 120px;
}

.score-box.best {
  background: #ffe4f0;
}

.label {
  font-size: 12px;
  color: #777;
}

.value {
  font-size: 24px;
  font-weight: bold;
}
</style>
