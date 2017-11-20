<template>
  <div class="order-page">
    <div class="order-img">
      <img :src="_goodsInfo.goods.img" alt="">
    </div>
    <div class="order-info">
      <h3>{{ _goodsInfo.goods.title }}</h3>
      <div class="order-info-item">
        <span class="price">¥{{ _goodsInfo.price / 100 || 0 }}</span>
        <span class="sale-price">¥{{ _goodsInfo.goods.price / 100 || 0 }}</span>
        <span class="spec">规格: {{ _goodsInfo.goods.spec }}</span>
        <span class="count">累计销售{{ _goodsInfo.goods.sales || 0 }}件</span>
      </div>
    </div>
    <div class="order-info-buy gray">
      <h3><hr>距离活动结束还剩<hr></h3>
      <div class="timer">
        <div class="timer-unit">{{ parseInt(timer.day / 10) || 0 }}</div>
        <div class="timer-unit">{{ timer.day % 10 || 0 }}</div>
        天
        <div class="timer-unit">{{ parseInt(timer.hour / 10) || 0 }}</div>
        <div class="timer-unit">{{ timer.hour % 10 || 0 }}</div>
        时
        <div class="timer-unit">{{ parseInt(timer.min / 10) || 0 }}</div>
        <div class="timer-unit">{{ timer.min % 10 || 0 }}</div>
        分
        <div class="timer-unit sec">{{ parseInt(timer.sec / 10) || 0 }}</div>
        <div class="timer-unit sec">{{ timer.sec % 10 || 0 }}</div>
        秒
      </div>
      <button @click="Join">
        <span class="rule">满{{ _goodsInfo.maxPeopleCount }}人就成团</span>
        <span class="content">去参团</span>
      </button>
      <div class="label label-full">
        来晚一步<br>
        该团已被挤爆<br>
        {{ isWait ? '请稍15分钟后再试' : '等明天来看看有没有名额吧'}}
      </div>
      <div class="label label-overtime">
        来晚一步<br>
        该团已结束<br>
        等明天来看看有没有活动吧
      </div>
    </div>
    <div class="order-desc">
      <div class="title"> 图文详情 </div>
      <div class="desc">{{ _goodsInfo.goods.content }} </div>
      <div class="desc-img">
        <img v-for="item in _goodsInfo.goods.descImg" :src="item" alt="">
      </div>
    </div>
    <loginDialog v-model="visibleLoginDialog" @loginSuccess="LoginSuccess"></loginDialog>
  </div>
</template>


<script>
  import { mapGetters } from 'vuex'
  import loginDialog from './dialogs/login.vue'
  export default {
    components: { loginDialog },
    data () {
      return {
        visibleLoginDialog: false,
        startTime: 0, // 活动开始时间
        timer: {
          day: 0,
          hour: 0,
          min: 0,
          sec: 0
        },
        isWait: ''
      }
    },
    mounted () {
      document.body.scrollTop = 0 // 回到页面顶部
      if (this._goodsInfo.maxPeopleCount - this._goodsInfo.activityCount <= 0) {
        document.getElementsByClassName('order-info-buy gray')[0].className = 'order-info-buy end'
        if (this._goodsInfo.maxPeopleCount - this._goodsInfo.payCount > 0) {
          this.isWait = 1
        }
        console.log('该团已被挤爆')
        return
      }
      if (this._goodsInfo.endTime < new Date().getTime()) {
        // 开团时间小于现在时间
        document.getElementsByClassName('order-info-buy gray')[0].className = 'order-info-buy overtime'
        console.log('该团已结束')
        return
      }
      this.startTime = this._goodsInfo.endTime
      let _this = this
      setInterval(function () {
        _this.Timer()
      }, 1000)
      this.SetShareInfo()
    },
    computed: {
      /**
       * 映射 Getter
       */
      ...mapGetters('goodsInfo', [
        '_goodsInfo'
      ])
    },
    methods: {
      Join () {
        this.$http.post('pintuan/myOrderList', {page: 0, size: 10}).then(response => {
          if (response.data.code === 1) {
            this.$router.push('/confirmOrder')
          }
        }, error => {
          if (error.data.code === -2) {
            console.log('未登录')
            this.visibleLoginDialog = true
          }
        })
      },
      /**
       * 设置分享信息
       */
      SetShareInfo () {
        let shareDate = {}
        this.$http.post('http://www.lanhaitianwang.com/weiphp/wechat-js-php-serve/JSSDK/getSign.php', {url: window.location.origin + window.location.pathname + window.location.search}).then(response => {
        }, error => {
          // 因为服务器没有返回 code = 1 的正确码, 所以 data 要在 error 接
          console.log(error, 'order error')
          window.readyWeChatJs(error.data)
          shareDate.title = this._goodsInfo.goods.title
          shareDate.link = window.location.origin + window.location.pathname + window.location.search
          shareDate.desc = this._goodsInfo.goods.content
          shareDate.imgUrl = this._goodsInfo.goods.img
          window.onMenuShareTimeline(shareDate)
          window.onMenuShareAppMessage(shareDate)
        })
      },
      LoginSuccess () {
        this.$router.push('/confirmOrder')
      },
      /**
       * 计时器
       */
      Timer () {
        let leftTime = ((this.startTime) - Date.parse(new Date())) / 1000
        if (leftTime < 0) {
          document.getElementsByClassName('order-info-buy')[0].className = 'order-info-buy overtime'
        }
        this.timer.day = parseInt(leftTime / 60 / 60 / 24, 10) // 获取剩余天数
        this.timer.hour = parseInt(leftTime / 60 / 60 % 24, 10) // 获取剩余小时数
        this.timer.min = parseInt(leftTime / 60 % 60, 10) // 获取剩余分钟数
        this.timer.sec = parseInt(leftTime % 60, 10) // 获取剩余秒数
      }
    }
  }
</script>


<style lang="less">
.order-page {
  .go-back {

  }
  .order-img {
    overflow: hidden;
    height: 488rem / 20;
    img {
      width: 100%;
    }
  }
  .order-info {
    overflow: hidden;
    background-color: #fff;
    border-bottom: 20rem / 20 solid #f6f8fa;
    h3 {
      margin: 0;
      font-weight: 400;
      padding: 28rem / 20;
      font-size: 32rem / 20;
    }
    .order-info-item {
      color: #bbb;
      padding-left: 28rem / 20;
      font-size: 26rem / 20;
      overflow: hidden;
      .price {
        color: #ff4d00;
        font-size: 48rem / 20;
      }
      .sale-price {
        text-decoration:line-through;
      }
      .spec {
        padding-left: 30rem / 20;
      }
      .count {
        padding-top: 15rem / 20;
        color: #000;
        float: right;
        padding-right: 55rem / 20;
      }
    }
  }
  .order-info-buy {
    width: 100%;
    text-align: center;
    height: 256rem / 20;
    background-color: #f3253a;
    border-bottom: 20rem / 20 solid #fff ;
    h3 {
      text-align: center;
      padding: 20rem / 20 0;
      // margin: 20rem / 20;
      margin: 0;
      color: #fff;
      font-weight: 500;
      font-size: 22rem / 20;
      hr {
        display: inline-block;
        width: 50rem / 20;
      }
    }
    .timer {
      color: #fff;
      font-size: 20rem / 20;
      margin-bottom: 45rem / 20;
      .timer-unit {
        width: 24rem / 20;
        height: 40rem / 20;
        text-align: center;
        font-size: 24rem / 20;
        display: inline-block;
        background-color: #000;
        line-height: 40rem / 20;
        border-radius: 8rem / 20;
        &.sec {
          color: #f32539;
          background-color: #fff;
        }
      }
    }
    > button {
      // display: block;
      border: 0;
      width: 524rem / 20;
      height: 84rem / 20;
      background: url(../assets/yellow-orange-button.png) no-repeat center;
      background-size: 100% 100%;
      &:active, &:focus {
        outline: none;
        background: url(../assets/yellow-orange-button-click.png) no-repeat center;
        background-size: 100% 100%;
      }
      span {
        width: 45%;
        color: #532900;
        text-align: center;
        display: inline-block;
        &.rule {
          font-size: 24rem / 20;
        }
        &.content {
          font-weight: bold;
          font-size: 36rem / 20;
        }
      }
    }
    .label {
      display: none;
    }
    &.gray {
      background-color: #98a2ab;
    }
    &.end {
      background: #f3253a url(../assets/label.png) no-repeat center;
      background-size: 70% 70%;
      h3, button, .timer{
        display: none;
      }
      .label-full {
        display: block;
        font-size: 32rem / 20;
        padding-top: 60rem / 20;
      }
    }
    &.overtime {
      background: #f3253a url(../assets/label.png) no-repeat center;
      background-size: 70% 70%;
      h3, button, .timer{
        display: none;
      }
      .label-overtime {
        display: block;
        font-size: 32rem / 20;
        padding-top: 60rem / 20;
      }
    }
  }
  .order-desc { 
    .title {
      color: #fff;
      height: 60rem / 20;
      font-size: 28rem / 20;
      background-color: #333;
      line-height: 60rem / 20;
      padding-left: 32rem / 20;
    }
    .desc {
      padding: 35rem / 20 40rem / 20 40rem / 20 40rem / 20;
      text-indent: 2em;
      font-size: 30rem / 20;
    }
    .desc-img {
      text-align: center;
      img {
        width: 100%;
        margin-top: 20rem / 20;
      }
    }
  }
}
</style>