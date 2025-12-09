<template>
  <div class="card help">
    <h2>玩法说明</h2>
    <ul>
      <li>使用键盘方向键 ↑ ↓ ← → 移动方块。</li>
      <li>手机端可在棋盘上滑动操作方向。</li>
      <li>相同数字相遇将会合并。</li>
      <li>合成 <strong>2048</strong> 即算胜利。</li>
      <li>点击“提前结束”可主动结束游戏并提交成绩。</li>
    </ul>
  </div>
</template>

<script setup>
</script>

<style scoped>
.card {
  width: 340px;
  padding: 18px;
  background: #fff4f8;
  border-radius: 12px;
  text-align: left;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card h2 {
  margin: 0 0 10px;
  text-align: center;
}

ul {
  padding-left: 20px;
  line-height: 1.6em;
  list-style: disc;
}
</style>
