<template>
  <div class="dialogs-wrap" v-show="visible">
    <div class="dialogs">
      <h3 class="dialogs-title">{{ title }}</h3>
      <div class="dialogs-content">
        <slot></slot>
      </div>
    </div>
    <div class="dialogs-close" @click="Close()">
    </div>
  </div>
</template>
<script>
export default {
  props: {
    title: String,
    value: {default: false, type: Boolean}
  },
  data () {
    return {
      visible: false
    }
  },
  watch: {
    value: function (val) {
      this.visible = val
    },
    visible: function (val) {
      this.$emit('input', val)
    }
  },
  methods: {
    /**
     * 关闭对话框
     */
    Close () {
      this.visible = false
    }
  }
}
</script>

<style lang="less">
  .dialogs-wrap {
    position: fixed;
    top: 50rem / 20;
    left: 50%;
    margin-left: -315rem / 20;
    .dialogs {
      width: 630rem / 20;
      height: 940rem / 20;
      background: url(../../assets/dialog-bg.png) no-repeat center;
      background-size: 100% 100%;
      .dialogs-title {
        font-size: 43rem / 20;
        color: #fff;
        padding-top: 90rem / 20;
      }
      .dialogs-content {
        margin: 0 auto;
        overflow: hidden;
        width: 535rem / 20;
        height: 720rem / 20;
      }
    }
    .dialogs-close {
      float: right;
      width: 56rem / 20;
      height: 80rem / 20;
      margin-right: 50rem / 20;
      background: url(../../assets/dialog-close.png) no-repeat center;
      background-size: 100% 100%;
    }
  }
</style>