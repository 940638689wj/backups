<template>
  <div class="dialogs-prizes-list">
    <dialogs :title="title" v-model="visible">
    <div class="prizes-list-title">
      <span>奖项</span>
      <span>奖品</span>
      <span>领奖</span>
    </div>
    <ul class="prizes-list">
      <li>
        <span>累积上传15天</span>
        <span>小浣熊酸奶机</span>
        <span><button class="active" @click="visibleConfirm = true">领取</button></span>
      </li>
      <li>
        <span>累积上传15天</span>
        <span>小浣熊酸奶机</span>
        <span><button>领取</button></span>
      </li>
      <li>
        <span>累积上传15天</span>
        <span>小浣熊酸奶机</span>
        <span><button>领取</button></span>
      </li>
      <li>
        <span>累积上传15天</span>
        <span>小浣熊酸奶机</span>
        <span><button>领取</button></span>
      </li>
      <li>
        <span>累积上传15天</span>
        <span>小浣熊酸奶机</span>
        <span><button>领取</button></span>
      </li>
      <li>
        <span>累积上传15天</span>
        <span>小浣熊酸奶机</span>
        <span><button>领取</button></span>
      </li>
      <li>
        <span>累积上传15天</span>
        <span>小浣熊酸奶机</span>
        <span><button>领取</button></span>
      </li>
    </ul>
    </dialogs>
    <confirm v-model="visibleConfirm" cancel="继续累积" confirm="领取" @Callback="ReceiveRrizes"><p class="prizes-confirm-content">领取后无法继续累积</p></confirm>
  </div> 
</template>

<script>
  import dialogs from './base.vue'
  import confirm from './confirm.vue'
  export default {
    components: { dialogs, confirm },
    props: {
      value: {default: false, type: Boolean}
    },
    data () {
      return {
        visible: false,
        visibleConfirm: false,
        title: '活动奖品'
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
       * 领取奖品回调
       * @param {Boolean} confirm 确认领取返回true
       */
      ReceiveRrizes (confirm) {
        console.log('ReceiveRrizes', confirm)
      }
    }
  }
</script>

<style lang="less">
.prizes-list-title {
  width: 100%;
  font-size: 0;
  color: #572a00;
  > span {
    font-weight: bold;
    width: 33.33%;
    font-size: 30rem / 20;
    display: inline-block;
  }
}
.prizes-list {
  padding: 0;
  list-style: none;
  border-top: 1rem / 20 solid #63d4f2;
  > li {
    padding: 20rem / 20 0;
    border-bottom: 1rem / 20 solid #63d4f2;
    line-height: 30rem / 20;
    > span {
      // font-weight: bold;
      width: 170rem / 20;
      font-size: 24rem / 20;
      display: inline-block;
      > button {
        font-size: 24rem / 20;
        color: #52251a;
        font-weight: 600;
        padding: 0;
        user-select:none;
        width: 98rem / 20;
        height: 38rem / 20;
        background: url(../../assets/gray-orange-button.png) no-repeat center;
        background-size: 100% 100%;
        &:active, &:focus {
          outline: none;
        }
        &.active {     
          background: url(../../assets/yellow-orange-button.png) no-repeat center;
          background-size: 100% 100%;
          &:active, &:focus {
            outline: none;
            background: url(../../assets/yellow-orange-button-click.png) no-repeat center;
            background-size: 100% 100%;
          }
        }
        border: 0;
      }
    }
  }
}
.prizes-confirm-content {
  font-size: 32rem / 20;
}
</style>