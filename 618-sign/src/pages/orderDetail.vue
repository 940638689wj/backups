<template>
  <div class="order-detail">
    <my-pageTitle>
      <div slot="title">订单详情</div>
    </my-pageTitle>

    <div class="goods-buy">
      <div class="title">
        <div class="ing"     v-if="orderDetail.payState == 0">待支付</div>
        <div class="success" v-else-if="groupState == 0">已成团，活动结束后发货</div>
        <div class="ing"     v-else-if="groupState">差{{ groupState }}人成团(如果拼团失败，活动结束后退款)</div>
        <div class="fail"    v-else-if="groupState == -1">已退款</div>
      </div>
      <div class="goods-desc">
        <div class="goods-img">
          <img :src="orderDetail.act.goods.img">
        </div>
        <div class="name-and-price">
          <div class="name">{{ orderDetail.act.goods.title }}</div>
          <div class="price">
            ￥{{ orderDetail.act.price / 100 }}
            <div class="specifications">
              规格：{{ orderDetail.act.goods.spec }} X 1
            </div>
          </div>
        </div>
      </div>
      <div class="total-price">
        共1件商品，合计：<span>￥{{ orderDetail.act.price / 100 }}</span>
      </div>
    </div>

    <div class="addr-info">
      <div class="loaction-icon">
        <img src="../assets/location-icon.png">
      </div>
      <div class="address">
        <div class="receive-man">收货人：{{ orderDetail.receiverUser }}</div>
        <span class="tel">{{ orderDetail.receiverMobile }}</span>
        <div class="receive-address">
          福建省福州市{{ orderDetail.receiverAddr }}
        </div>
      </div>
    </div>

    <div class="order-num-time">
      <div>订单号：{{ orderDetail.orderId }}</div>
      <div v-if="orderDetail.payState === 1">付款时间：未付款</div>
      <div v-else>付款时间：{{ orderDetail.payTime | datetime }}</div>
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
  import { mapGetters } from 'vuex'
  export default {
    data () {
      return {
        countGoods: 0,
        groupState: 0,
        orderDetail: {}
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
      this.orderDetail = this._goodsInfo
      let state = this.orderDetail.act.maxPeopleCount - this.orderDetail.act.activityCount
      if (state === 0) {
        this.groupState = 0 // 已成团
      }
      else if (state) {
        this.groupState = state
      }
      else {
        this.groupState = -1
      }
    },
    methods: {
      getOrderDetail () {
        this.orderDetail = this.$route.query
      }
    }
  }
</script>

<style lang="less">
  body {
    background-color: #f6f8fa;
  }
  .order-detail {
    font-size: 26rem / 20;

    .goods-buy {
      background-color: #ffffff;
      margin-top: 20rem / 20;
      .title {
        line-height: 80rem / 20;
        text-align: center;
        font-size: 30rem / 20;
        color: #ffffff;
        .success {
          background-color: #13ce66;
        }
        .ing {
          background-color: #ff4949;
        }
        .fail {
          background-color: #198cff;
        }
      }
      .goods-desc {
        width: 100%;
        overflow: hidden;
        background-color: #f6f8fa;
        padding-bottom: 38rem / 20;
        .goods-img {
          width: 20%;
          float: left;
          margin: 20rem / 20 24rem / 20;
          img {
            width: 128rem / 20;
            height: 128rem / 20;
          }
        }
        .name-and-price {
          width: 70%;
          float: left;
          margin-top: 20rem / 20;
          div:nth-child(2) {
            margin-top: 40rem / 20;
            color: #ff4d00;
          }
          .specifications {
            float: right;
            margin-left: 30rem / 20;
            color: #666666;
          }
        }
      }
      .total-price {
        width: 100%;
        text-align: right;
        height: 80rem / 20;
        line-height: 80rem / 20;
        span {
          height: 55rem / 20;
          text-align: center;
          margin-right: 30rem / 20;
          color: #ff4d00;
        }
      }
    }

    .addr-info {
      background-color: #ffffff;
      height: 144rem / 20;
      margin-top: 20rem / 20;

      .loaction-icon {
        float: left;
        margin: 52rem / 20 30rem / 20 0 24rem / 20;
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
        }
      }
      i {
        float: right;
        font-size: 2rem;
        margin: 50rem / 20 20rem / 20 0 0;
      }
    }

    .order-num-time {
      margin-top: 20rem / 20;
      padding: 20rem / 20 20rem / 20;
      background-color: #ffffff;
      font-size: 24rem / 20;
      color: #666666;
    }

    .QR-code {
      text-align: center;
      margin-top: 100rem / 20;
      img {
        height: 200rem / 20;
        width: 200rem / 20;
      }
      div {
        margin-top: 40rem / 20;
        margin-bottom: 140rem / 20;
        font-size: 24rem / 20;
        color: #333333;
      }
    }

  }
</style>