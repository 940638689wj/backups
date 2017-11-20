<template>
  <div class="page-title" @click="Click">
    <slot name="title"></slot>
  </div>
</template>

<script>
  export default {
    data () {
      return {
      }
    },
    methods: {
       /**
       * 点击
       */
      Click () {
      }
    }
  }
</script>

<style lang="less" scoped>
  .page-title {
    background-color: #ffffff;
    font-size: 36rem / 20;
    text-align: center;
    color: #333333;
    line-height: 100rem / 20;
  }
</style>