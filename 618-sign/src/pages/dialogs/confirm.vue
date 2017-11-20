<template>
  <div class="dialogs-confirm" v-show="visible">
    <div class="dialogs-confirm-content">
    <slot></slot>
    </div>
    <div class="dialogs-confirm-button">
      <button @click="Cancel">{{ cancel }}</button>
      <button @click="Confirm">{{ confirm }}</button>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    cancel: {default: '取消', type: String},
    confirm: {default: '确认', type: String},
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
    },
    /**
     * 取消
     */
    Cancel () {
      this.Close()
      this.$emit('Callback', false)
    },
    /**
     * 确认
     */
    Confirm () {
      this.Close()
      this.$emit('Callback', true)
    }

  }
}
</script>

<style lang="less">
.dialogs-confirm {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translateY(-50%);
  overflow: hidden;
  width: 500rem / 20;
  background-color: #fff;
  margin-left: -250rem / 20;
  border-radius: 12rem / 20;
  box-shadow: 0 1rem / 20 3rem / 20 rgba(0,0,0,.3);
  // width: 500rem / 20;
  .dialogs-confirm-content {
    padding: 35rem / 20 55rem /20;
  }
  .dialogs-confirm-button {
    font-size: 0;
    overflow: hidden;
    text-align: center;
    border-top: 1rem / 20 solid #dddddd;
    button {
      border: 0;
      width: 50%;
      color: #0080ff;
      height: 90rem / 20;
      font-size: 34rem / 20;
      background-color: #fff;
      &:active, &:focus {
        outline: none;
      }
      &:nth-child(1) {
        border-right: 1rem / 20 solid #dddddd;
      }
    }
  }
}
</style>