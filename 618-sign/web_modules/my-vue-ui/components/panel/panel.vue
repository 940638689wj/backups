<template>
  <transition>
    <div v-if="value" class="my-panel" @keyup.esc="Input(false)">
      <!-- <div class="modal"></div> -->
      <div class="panel-main" @click.self="Input(false)">
        <div class="panel-container">
          <div class="box">
            <div class="header">{{ title }}</div>
            <div class="content"><slot></slot></div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>


<script>
  export default {
    props: {
      value: Boolean,
      title: String
    },
    mounted () {
      document.body.appendChild(this.$el)
    },
    methods: {
      /**
       * v-model
       */
      Input (value) {
        this.$emit('input', value)
      }
    }
  }
</script>


<style lang="less" scoped>
  .my-panel {

    &.v {
      &-enter-active,
      &-leave-active {
        transition: all .3s;
      }
      &-enter {
        .box {
          left: 100% !important;
        }
      }
      &-leave {
        .box {
          left: 0 !important;
        }
      }
      &-enter-active {
        .box {
          transition: all .3s;
        }
      }
      &-leave-active {
        .box {
          left: 100% !important;
          transition: all .3s;
        }
      }
    }

    .panel-main {
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      
      .panel-container {
        position: absolute;
        right: 0;
        height: 100%;
        overflow-x: hidden;
        overflow-y: auto;

        .box {
          position: relative;
          background-color: #fff;
          left: 0;
          margin-left: 10px;
          box-shadow: 0 0 10px #ccc;
          min-height: 100%;
          overflow: hidden;

          .header {
            background-color: #eef1f6;
            height: 36px;
            line-height: 36px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            border-bottom: solid 1px #ddd;
          }

          .content {
            padding: 0 2em 2em 2em;
          }
        }
      }
    }

    // .modal {
    //   position: fixed;
    //   left: 0;
    //   top: 0;
    //   width: 100%;
    //   height: 100%;
    //   opacity: .5;
    //   background: #fff;
    // }
  }
</style>