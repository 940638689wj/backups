<template>
  <div class="my-order">
    <my-pageTitle>
      <div slot="title">我的订单</div>
    </my-pageTitle>

    <div class="no-order" v-if="!orderList.length">暂无订单...</div>

    <div class="goods-buy" v-for="(item, index) in orderList">
      <div class="title">
        <span class="order-num">订单: {{ item.orderId }}</span>
        <span class="success" v-if="item.orderState === 0">已成团</span>
        <span class="fail"  v-else-if="item.payState === 0">未付款</span>
        <span class="fail"  v-else-if="item.orderState === 1 && item.payState === 1">已付款,未成团</span>
        <span class="return"  v-else-if="item.orderState === 2">已退款</span>
      </div>
      <div class="goods-desc">
        <div class="goods-img">
          <img :src="item.act.goods.img">
        </div>
        <div class="name-and-price">
          <div class="name">{{ item.act.goods.title }}</div>
          <div class="price">
            ￥{{ item.act.price / 100 }}
            <div class="specifications">
              规格: {{ item.act.goods.spec }}装 X 1
            </div>
          </div>
        </div>
      </div>
      <div class="desc-button">
        <span @click="orderDetail(item)">详情</span>
      </div>
    </div>
    <loginDialog v-model="visibleLoginDialog" @loginSuccess="LoginSuccess"></loginDialog>

  </div>
</template>

<script>
  import { mapActions } from 'vuex'
  import loginDialog from './dialogs/login.vue'
  export default {
    components: { loginDialog },
    data () {
      return {
        orderList: [],
        search: {
          page: 0,
          size: 50
        },
        visibleLoginDialog: false,
        countGoods: 0
      }
    },
    created () {
      this.getOrderList()
    },
    methods: {
      /**
       * 分发 Action
       */
      ...mapActions('goodsInfo', [
        '_AddgoodsInfo'
      ]),
      getOrderList () {
        this.$http.post('pintuan/myOrderList', this.search).then(response => {
          this.orderList = response.data.json.content
          for (let i in this.orderList) {
            this.orderList[i].act.goods.img = this.orderList[i].act.goods.img && this.orderList[i].act.goods.img.split('|')[0]
          }
        }, (error) => {
          if (error.data.code === -2) {
            console.log('未登陆')
            this.visibleLoginDialog = true
          }
        })
      },
      LoginSuccess () {
        this.getOrderList()
      },
      orderDetail (vo) {
        console.log(vo)
        this._AddgoodsInfo(vo)
        this.$router.push('/orderDetail')
      }
    }
  }
</script>

<style lang="less">
  body {
    background-color: #f6f8fa;
  }
  .my-order {
    font-size: 26rem / 20;

    .no-order {
      margin-top: 120rem / 20;
      text-align: center;
    }

    .goods-buy {
      height: 350rem / 20;
      background-color: #ffffff;
      margin-top: 20rem / 20;
      .title {
        line-height: 80rem / 20;
        padding: 0 20rem / 20;
        span {
          float: right;
        }
        .order-num {
          float: left;
          font-size: 24rem / 20;
          color: #666666;
        }
        .success {
          color: #13ce66;
        }
        .fail {
          color: #ff4949;
        }
        .return {
          color: #198cff;
        }
      }
      .goods-desc {
        height: 170rem / 20;
        background-color: #f6f8fa;
        width: 100%;
        overflow: hidden;
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
        .buy-num {
          float: right;
          margin-top: 100rem / 20;
          margin-right: 20rem / 20;
        }
      }
      .desc-button {
        float: right;
        span {
          display: inline-block;
          height: 54rem / 20;
          line-height: 54rem / 20;
          width: 128rem / 20;
          text-align: center;
          border: 1rem / 20 solid #999999;
          border-radius: 4rem / 20;
          margin-top: 20rem / 20;
          margin-right: 30rem / 20;
          color: #666666;
        }
      }
    }
  }
</style>