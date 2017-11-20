<template>
  <transition name="modal" v-if="visible">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="dialogs-login">  
            <div class="close-dialog" @click=""></div>
            <div class="dialogs-login-content">
              <slot></slot>
              <div class="mobile">
                <span>手机号</span>
                <input type="number" v-model="mobileNumber" pattern="[0-9]*">
              </div>
              <div class="check-code">
                <span>验证码</span>
                <input type="number" v-model="checkCode" pattern="[0-9]*">
                <button v-model="checkCode" @click=SendCode($event) class="send-code">{{ send }}</button>
              </div>
              <div class="errorMsg">{{ errorMsg }}</div>
            </div>
            <div class="dialogs-login-button">
              <button @click="Login($event)">
                {{ login }}
              </button>
            </div>

          </div>

        </div>
      </div>
    </div>
  </transition>
</template>
<script>
import Cryptojs from 'crypto-js'
export default {
  props: {
    login: {default: '登录', type: String},
    value: {default: false, type: Boolean}
  },
  data () {
    return {
      visible: false,
      mobileNumber: '',
      checkCode: '',
      errorMsg: '',
      send: '发送'
    }
  },
  watch: {
    value: function (val) {
      this.visible = val
      this.mobileNumber = ''
      this.checkCode = ''
      this.errorMsg = ''
    },
    visible: function (val) {
      this.$emit('input', val)
    }
  },
  methods: {
    Over () {
      console.log(123)
    },
    /**
     * 关闭对话框
     */
    Close () {
      this.visible = false
    },
    SendCode (e) {
      let _this = this
      setTimeout(function () {
        _this.errorMsg = ''
      }, 2000)
      if (!this.mobileNumber) {
        this.errorMsg = '请输入手机号'
        return
      }
      if (!(/^1(3|4|5|7|8)\d{9}$/.test(this.mobileNumber))) {
        this.errorMsg = '请输入正确的手机号'
        return
      }
      let senMsgKey = Cryptojs.MD5(this.mobileNumber + 'i2!d$2*3^0@#4').toString()
      this.$http.post('common/sendVerily', {mobile: Number(this.mobileNumber), test: 1, key: senMsgKey}).then(response => {
        if (response.data.code === 1) {
          this.errorMsg = ''
          this.Interval(e, '已发送', 60)
        }
      }, error => {
        if (error.data.code === 0) {
          this.errorMsg = error.data.msg
        }
      })
    },
    /**
     * 确认
     */
    Login (e) {
      if (!this.mobileNumber || !this.checkCode) {
        this.Interval(e, '请输入手机号和验证码', 3)
        return
      }
      this.$http.post('common/checkVerily', {mobile: Number(this.mobileNumber), sms: this.checkCode}).then(response => {
        if (response.data.code === 1) {
          // 验证成功
          this.Close()
          this.$emit('loginSuccess')
        }
      }, error => {
        if (error.data.code === 0) {
          this.Interval(e, '验证码错误', 3)
          return
        }
      })
    },
    /**
     * 定时器
     * @param {[type]} e    [事件对象]
     * @param {[type]} msg  [提示消息]
     * @param {[type]} time [时间 / 秒]
     */
    Interval (e, msg, time) {
      let _this = e.target
      if (_this.getAttribute('disable')) { // 防止多次点击
        return
      }
      let text = _this.innerText // 原文本内容
      let color = _this.style.color
      let TimerId
      _this.setAttribute('disable', true)
      _this.style.color = '#969696'
      _this.style.borderColor = '#969696'
      _this.innerText = msg + '(' + time + ')'
      TimerId = setInterval(function () {
        time--
        if (time === 0) {
          _this.removeAttribute('disable')
          _this.style.color = color
          _this.innerText = text
          clearTimeout(TimerId)
          return
        }
        _this.innerText = msg + '(' + time + ')'
      }, 1000)
    }
  }
}
</script>

<style lang="less">
.dialogs-login {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translateY(-50%);
  overflow: hidden;
  width: 540rem / 20;
  background-color: #fff;
  margin-left: -250rem / 20;
  border-radius: 12rem / 20;
  box-shadow: 0 1rem / 20 3rem / 20 rgba(0,0,0,.3);
  // width: 500rem / 20;
  
  .close-dialog {
    float: right; 
    width: 30rem / 20;
    margin-top: 5rem / 20;
  }
  
  .dialogs-login-content {
    padding: 40rem / 20 20rem /20;
    font-size: 28rem / 20;
    span {
      color: #777777;
    }
    span:nth-child(1) {
      padding-right: 20rem / 20;
    }
    input {
      width: 380rem / 20;;
      line-height: 60rem / 20;
      font-size: 30rem / 20;
      padding-left: 10rem / 20;
      border: 0;
      background: #EEEEEE;
      box-sizing: border-box;
      -webkit-appearance: none;
      -moz-appearance: none;
      -o-appearance: none;
      appearance: none;
      outline:none;
    }
    .check-code {
      margin-top: 20rem / 20;
      width: 520rem / 20;
      input {
        width: 210rem / 20;
        margin-right: 12rem / 20; 
      }
      .send-code {
        width: 150rem / 20;
        font-size: 28rem / 20;
        text-align: center;
        display: inline-block;
        line-height: 59rem / 20;
        height: 61rem / 20;
        border: 1rem / 20 solid #198CFF;
        background: #ffffff;
        color: #198CFF;
        border-radius: 2rem / 20;
        margin-top: -1rem / 20;
      }
    }
    .errorMsg {
      position: absolute;
      margin-top: 1rem / 20;
      color: red;
    }
  }
  .dialogs-login-button {
    font-size: 0;
    overflow: hidden;
    text-align: center;
    border-top: 1rem / 20 solid #dddddd;
    button {
      border: 0;
      color: #0080ff;
      height: 80rem / 20;
      font-size: 34rem / 20;
      background-color: #fff;
      word-break:keep-all;           /* 不换行 */
      white-space:nowrap;          /* 不换行 */
      &:active, &:focus {
        outline: none;
      }
    }
  }
}
</style>