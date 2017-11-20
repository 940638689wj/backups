<template>
  <div class="my-simple-page">
    <button class="my-simple-page-prev" @click="Prev" :class="{ disabled: currentPage == 1 }">
      <i class="fa fa-caret-left"></i>
    </button>
    <span class="my-simple-page-info">{{ currentPage }} / {{ lastPage }}</span>
    <button class="my-simple-page-next" @click="Next" :class="{ disabled: currentPage == lastPage }">
      <i class="fa fa-caret-right"></i>
    </button>
    <input type="text" :value="currentPage" @input="Input($event)">
    <button class="my-simple-page-skip" @click="PageTo">跳转</button>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        targetPage: undefined
      }
    },
    props: {
      currentPage: {
        type: Number,
        default: 1
      },
      pageSize: {
        type: Number,
        default: 10
      },
      total: {
        type: Number,
        default: 0
      }
    },
    computed: {
      lastPage () {
        if (this.currentPage !== 1 && this.currentPage > this.total / this.pageSize) {
          // 如果当前页大于总页数
          this.$emit('pageTo', Math.ceil(this.total / this.pageSize))
        }
        return Math.ceil(this.total / this.pageSize)
      }
    },
    methods: {
      /**
       * 输入框赋值
       * @param {Object} E Event 对象
       */
      Input (E) {
        let number = Number(E.target.value)
        if (isNaN(number)) {
          E.target.value = this.currentPage
        }
        else if (number < 1) {
          E.target.value = 1
          this.targetPage = 1
        }
        else if (number > this.lastPage) {
          E.target.value = this.lastPage
          this.targetPage = this.lastPage
        }
        else {
          this.targetPage = number
        }
      },
      /**
       * 跳转
       */
      PageTo () {
        this.$emit('pageTo', this.targetPage)
      },
      /**
       * 上一页
       */
      Prev () {
        if (this.currentPage - 1 >= 1) {
          this.targetPage = this.currentPage - 1
          this.PageTo()
        }
      },
      /**
       * 下一页
       */
      Next () {
        if (this.currentPage + 1 <= this.lastPage) {
          this.targetPage = this.currentPage + 1
          this.PageTo()
        }
      }
    }
  }
</script>

<style lang="less">
  @height: 32px;
  @bgColor: #ffffff;
  @bgColorHover: #e4e8f1;

  .my-simple-page {
    font-size: 14px;

    button:focus {
      outline: none;
    }

    .btn() {
      height: @height;
      border: 0;
      cursor: pointer;
      background-color: @bgColor;
      border: 1px solid #cccccc;
      border-radius: 2px;

      &:hover {
        background-color: @bgColorHover;
      }
    }

    &-prev, &-next {
      .btn();
      display: inline-block;
      width: @height;

      > i {
        font-size: 12px;
        color: #CCCCCC;
      }

      &.disabled {
        cursor: not-allowed;
      }
    }

    &-info {
      color: #333;
      display: inline-block;
      height: @height;
      line-height: @height;
      margin: 0 .3em;
    }

    > input {
      color: #333;
      width: @height * 2;
      height: @height - 8px;
      text-align: center;
      padding: 3px;
      border: 1px solid #cccccc;
      border-radius: 2px;
      margin: 0 (@height / 3);
      background-color: @bgColor;

      &:focus {
        outline: none;
      }
    }

    &-skip {
      .btn();
      color: #333;
      width: @height * 2;
    }
  }
</style>