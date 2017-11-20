<template>
  <div class="dialogs-likes">
    <dialogs :title="title" v-model="visible">
    <div class="likes-list-title">
      <span>排名</span>
      <span>昵称</span>
      <span><img src="../../assets/hearth.png" alt=""></span>
    </div>
    <ul class="likes-list">
      <li>
        <span class="rank">1</span>
        <span>
          <img src="../../assets//test/1.jpg" alt="" class="user-head">
          <span class="user-name"> 月亮弯弯</span>
        </span>
        <span>88888个</span>
      </li>
      <li>
        <span  class="rank">2</span>
        <span>
          <img src="../../assets//test/1.jpg" alt="" class="user-head">
          <span class="user-name"> 月亮弯弯</span>
        </span>
        <span>88888个</span>
      </li>
      <li>
        <span  class="rank">3</span>
        <span>
          <img src="../../assets//test/1.jpg" alt="" class="user-head">
          <span class="user-name"> 月亮弯弯</span>
        </span>
        <span>88888个</span>
      </li>
      <li>
        <span  class="rank">4</span>
        <span>
          <img src="../../assets//test/1.jpg" alt="" class="user-head">
          <span class="user-name"> 月亮弯弯</span>
        </span>
        <span>88888个</span>
      </li>
      <li>
        <span  class="rank">5</span>
        <span>
          <img src="../../assets//test/1.jpg" alt="" class="user-head">
          <span class="user-name"> 月亮弯弯</span>
        </span>
        <span>88888个</span>
      </li>
      <li>
        <span  class="rank">6</span>
        <span>
          <img src="../../assets//test/1.jpg" alt="" class="user-head">
          <span class="user-name"> 月亮弯弯</span>
        </span>
        <span>88888个</span>
      </li>
      <li>
        <span  class="rank">7</span>
        <span>
          <img src="../../assets//test/1.jpg" alt="" class="user-head">
          <span class="user-name"> 月亮弯弯</span>
        </span>
        <span>88888个</span>
      </li>
      <li>
        <span  class="rank">8</span>
        <span>
          <img src="../../assets//test/1.jpg" alt="" class="user-head">
          <span class="user-name"> 月亮弯弯</span>
        </span>
        <span>88888个</span>
      </li>
      <li>
        <span class="rank">9</span>
        <span>
          <img src="../../assets//test/1.jpg" alt="" class="user-head">
          <span class="user-name"> 月亮弯弯</span>
        </span>
        <span>88888个</span>
      </li>
      <li>
        <span>10</span>
        <span>
          <img src="../../assets//test/1.jpg" alt="" class="user-head">
          <span class="user-name"> 月亮弯弯</span>
        </span>
        <span>88888个</span>
      </li>
    </ul>
    </dialogs>
  </div> 
</template>

<script>
  import dialogs from './base.vue'
  export default {
    components: { dialogs },
    props: {
      value: {default: false, type: Boolean}
    },
    data () {
      return {
        visible: false,
        title: '点赞排行榜'
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
    methods: {}
  }
</script>

<style lang="less">
.dialogs-likes {  
  .likes-list-title {
    font-size: 0;
    width: 100%;
    color: #572a00;
    > span {
      width: 33.33%;
      font-weight: bold;
      font-size: 30rem / 20;
      display: inline-block;
    }
  }
  .likes-list {
    padding: 0;
    list-style: none;
    margin-top: 8rem / 20;
    border-top: 1rem / 20 solid #63d4f2;
    > li {
      font-size: 0;
      height: 48rem / 20;
      padding: 10rem / 20 0;
      line-height: 30rem / 20;
      border-bottom: 1rem / 20 solid #63d4f2;
      &:nth-child(1) {
        .rank {
          color: #fff;
          height: 48rem / 20;
          background: url(../../assets/champion-icon.png) no-repeat center;
        }
      }
      &:nth-child(2) {
        .rank {
          color: #fff;
          height: 48rem / 20;
          background: url(../../assets/runner-up-icon.png) no-repeat center;
        }
      }
      &:nth-child(3) {
        .rank {
          color: #fff;
          height: 48rem / 20;
          background: url(../../assets/third-icon.png) no-repeat center;
        }
      }
      > span {
        width: 33.33%;
        font-size: 24rem / 20;
        display: inline-block;
        >.user-head {
          width: 48rem / 20;
          height: 48rem / 20;
          border-radius: 999rem;
          vertical-align: middle;
        }
        >.user-name {
          color: #52251a;
          font-size: 28rem / 20;
          vertical-align: middle;
        }
      }
    }
  }
}
</style>