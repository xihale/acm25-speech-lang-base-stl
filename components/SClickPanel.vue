<template>
  <div class="s-click-panel">
    <slot />
  </div>
</template>

<script setup>
import { provide } from 'vue'

const STACK_CLICK_SYMBOL = Symbol.for('acm25.s-click-panel')

const usedSteps = new Set()
let counter = -1  // 从 -1 开始，第一个元素会得到 0

function normalize(value) {
  const num = Number(value)
  return Number.isFinite(num) ? Math.max(0, Math.floor(num)) : undefined
}

function allocateStep(explicit) {
  const normalized = normalize(explicit)

  if (normalized != null) {
    usedSteps.add(normalized)
    if (normalized > counter)
      counter = normalized
    return normalized
  }

  // 自动分配：递增，从 0 开始
  counter += 1
  while (usedSteps.has(counter))
    counter += 1
  usedSteps.add(counter)
  return counter
}

provide(STACK_CLICK_SYMBOL, {
  registerStep(explicit) {
    return allocateStep(explicit)
  },
})
</script>
