<template>
  <div class="modal-backdrop">
    <div class="modal">
      <h2>恭喜达成 2048！</h2>
      <p>当前分数：{{ score }}</p>

      <div class="modal-actions">
        <button @click="$emit('submit')">提交成绩</button>
        <button @click="$emit('continue')">继续挑战</button>
        <button @click="$emit('restart')">重新开始</button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  score: { type: Number, required: true }
})

defineEmits(["submit", "continue", "restart"])
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.35);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #fffdf7;
  padding: 20px;
  width: 260px;
  border-radius: 14px;
  text-align: center;
}

.modal-actions {
  margin-top: 15px;
  display: flex;
  justify-content: center;
  gap: 12px;
}

button {
  padding: 6px 12px;
  border-radius: 18px;
  border: none;
  cursor: pointer;
  background: #ffd6a5;
}
</style>
