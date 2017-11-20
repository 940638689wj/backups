<template>
  <div class="user-center">
    <div class="banner">
      <img src="../assets/user-banner.png" alt="">
      <div class="user-info">
        <img src="../assets//test/1.jpg" alt="" class="user-head">
        <span class="user-name"> 月亮弯弯</span>
      </div>
    </div>
    <div class="warning">
      已上传活鱼图片0天，还有15天可获得奖品
    </div>
    
    <div class="photo-list">
      <button class="set-addr-button">设置上传地址>></button>
      <h3 class="photo-list-date">12月6日</h3>
      <ul class="photo-list-item">
        <li>
          <img src="../assets/user-banner.png" alt="">
        </li>
        <li>
          <img src="../assets/user-banner.png" alt="">
        </li>
        <li>
          <img src="../assets/user-banner.png" alt="">
        </li>
        <li>
          <img src="../assets/user-banner.png" alt="">
        </li>
        <li>
          <img src="../assets/user-banner.png" alt="">
        </li>
      </ul>
      <h3 class="photo-list-date">12月6日</h3>
      <ul class="photo-list-item">
        <li>
          <img src="../assets/user-banner.png" alt="">
        </li>
        <li>
          <img src="../assets/user-banner.png" alt="">
        </li>
        <li>
          <img src="../assets/user-banner.png" alt="">
        </li>
      </ul>
    </div>
  </div>
</template>


<script>
  export default {
  }
</script>


<style lang="less">
.user-center {
  text-align: center;
  > .banner {
    position: relative;
    width: 100%;
    img {
      width: 100%;
    }
    > .user-info {
      font-size: 0;
      text-align: left;
      left: 36rem / 20;
      bottom: 60rem / 20;
      position: absolute;
      height: 159rem / 20;
      vertical-align: middle;
      >.user-head {
        display: inline-block;
        height: 159rem / 20;
        width: 159rem / 20;
        border-radius: 999rem;
      }
      >.user-name {
        float: right;
        color: #f5f5f5;
        font-size: 32rem / 20;
        padding-left: 30rem / 20;
        line-height: 159rem / 20;
      }
    }
  }
  .warning {
    width: 100%;
    color: #f0622a;
    height: 70rem / 20;
    text-align: center;
    font-size: 24rem / 20;
    margin-top: 10rem / 20; 
    line-height: 70rem / 20;
    background-color: #feda32;
  }
  .set-addr-button {
    border: 0;
    float: right;
    color: #177ee6;
    font-size: 28rem / 20;
    margin-right: 30rem / 20;
    background-color: transparent;
    &:active, &:focus {
      outline: none;
    }
  }
  .photo-list {
    font-size: 0;
    .photo-list-date {
      text-align: left;
      font-weight: 500;
      font-size: 30rem / 20;
      width: 690rem / 20;
      margin: 26rem / 20 auto;
    }
    .photo-list-item {
      padding: 0;
      margin: 0 auto;
      overflow: hidden;
      width: 690rem / 20;
      > li {
        float: left;
        overflow: hidden;
        text-align: center;
        position: relative;
        width: 218rem / 20;
        height: 218rem / 20;
        display: inline-block;
        margin-top: 18rem / 20;
        background: url(../assets/transparent.png);
        img {
          left: 0;
          top: 50%;
          width: 100%;
          position: absolute;
          transform: translateY(-50%);
        }
        &:nth-child(3n + 2) {
          margin: 0 18rem / 20;
          margin-top: 18rem / 20;
        }
      }
    }
  }
}
</style>