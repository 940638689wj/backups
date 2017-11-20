<template>
  <div class="pay-success">
    <my-pageTitle>
      <div slot="title">{{ paySatus }}</div>
    </my-pageTitle>
    <div class="pay-status loading">
    </div>
    <div class="pay-status-str">
      <span>{{ paySatus }}</span> 
    </div>
    <div class="order-number">
      订单号: {{ orderId }}
    </div>
    <div class="success-desc">
      拼团成功，预计活动结束后统一进行发货
      <br/>
      可在订单管理查看该团是否成功，也可添加客服微信号进行咨询
    </div>
    <div class="option-button-wrap">
      <router-link class="go-buy-button" to="/">
        继续购物
      </router-link>
      <a class="order-manage-button" @click="GotoMyOrder">
        订单管理
      </a>
    </div>
    <div class="QR-code">
      <img src="../assets/QR-code.png">
      <div>
        保存图片至手机
        <br/>
        微信扫一扫时选择从相册选取二维码添加客服
      </div>
    </div>

  </div>
</template>

<script>
  import { mapActions } from 'vuex'
  export default {
    data () {
      return {
        paySatus: '支付中...',
        orderId: 999999999999,
        id: this.$route.params.orderId
      }
    },
    methods: {
      /**
       * 分发 Action
       */
      ...mapActions('global', [
        '_SetGoBackRouter'
      ]),
      GotoMyOrder () {
        this._SetGoBackRouter('/')
        this.$router.push('/myOrder')
      },
      /**
       * 刷新订单状态
       */
      RefreshOrderStatus () {
        this.$http.post('pintuan/getOrder', {id: this.id}).then(response => {
          this.orderId = response.data.json.orderId
          switch (response.data.json.payState) {
            case 1:
              this.$el.getElementsByClassName('pay-status')[0].className = 'pay-status loading'
              this.paySatus = '支付中...'
              let _this = this
              setTimeout(function () {
                _this.RefreshOrderStatus()
              }, 2000)
              break
            case 2:
              this.$el.getElementsByClassName('pay-status')[0].className = 'pay-status success'
              this.paySatus = '支付成功'
              break
            case 3:
              this.$el.getElementsByClassName('pay-status')[0].className = 'pay-status error'
              this.paySatus = '支付失败'
              break
            case 4:
              this.$el.getElementsByClassName('pay-status')[0].className = 'pay-status error'
              this.paySatus = '已退款'
              break
          }
        }, (error) => {
          this.$el.getElementsByClassName('pay-status')[0].className = 'pay-status error'
          this.paySatus = '订单状态查询失败'
          if (error.data.code === -2) {
            console.log('未登陆')
            this.visibleLoginDialog = true
          }
        })
      }
    },
    mounted () {
      this._SetGoBackRouter('/order/' + this.id)
      this.RefreshOrderStatus()
    }
  }
</script>

<style lang="less">
  .pay-success {
    >.pay-status {
      height: 200rem / 20;
      margin-top: 60rem / 20;
      &.success {
        background: url(../assets/pay-success.png) no-repeat 50%;
      }
      &.error {
        background: url(../assets/error-icon.png) no-repeat 50%;
      }
      &.loading {
        background: url(../assets/loading.gif) no-repeat 50%;
      }
    }
    >.pay-status-str {
      text-align: center;
    }
    .order-number {
      text-align: center;
      font-size: 36rem / 20;
      color: #333333;
      margin-top: 30rem / 20;
      margin-bottom: 20rem / 20;
    }
    .success-desc {
      font-size: 24rem / 20;
      color: #999999;
      width: 435rem / 20;
      margin: 0 auto;
      text-align: center; 
    }
    .option-button-wrap {
      text-align: center;
      a {
        color: #ffffff;
        display: inline-block;
        background-color: #198cff;
        text-align: center;
        width: 280rem / 20;
        height: 88rem / 20;
        line-height: 88rem / 20;
        font-size: 32rem / 20;
        margin: 50rem / 20 20rem/ 20 70rem / 20 auto;
        border-radius: 4rem / 20;
      }  
      .order-manage-button {
        color: #198cff;
        background-color: #fff;
        border: 1rem / 20 solid #198cff;
      }
    }
    .QR-code {
      text-align: center;
      img {
        width: 212rem / 20;
        height: 212rem / 20;
      }
      div {
        margin-top: 40rem / 20;
        font-size: 24rem / 20;
        color: #333333;
      }
    }

  }
</style>