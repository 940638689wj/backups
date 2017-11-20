<template>
  <transition name="modal" v-if="visible">
    <div class="modal-mask" @click="Click(123)">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="dialogs-address" @click.stop="">
            <div class="add-address-title">添加收货地址</div>

            <div class="dialogs-address-content">
              <div class="mobile">
                <span>姓名</span>
                <input v-model="formData.user">
              </div>
              <div class="check-code">
                <span>手机</span>
                <input type="number" v-model="formData.mobile"  pattern="[0-9]*">
              </div>
            </div>

            <div class="dialogs-address-content">
              <div class="address-title">
                <span>详细地址</span>
                <span>福建省</span>
                <span>福州市</span>

                <!-- <select>
                  <option value ="福建省">福建省</option>
                  <option value ="saab">Saab</option>
                  <option value="opel">Opel</option>
                  <option value="audi">Audi</option>
                </select> -->
              </div>
              <textarea v-model="formData.addr" rows="2" cols="2" placeholder="请填写详细地址">
              </textarea>
            </div>

            <div class="errorMsg">{{ errorMsg }}</div>

            <div class="dialogs-address-button">
              <button @click="Save()">
                保存
              </button>
            </div>

          </div>

        </div>
      </div>
    </div>
  </transition>
</template>
<script>
export default {
  props: {
    value: {default: false, type: Boolean},
    addressInfo: Object
  },
  data () {
    return {
      visible: false,
      formData: {
        // user: '小明',
        // mobile: '15654654654',
        // addr: '科技大厦'
      },
      qu: '福建省',
      errorMsg: ''
    }
  },
  watch: {
    value: function (val) {
      this.visible = val
      this.errorMsg = ''
      this.formData = this.addressInfo
    },
    visible: function (val) {
      this.$emit('input', val)
    }
  },
  methods: {
    /**
     * 关闭对话框
     */
    Close () {
      this.visible = false
    },
    Click (vo) {
      console.log(vo)
    },
    /**
     * 保存地址
     */
    Save () {
      if (!this.formData.user || !this.formData.mobile || !this.formData.addr) {
        this.errorMsg = '请填写信息'
        return
      }
      else if (!(/^1(3|4|5|7|8)\d{9}$/.test(this.formData.mobile))) {
        this.errorMsg = '手机号码不正确'
        return
      }
      this.Close()
      this.$emit('addAddress', this.formData)
    }
  }
}
</script>

<style lang="less">
.dialogs-address {
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

  .add-address-title {
    line-height: 68rem / 20;
    text-align: center;
    font-size: 30rem / 20;
    color: #333333;
    border-bottom: 1rem / 20 solid #dddddd;
  }
  .dialogs-address-content {
    padding: 20rem / 20 20rem /20;
    font-size: 28rem / 20;
    border-bottom: 1rem / 20 solid #dddddd;
    span {
      color: #777777;
    }
    span:nth-child(1) {
      padding-right: 20rem / 20;
    }
    input {
      width: 380rem / 20;
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
    textarea {
      width: 100%;
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
    .address-title {
      select {
        font-size: 30rem / 20;
        width: 110rem / 20;
        height: 40rem / 20;
        float: right;
      }
      span:nth-child(2) {
        margin: 0 66rem / 20;
      }
      span:nth-child(3) {
        float: right;
      }
    }
    .check-code {
      margin-top: 20rem / 20;
      input {
        margin-right: 12rem / 20; 
      }
    }
  }
  .errorMsg {
    position: absolute;
    margin-left: 20rem / 20;
    color: red;
  }
  .dialogs-address-button {
    font-size: 0;
    overflow: hidden;
    text-align: center;
    button {
      border: 0;
      width: 50%;
      color: #0080ff;
      height: 80rem / 20;
      font-size: 34rem / 20;
      background-color: #fff;
      &:active, &:focus {
        outline: none;
      }
    }
  }
}
</style>