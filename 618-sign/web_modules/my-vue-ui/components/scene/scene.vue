<template>
  <div class="scene-container">
    <div class="scene-section">
      <div class="scene-head">
        <h3 class="title-strong border-bottom-blue" v-text="title"></h3>
      </div>
      <div class="scene-content">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      title: ''
    }
  }
</script>

<style lang="less">
  @import '~global/variable.less';
  /** scene容器样式 **/
  .scene-container {
    margin: 20px;
    padding: 29px;
    border-radius: 2px;
    background: @bgColor;
    border: 1px solid @borderColor;

    .block {
      margin: 0;
      overflow: hidden;
      padding: 10px 0 10px 0;
    }

    .scene-float-right * {
      float: right;
    }

    .scene-float-left * {
      float: left;
    }

    .title-strong {
      margin: 0;
      font-size: 16px;
      font-weight: bold;
    }

    .border-bottom-blue {
      min-width: 60px;
      padding-bottom: 10px;
      display: inline-block;
      border-bottom: 4px solid @baseColor;
    }

    /** scene容器head **/
    .scene-head {
      border-bottom: 1px solid @borderColor;
    }

    .scene-content {
      margin: 0;
      padding: 0;
    }

    .el-button--text {
      padding: 0;
    }

    .el-pagination {
      background-color: inherit;
    }
  }
</style>