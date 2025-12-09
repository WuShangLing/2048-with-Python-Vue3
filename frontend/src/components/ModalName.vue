<template>
  <div class="modal-backdrop">
    <div class="modal">
      <h2>提交成绩</h2>
      <p>名字只能包含字母和数字（可留空）</p>

      <input
        class="name-input"
        v-model="localName"
        placeholder="输入名字"
      />

      <div class="modal-actions">
        <button @click="confirm">确认提交</button>
        <button @click="$emit('cancel')">取消</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue"

const props = defineProps({
  modelValue: {
    type: String,
    default: ""
  }
})

const emit = defineEmits(["update:modelValue", "confirm", "cancel"])

const localName = ref(props.modelValue)

watch(
  () => props.modelValue,
  (v) => {
    localName.value = v
  }
)

const confirm = () => {
  emit("update:modelValue", localName.value)
  emit("confirm")
}
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

.name-input {
  width: 90%;
  padding: 6px;
  margin-top: 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
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
  background: #cdeeff;
}
</style>
