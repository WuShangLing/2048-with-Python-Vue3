<template>
  <div class="card leaderboard">
    <h2>排行榜（Top 3）</h2>

    <table class="rank-table">
      <thead>
        <tr>
          <th>#</th>
          <th>玩家</th>
          <th>分数</th>
        </tr>
      </thead>

      <tbody>
        <tr v-if="list.length === 0">
          <td colspan="3">暂无记录</td>
        </tr>

        <tr v-for="(item, idx) in top3" :key="idx">
          <td>{{ idx + 1 }}</td>
          <td>{{ item.player }}</td>
          <td>{{ item.score }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { computed } from "vue"

const props = defineProps({
  list: {
    type: Array,
    default: () => []
  }
})

const top3 = computed(() => props.list.slice(0, 3))
</script>

<style scoped>
.card {
  width: 340px;
  padding: 18px;
  background: #e8faff;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.rank-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.rank-table th,
.rank-table td {
  border: 1px solid #ddd;
  padding: 6px;
}

.rank-table th {
  background: #cdeeff;
  font-weight: bold;
}
</style>
