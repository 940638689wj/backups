<template>
  <div class="confirm-order">
    <my-pageTitle>
      <div slot="title">确认订单</div>
    </my-pageTitle>
    <div class="title-bottom-line"></div>
    <div class="addr-info"  @click="AddAddressDialog">
      <div class="loaction-icon">
        <img src="../assets/location-icon.png">
      </div>
      <div class="add-new-address" v-if="!addressInfo.user">
        <div>新建收货地址</div>
        <div>此次拼团仅限福州地区</div>
      </div>
      <div class="address" v-if="addressInfo.user">
        <div class="receive-man">收货人：{{ addressInfo.user }}</div>
        <span class="tel">{{ addressInfo.mobile }}</span>
        <div class="receive-address" style="
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 2;
          overflow: hidden;
        ">
          收货地址：福建省福州市{{ addressInfo.addr }}
        </div>
      </div>
      <i class="fa fa-angle-right"></i>
    </div>
    <div class="goods-buy">
      <div class="blank"></div>
      <div class="goods-desc">
        <img :src="_goodsInfo.goods.img" alt="">
        <div class="name-and-price">
          <div style="
              display: -webkit-box;
              -webkit-box-orient: vertical;
              -webkit-line-clamp: 2;
              overflow: hidden;
            ">{{ _goodsInfo.goods.title }}</div>
          <div class="goodsPrice">￥{{ _goodsInfo.price / 100 }}</div>
          <div class="specifications">规格:{{ _goodsInfo.goods.spec }}</div>
        </div>
      </div>
      <div class="blank"></div>
<!--       <div class="buy-number">
        <div>购买数量</div>
        <my-input-number v-model="countGoods" :min="1" :max="500" @change="EditTempCount"></my-input-number>
      </div> -->
    </div>
    <div class="wechat-pay">
      <img src="../assets/wechat-pay.png">
      <span>微信支付</span>
      <input type="radio" value="1" v-model="payWay">
    </div>
    <div class="number-limit">
      活动名额有限,请尽快完成支付
    </div>
    <div class="confirm-pay">
      <span class="confirm-button" @click="ConfirmOrder">确定支付</span>
      <span class="confirm-msg">
        <span class="error-msg">{{ errorMsg }}</span>
        <span v-if="!errorMsg">
          共{{ countGoods }}件商品,合计:
          <span class="price">￥{{ countGoods * _goodsInfo.price / 100 || 0 }}</span>
        </span>
      </span>
    </div>
    <addAddressDialog v-model="addAddressDialogvisible" :addressInfo="addressInfo" @addAddress="AddAddress"></addAddressDialog>
  </div> 
</template>

<script>
  import { mapGetters } from 'vuex'
  import addAddressDialog from './dialogs/addAddress.vue'
  export default {
    components: { addAddressDialog },
    data () {
      return {
        addAddressDialogvisible: false,
        addressInfo: {user: null, mobile: null, addr: null},
        isNeedAdder: true,
        payWay: 1,
        countGoods: 1,
        errorMsg: ''
      }
    },
    computed: {
      /**
       * 映射 Getter
       */
      ...mapGetters('goodsInfo', [
        '_goodsInfo'
      ])
    },
    created () {
      let ua = window.navigator.userAgent.toLowerCase()
      if (ua.match(/MicroMessenger/i) && ua.match(/MicroMessenger/i).toString() === 'micromessenger') {
        console.log('是微信')
      }
      else {
        console.log('不是微信')
      }
      // 监听 订单 状态
      // let _this = this
      // let intervalId = setInterval(function () {
      //   _this.$http.post('pintuan/myOrderList', {page: 0, size: 10}).then(response => {
      //     if (response.data.code === 1) {
      //       // this.$router.push('/confirmOrder')
      //     }
      //   }, error => {
      //     if (error.data.code === -2) {
      //       console.log('未登录')
      //       console.log(intervalId)
      //       // this.visibleLoginDialog = true
      //     }
      //   })
      //   // if (this) {
      //   //   clearInterval(intervalId)
      //   // }
      // }, 3000)
    },
    methods: {
      AddAddress (vo) {
        this.addressInfo = vo
      },
      AddAddressDialog () {
        this.addAddressDialogvisible = true
      },
      EditTempCount (vo) {
        console.log(vo)
      },
      ConfirmOrder () {
        if (!this.addressInfo.mobile) {
          this.errorMsg = '请添加收货地址'
          return
        }
        if (!this.payWay) {
          this.errorMsg = '请选择支付方式'
          return
        }
        if (!this.addAddressDialogvisible) {
          console.log('发送订单请求')
          this.errorMsg = ''
          // 设置
          this.addressInfo.aid = this._goodsInfo.id
          this.$http.post('pintuan/order', this.addressInfo).then(response => {
            this.errorMsg = response.data.msg
            console.log(response.data.json)
            if (response.data.code === 1) {
              console.log(response.data.json)
              // let redirectUrl = window.location.origin + window.location.pathname + '#/paySuccess/' + response.data.json.id
              // let errorRedirectUrl = window.location.href
              // this.GetWeChatPayInfo(redirectUrl, errorRedirectUrl, response.data.json.id)
              // 支付成功后跳转到paySuccess页面
              // this.$router.push({
              //   path: '/paySuccess',
              //   query: {orderId: response.data.json.orderId}
              // })
            }
          }, error => {
            this.errorMsg = error.data.msg
          })
        }
      },
      /**
       * 获取微信支付信息
       */
      GetWeChatPayInfo (redirectUrl, errorRedirectUrl, orderId) {
        let serverUrl = 'http://www.lanhaitianwang.com/weiphp/wechat-js-php-serve/wechatPintuanPay.php?' + this.UrlEncode({redirectUrl: redirectUrl, errorRedirectUrl: errorRedirectUrl, orderId: orderId})
        // console.log('跳转地址', serverUrl)
        window.location.href = serverUrl
      },
      /**
       * 将对象转成URL参数字符串
       * @param {[type]} param  [description]
       * @param {[type]} key    [description]
       * @param {[type]} encode [description]
       */
      UrlEncode  (param, key = null, encode = null) {
        if (param === null) {
          return ''
        }
        var paramStr = ''
        var t = typeof (param)
        if (t === 'string' || t === 'number' || t === 'boolean') {
          paramStr += '&' + key + '=' + ((encode === null || encode) ? encodeURIComponent(param) : param)
        }
        else {
          for (var i in param) {
            var k = key === null ? i : key + (param instanceof Array ? '[' + i + ']' : '.' + i)
            paramStr += this.UrlEncode(param[i], k, encode)
          }
        }
        return paramStr
      }
    },
    mounted () {
      this.$http.post('pintuan/getAddress').then(response => {
        if (response.data.json !== undefined) {
          this.addressInfo.user = response.data.json.receiverUser
          this.addressInfo.mobile = response.data.json.receiverMobile
          this.addressInfo.addr = response.data.json.receiverAddr
        }
        console.log(response)
      }, error => {
        console.log(error)
      })
    }

  }
</script>

<style lang="less">
  body {
    background-color: #f6f8fa;
  }
  .confirm-order {
    font-size: 26rem / 20;
    .title-bottom-line {
      margin-top: 11rem / 20;
      height: 6rem / 20;
      background-image: url(../assets/title-line.png);
      border-bottom: 1rem / 20 solid #dddddd;
    }
    .addr-info {
      background-color: #ffffff;
      height: 144rem / 20;

      .loaction-icon {
        float: left;
        margin: 52rem / 20 30rem / 20 0 24rem / 20;
      }

      .add-new-address {
        float: left;
        div:nth-child(1) {
          margin-top: 33rem / 20;
        }
        div:nth-child(2) {
          color: red;
          margin-top: 10rem / 20;
        }
      }
      .address {
        float: left;
        width: 80%;
        .tel {
          float: right;
          margin-top: -30rem / 20;
        }
        .receive-man {
          margin-top: 18rem / 20;
        }
        .receive-address {
          margin-top: 10rem / 20;
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 2; //文本行数
          overflow: hidden;
        }
      }
      i {
        float: right;
        font-size: 2rem;
        margin: 50rem / 20 20rem / 20 0 0 ;
      }
    }

    .goods-buy {
      height: 200rem / 20;
      margin-top: 20rem / 20;
      background-color: #ffffff;
      overflow: hidden;
      .blank {
        width: 100%;
        height: 20rem / 20;
      }
      .goods-desc {
        background-color: #f6f8fa;
        height: 160rem / 20;
        width: 95%;
        margin: 0 auto 0 auto;
        img {
          float: left;
          margin: 18rem / 20 20rem / 20;
          width: 128rem / 20;
          height: 128rem / 20;
        }
        .name-and-price {
          float: left;
          margin-top: 18rem / 20;
          div:nth-child(1) {
            width: 530rem / 20;
          }
          .goodsPrice {
            margin-top: 20rem / 20;
            color: #ff4d00;
            display: inline-block;
          }
          .specifications {
            float: right;
            margin-top: 20rem / 20;
          }
        }
      }
      .buy-number {
        width: 95%;
        margin: 0 auto;
        height: 60rem / 20;

        div:nth-child(1) {
          line-height: 53rem / 20;
          float: left;
          font-size: 28rem / 20;
        }
        div:nth-child(2) {
          float: right;
          border-radius: 7rem / 20;
          span:hover {
            background-color: #ffffff;
          }
          .decrease {
            border-bottom-left-radius: 7rem / 20;
            border-top-left-radius: 7rem / 20;
          }
          .increase {
            border-bottom-right-radius: 7rem / 20;
            border-top-right-radius: 7rem / 20;
          }
        }
      }
    }

    .wechat-pay {
      margin-top: 20rem / 20;
      background-color: #ffffff;
      height: 88rem / 20;
      img {
        float: left;
        margin: 20rem / 20 26rem / 20;
      }
      span {
        display: inline-block;
        margin-top: 20rem / 20;
      }
      input {
        height: 38rem / 20;
        width: 35rem / 20;
        float: right;
        margin-top: 27rem / 20;
        margin-right: 27rem / 20;
        background-color: #ffffff;
      }
    }

    .number-limit {
      margin-top: 20rem / 20;
      margin-left: 30rem / 20;
      margin-bottom: 200rem / 20;
      font-size: 24rem / 20;
      color: #ff4949;
    }

    .confirm-pay {
      position: fixed;
      bottom: 0;
      height: 98rem / 20;
      line-height: 98rem / 20;
      width: 100%;
      background-color: #ffffff;
      .confirm-button {
        float: right;
        width: 240rem / 20;
        background-color: #3F8EFE;
        text-align: center;
        color: #ffffff;
        font-size: 32rem / 20;
      }
      .confirm-msg {
        float: right;
        .error-msg {
          color: red;
          margin-right: 30rem / 20;
        }
        .price {
          color: #F15012;
          margin-right: 30rem / 20;
        }
      }
    }

  }
</style>