<template>
  <div class="slidev-layout two-cols" :class="$props.class">
    <div class="flex gap-4 h-full" :class="$props.layoutClass">
      <s-click-panel class="col-left">
        <slot />
      </s-click-panel>
      <s-click-panel class="col-right">
        <slot name="right" />
      </s-click-panel>
    </div>
  </div>
</template>

<script setup>
import SClickPanel from '../components/SClickPanel.vue'

defineProps({
  class: {
    type: String,
    default: '',
  },
  layoutClass: {
    type: String,
    default: '',
  },
})
</script>
