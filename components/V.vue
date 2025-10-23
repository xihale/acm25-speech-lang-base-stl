<!--
  V 组件 - 基于 v-click 的点击显示组件
  
  用法：
    在 two-cols 布局中：
    ::left::
    <v>自动分配为 0（进入时即显示）</v>
    <v>自动分配为 1</v>
    
    ::right::
    <v>自动分配为 0（进入时即显示）</v>
    <v>自动分配为 1</v>
  
  特性：
    - 使用 Slidev 原生 v-click 机制
    - 每次只显示当前块（通过 v-show）
    - 左右 panel 独立计数，都从 0 开始
    - 第一个元素（步骤 0）在进入幻灯片时就显示
-->
<template>
  <div
    v-show="isVisible"
    class="v-container"
  >
    <slot />
  </div>
</template>

<script setup>
import { inject, computed, onMounted } from 'vue'
import { useSlideContext } from '@slidev/client'

const STACK_CLICK_SYMBOL = Symbol.for('acm25.s-click-panel')

const props = defineProps({
  at: {
    type: [Number, String],
    default: undefined,
  },
})

const panel = inject(STACK_CLICK_SYMBOL, null)
const { $clicks } = useSlideContext()

// 分配步骤号（只执行一次）
const assignedStep = (() => {
  if (panel?.registerStep) {
    // 在 SClickPanel 内部，使用其自动分配机制
    return panel.registerStep(props.at)
  }
  
  // 不在 SClickPanel 内部
  if (props.at !== undefined) {
    const num = Number(props.at)
    return Number.isFinite(num) && num >= 0 ? num : 0
  }
  
  // 默认为 0（这样第一个元素在进入时就显示）
  return 0
})()

// 调试：打印分配的步骤
onMounted(() => {
  console.log('V component mounted, assignedStep:', assignedStep, 'current $clicks:', $clicks.value)
})

// 只在当前步骤显示
const isVisible = computed(() => {
  const visible = $clicks.value === assignedStep
  console.log('isVisible check: $clicks =', $clicks.value, 'assignedStep =', assignedStep, 'visible =', visible)
  return visible
})
</script>
