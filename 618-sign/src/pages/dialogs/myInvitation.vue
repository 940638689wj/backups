<template>
  <div class="dialogs-my-invitation">
    <dialogs :title="title" v-model="visible">
    <ul class="invitation-user-list">
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </li>
      <li>
        <img src="../../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
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
        title: '邀约列表'
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
.invitation-user-list {
  padding: 0;
  list-style: none;
  line-height: 68rem / 20;
  text-align: left;
  font-size: 0;
  // background-color: blue;
  li {
    // background-color: yellow;
    width: 33.33%;
    overflow: hidden;
    height: 68rem / 20;
    display: inline-block;
    border-bottom: 1rem / 20 solid #63d4f2;
    padding: 0;
    margin: 0;
    .user-head {
      vertical-align: middle;
      width: 48rem / 20;
      height: 48rem / 20;
      border-radius: 999rem;
    }
    .user-name {
      vertical-align: middle;
      color: #52251a;
      font-size: 28rem / 20;
    }
  }
}
</style>