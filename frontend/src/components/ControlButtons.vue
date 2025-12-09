<template>
  <div class="btn-group">
    <button class="btn restart" @click="$emit('restart')">
      重新开始
    </button>
    <button class="btn end" @click="$emit('end')">
      提前结束
    </button>
  </div>
</template>

<script setup>
defineEmits(["restart", "end"])
</script>

<style scoped>
.btn-group {
  display: flex;
  justify-content: center;
  gap: 14px;
  margin-top: 20px;
}

.btn {
  padding: 10px 20px;
  border-radius: 20px;
  border: none;
  cursor: pointer;
  color: #444;
  font-size: 14px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.12);
  transition: transform 0.12s;
}

.restart {
  background: #ffd1dc;
}

.end {
  background: #ffd6a5;
}

.btn:hover {
  transform: translateY(-2px);
}
</style>
