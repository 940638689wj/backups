<template>
  <div class="input-number" :class="{ disabled }">
    <span class="decrease" @click="Decrease" @mousedown.prevent :class="{ disabled: value == min }">
      <i class="iconfont icon-minus"></i>
    </span>
    <input type="text" :value.number="value" @input="ForceNumber($event),Input($event.target.value)" :disabled="disabled">
    <span class="increase" @click="Increase" @mousedown.prevent :class="{ disabled: value == max }">
      <i class="iconfont icon-plus"></i>
    </span>
  </div>
</template>

<script>
  export default {
    props: {
      step: {
        type: Number,
        default: 1
      },
      max: {
        type: Number,
        default: Infinity
      },
      min: {
        type: Number,
        default: 0
      },
      value: {
        default: 0
      },
      disabled: Boolean,
      size: String,
      controls: {
        type: Boolean,
        default: true
      }
    },
    methods: {
      /**
       * 强制输入格式
       * @param {object} E Event 对象
       */
      ForceNumber (E) {
        let number = Number(E.target.value)
        if (isNaN(number)) {
          E.target.value = this.value
        }
        if (number < this.min) {
          E.target.value = this.min
        }
        if (number > this.max) {
          E.target.value = this.max
        }
      },
      /**
       * 输入框赋值
       * @param {integer} value 目标页码
       */
      Input (value) {
        this.$emit('input', value)
        this.$emit('change', value)
      },
      /**
       * 递增
       */
      Increase () {
        if (this.disabled) {
          return
        }
        const value = this.value || 0
        if (value + this.step >= this.max) {
          this.Input(this.max)
        }
        else {
          this.Input(value + this.step)
        }
      },
      /**
       * 递减
       */
      Decrease () {
        if (this.disabled) {
          return
        }
        const value = this.value || 0
        if (value - this.step <= this.min) {
          this.Input(this.min)
        }
        else {
          this.Input(value - this.step)
        }
      }
    }
  }
</script>

<style lang="less" scoped>
  @height: 54rem / 20;
  @color: #999;
  @colorDisabled: #ccc;

  .btn() {
    display: inline-block;
    width: @height;
    height: @height;
    line-height: @height;
    text-align: center;
    cursor: pointer;

    > i {
      font-size: 14rem / 20;
    }

    &:hover {
      background-color: #e3ebf7;
    }
  }

  .input-number {
    display: inline-block;
    height: @height;
    border: solid 1rem / 20 @color;
    background-color: #fff;

    &.disabled {
      background-color: #e5e9f2;
      color: @colorDisabled;
      border-color: @colorDisabled;
      
      span {
        border-color: @colorDisabled;
        cursor: not-allowed;
      }

      input {
        color: @color;
      }
    }

    input {
      width: @height;
      border: 0;
      font-size: 28rem / 20;
      text-align: center;
      background-color: transparent;

      &:focus {
        outline: none;
      }

    }

    .decrease {
      .btn();
      border-right: solid 1rem / 20 @color;

      &.disabled {
        cursor: not-allowed;
        border-color: @colorDisabled;
      }
    }

    .increase {
      .btn();
      border-left: solid 1rem / 20 @color;

      &.disabled {
        cursor: not-allowed;
        border-color: @colorDisabled;
      }
    }
  }
</style>