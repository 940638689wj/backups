<template>
  <component :is="templateName"></component>
</template>

<script>
  import templateDefault from './templateDefault.vue'
  export default {
    components: { templateDefault },
    computed: {
      /**
       * 系统模板名称
       * @return {string}
       */
      templateName () {
        let t = this.$route.meta.t || 0
        return [
          'templateDefault'
        ][t]
      }
    },
    methods: {
    }
  }
</script>

<style lang="less">
  @import '~global/main.less';

  html, body {
    margin: 0;
    height: 100%;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }

  .page-box {
    overflow: hidden;
    margin-top: 10px;

    .left {
      float: left;
      font-size: 14px;
      color: #333;

      select {
        outline: none;
        width: 48px;
        height: 28px;
        border-color: @borderColor;
      }
    }

    .right {
      float: right;
    }
  }
</style>