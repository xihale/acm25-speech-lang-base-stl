<!--
  V 组件 - 基于 Slidev 原生 v-click 机制的点击显示组件
  
  用法：
    在 two-cols 布局中：
    ::left::
    <v>第一次点击显示（之前的隐藏）</v>
    <v>第二次点击显示（之前的隐藏）</v>
    
    ::right::
    <v>第一次点击显示（之前的隐藏）</v>
    <v>第二次点击显示（之前的隐藏）</v>
  
  特性：
    - 每次只显示当前步骤的内容
    - 之前的内容会被隐藏
    - 支持在 SClickPanel 内部使用（左右独立计数）
    - 不在 SClickPanel 内也能自动递增
    - 支持 at 属性指定显示步骤
-->
<template>
  <div
    v-click="clickDirective"
    v-show="isVisible"
    class="v-container"
  >
    <slot />
  </div>
</template>

<script setup>
import { inject, computed, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'

const STACK_CLICK_SYMBOL = Symbol.for('acm25.s-click-panel')

const props = defineProps({
  at: {
    type: [Number, String],
    default: undefined,
  },
})

const panel = inject(STACK_CLICK_SYMBOL, null)
const { $clicks, $slidev } = useSlideContext()

// 全局计数器，用于在没有 SClickPanel 时自动分配步骤
if (!globalThis.__vComponentCounter) {
  globalThis.__vComponentCounter = {}
}

// 用于存储分配的步骤号
const assignedStepRef = ref(null)

// 分配步骤号
const clickDirective = computed(() => {
  if (panel?.registerStep) {
    // 在 SClickPanel 内部，使用其自动分配机制
    const step = panel.registerStep(props.at)
    assignedStepRef.value = step
    return step
  }
  
  // 不在 SClickPanel 内部
  if (props.at !== undefined) {
    const num = Number(props.at)
    const step = Number.isFinite(num) && num >= 0 ? num : undefined
    assignedStepRef.value = step
    return step
  }
  
  // 自动分配：使用全局计数器，按幻灯片页面隔离
  const slideId = $slidev?.nav?.currentSlideNo || 0
  if (!globalThis.__vComponentCounter[slideId]) {
    globalThis.__vComponentCounter[slideId] = 0
  }
  const step = globalThis.__vComponentCounter[slideId]++
  assignedStepRef.value = step
  return step
})

// 只在当前步骤显示（之前的会隐藏）
const isVisible = computed(() => {
  if (assignedStepRef.value === null) return false
  return $clicks.value === assignedStepRef.value
})
</script>
