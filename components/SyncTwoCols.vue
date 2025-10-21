<template>
  <div class="two-cols-sync grid grid-cols-2 gap-4">
    <!-- 左侧代码块 -->
    <div class="col-left" @click="handleClick">
      <slot name="left" :currentStep="currentStep" />
    </div>
    
    <!-- 右侧解释块 -->
    <div class="col-right" @click="handleClick">
      <slot name="right" :currentStep="currentStep" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  steps: {
    type: Number,
    default: 1
  }
})

const { $clicks, $clicksContext } = useSlideContext()

// 当前步骤，从 0 开始
const currentStep = computed(() => $clicks.value)

// 总步骤数
const totalSteps = computed(() => props.steps)

// 点击处理
function handleClick() {
  if (currentStep.value < totalSteps.value) {
    $clicksContext.next()
  }
}
</script>

<style scoped>
.two-cols-sync {
  height: 100%;
  cursor: pointer;
}

.col-left, .col-right {
  height: 100%;
}
</style>
