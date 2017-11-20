<template>
  <div class="index-home">
    <div class="banner">
      <img src="../assets/home-banner.png" alt="">
    </div>
    <div class="content">
      <div class="my-order" @click="GoToMyOrder">
        <span>我的订单</span>
        <i class="fa fa-angle-right"></i>
        <!-- <i class="fa fa-angle-right"></i> -->
      </div>
      <ul class="order-list">
        <li class="hot-sale" v-for="(item, index) in list" :class="{hot:item.goods.high===1}">
          <img :src="item.goods.img" @click="ToOrder(item)">
          <div class="order-item-info">
            <h3 @click="ToOrder(item)" style="
              display: -webkit-box;
              -webkit-box-orient: vertical;
              -webkit-line-clamp: 3;
              overflow: hidden;
            ">{{ item.goods.title }}</h3>
            <p class="tag">{{ item.goods.tags | truncate(10, '') }}</p>
            <p class="addr">仅限福州</p>
            <p class="price"><span>¥{{ item.goods.price / 100 || 0 }}</span><span class="unit">规格: {{ item.goods.spec }}</span></p>
            <button @click="ToOrder(item)">
              <span>{{ item.maxPeopleCount }}人团:
                <span class="red">¥{{ item.price / 100 }}</span>
              </span>
              <span class="button-txt"> <a href="javascript:void(0)">参团&nbsp;<i class="fa fa-angle-right"></i></a></span>
            </button>
          </div>
        </li>
      </ul>
      <div class="rule">
        <h3> <hr> 参团须知 <hr> </h3>
        <span v-for="item in rule">{{ item }}</span>
      </div>
    </div>
  </div> 
</template>

<script>
  import { mapActions } from 'vuex'
  export default {
    data () {
      return {
        search: {
          page: 0,
          size: 100
        },
        list: [],
        visibleRule: false,
        visiblePrizesList: false,
        visibleInvitation: false,
        visibleLikes: false,
        visibleConfirm: false,
        rule: ''
      }
    },
    created () {
      this.getList()
      this.getRule()
      this.SetShareInfo()
    },
    methods: {
      /**
       * 分发 Action
       */
      ...mapActions('goodsInfo', [
        '_AddgoodsInfo'
      ]),
      getList () {
        this.$http.post('pintuan/getActivitys', this.search).then(response => {
          this.list = response.data.json.content
          document.body.scrollTop = 0 // 回到页面顶部 从商品详情返回会白屏的问题
          for (let i in this.list) {
            if (this.list[i].goods.img) {
              this.list[i].goods.descImg = this.list[i].goods.img.split('|')
              this.list[i].goods.descImg.splice(0, 1)
              this.list[i].goods.img = this.list[i].goods.img.split('|')[0]
            }
          }
        }, error => {
          console.log(error)
        })
      },
      /**
       * 获取index页底部规则
       */
      getRule () {
        this.$http.post('pintuan/getRule').then(response => {
          this.rule = response.data.json.split('\n')
        }, error => {
          console.log(error)
        })
      },
      /**
       * 设置分享信息
       */
      SetShareInfo () {
        let getConfigUrl = 'http://www.lanhaitianwang.com/weiphp/wechat-js-php-serve/JSSDK/getSign.php'
        this.$http.post(getConfigUrl, {url: window.location.origin + window.location.pathname + window.location.search}).then(response => {
          console.log(response, 'index success')
          window.readyWeChatJs(response.data)
        }, error => {
          console.log(error, 'index error')
          window.readyWeChatJs(error.data)
          let shareDate = {}
          shareDate.title = '【多！好！省！】高端大气上档次的深海大鱼限时抢！'
          shareDate.link = window.location.origin + window.location.pathname
          shareDate.desc = '30元海鲈鱼！140元法国银鳕鱼！120元阿根廷红虾！通通包邮！高档海产品放血大卖，邀好友一起来拼团！'
          shareDate.imgUrl = window.location.origin + window.location.pathname + 'static/img/wechat-share.png'
          window.onMenuShareTimeline(shareDate)
          window.onMenuShareAppMessage(shareDate)
        })
      },
      /**
       * 去开团
       * @param  {Object} vo 商品详情
       */
      ToOrder (vo) {
        console.log(vo)
        this._AddgoodsInfo(vo)
        this.$router.push({
          path: '/order',
          parmary: vo
        })
      },
      /**
       * 去我的订单
       */
      GoToMyOrder () {
        this.$router.push('/myOrder')
      },
       /**
       * 点击上传图片上传按钮
       */
      HandleClick (event) {
        event.currentTarget.childNodes[0].click()
      },
            /**
       * 用户选择完成内容后触发, 发送图片消息
       */
      HandleChange (event) {
        let files = event.target.files
        if (!files) {
          return
        }
        let formData = new window.FormData() // 创建FormData对象
        formData.append('imgType', 4)
        formData.append('fileUps', files[0])
        // 上传图片到本地服务器
/*        this.$http.post('uploadImgs.do', formData).then((response) => {
        }) */
        console.log(formData)
      }
    }
  }
</script>

<style lang="less">
  .index-home {
    background-color: #ff7323;
    text-align: center;
    > .banner {
      img {
        width: 100%;
      }
    }

    .content {
      padding: 32rem / 20 24rem / 20;
      >.my-order {
        font-weight: 500;
        height: 88rem / 20;
        font-size: 28rem / 20;
        background-color: #fff;
        line-height: 88rem / 20;
        border-radius: 4rem / 20;
        span {
          float: left;
          padding-left: 20rem / 20;
        }
        i {
          color: #ddd;
          float: right;
          line-height: 88rem / 20;
          padding-right: 50rem / 20;
        }
      }
      .order-list {
        padding: 0;
        list-style: none;
        li {
          overflow: hidden;
          padding: 20rem / 20; 
          margin-top: 30rem / 20;
          background-color: #fff;
          border-radius: 4rem / 20;
          &.hot-sale {
            background-color: #fff;
          }
          &.hot {
            background: #fff url(../assets/hot-sale.png) no-repeat right top;
          }
          img {
            width: 200rem / 20;
            height: 260rem / 20;
            float: left;
          }
          .order-item-info {
            float: left;
            text-align: left;
            display: inline-block;
            margin-left: 10rem / 20;
            > h3 {
              padding: 0;
              margin: 0;
              height: 107rem / 20;
              width: 380rem / 20;
              font-size: 26rem / 20 !important;
            }
            > .tag {
              display: inline-block;
              margin: 0;
              width: 320rem / 20;
              text-overflow: ellipsis;
            }
            > .addr {
              display: inline-block;
              margin: 0;
              color: #666;
              font-size: 24rem / 20;
              &:before {
                float: left;
                content: "　";
                display: block;
                width: 18rem / 20;
                height: 22rem / 20;
                line-height: 24rem / 20;
                padding-top: 10rem / 20;
                background: url(../assets/mark.png) no-repeat center;
              }
            }
            .price {
              color: #999;
              margin: 5rem / 20 0;
              font-size: 26rem / 20;
              text-decoration:line-through;
              .unit {
                float: right;
              }
            }
            button {
              border: 0;
              font-size: 0;
              padding: 2rem / 20;
              width: 440rem / 20;
              height: 80rem / 20;
              background-color: #f3253a;
              // text-align: right;
              span {
                float: left;
                overflow: hidden;
                text-align: center;
                width: 300rem / 20;
                height: 76rem / 20;
                font-size: 28rem / 20;
                line-height: 76rem / 20;
                display: inline-block;
                background-color: #fff;
                &.red {
                  float: right;
                  width: 150rem / 20;
                  color: #ff4d00;
                  height: 76rem / 20;
                }
              }
              .button-txt {
                float: right;
                color: #fff;
                width: 130rem / 20;
                background-color: #f3253a;
                a {
                  color: #fff;
                }
              }
            }
          }
        }
      }
    }

    .rule {
      color: #fff;
      text-align: left;
      h3 {
        font-size: 30rem / 20;
        text-align: center;
        hr {
          width: 60rem / 20;
          display: inline-block;
        }
      }
      span {
        font-size: 10rem / 20;
        display: block;
      }
    }
  }
</style>