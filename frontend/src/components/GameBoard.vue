<template>
  <div class="board" ref="boardEl">
    <div class="row" v-for="(row, i) in board" :key="i">
      <div
        class="cell"
        v-for="(cell, j) in row"
        :key="j"
        :class="[
          valueClass(cell),
          anim[i][j].isNew && 'tile-new',
          anim[i][j].isMerged && 'tile-merged'
        ]"
      >
        {{ cell === 0 ? '' : cell }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue"

defineProps({
  board: {
    type: Array,
    required: true
  },
  anim: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(["move"])

const boardEl = ref(null)

// 阻止方向键滚动 + 发送移动事件
const onKey = (e) => {
  if (["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"].includes(e.key)) {
    e.preventDefault()
  }

  if (e.key === "ArrowUp") emit("move", "up")
  if (e.key === "ArrowDown") emit("move", "down")
  if (e.key === "ArrowLeft") emit("move", "left")
  if (e.key === "ArrowRight") emit("move", "right")
}

// 触摸滑动
let sx = 0, sy = 0
const TH = 30

const ts = (e) => {
  sx = e.touches[0].clientX
  sy = e.touches[0].clientY
}

const te = (e) => {
  const dx = e.changedTouches[0].clientX - sx
  const dy = e.changedTouches[0].clientY - sy

  if (Math.abs(dx) < TH && Math.abs(dy) < TH) return

  if (Math.abs(dx) > Math.abs(dy)) {
    emit("move", dx > 0 ? "right" : "left")
  } else {
    emit("move", dy > 0 ? "down" : "up")
  }
}

// 数字对应 class
const valueClass = (v) => {
  if (!v) return "v-0"
  if (v > 2048) return "v-4096"
  return `v-${v}`
}

onMounted(() => {
  window.addEventListener("keydown", onKey, { passive: false })
  if (boardEl.value) {
    boardEl.value.addEventListener("touchstart", ts, { passive: true })
    boardEl.value.addEventListener("touchend", te, { passive: true })
  }
})

onUnmounted(() => {
  window.removeEventListener("keydown", onKey)
})
</script>

<style scoped>
.board {
  width: 400px;
  margin: 20px auto;
  padding: 12px;
  background: #f3eee6;
  border-radius: 14px;
  box-shadow: 0 3px 8px rgba(0,0,0,0.15);
}

.row {
  display: flex;
  justify-content: center;
}

.cell {
  width: 80px;
  height: 80px;
  margin: 6px;
  border-radius: 10px;
  background: #eee4da;
  font-size: 26px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  transition: background-color 0.25s, transform 0.25s;
}

/* 马卡龙颜色 */
.v-0 { background: #f7f5f2; }
.v-2 { background: #ffe4e1; }
.v-4 { background: #fff4c1; }
.v-8 { background: #c8f7c5; }
.v-16 { background: #cfe8ff; }
.v-32 { background: #f8d1ff; }
.v-64 { background: #ffd6a5; }
.v-128 { background: #e2f0cb; }
.v-256 { background: #ffcad4; }
.v-512 { background: #e2cfea; }
.v-1024 { background: #bde0fe; }
.v-2048 { background: #ffc8dd; }
.v-4096 { background: #ffafcc; }

/* 动画 */
@keyframes pop {
  0% { transform: scale(0.3); opacity: 0.3; }
  60% { transform: scale(1.15); opacity: 1; }
  100% { transform: scale(1); }
}
.tile-new {
  animation: pop 0.25s ease-out;
}

@keyframes merge {
  0% { transform: scale(1); }
  50% { transform: scale(1.18); box-shadow: 0 0 18px rgba(255,255,255,0.8); }
  100% { transform: scale(1); box-shadow: none; }
}
.tile-merged {
  animation: merge 0.25s ease-out;
}
</style>
