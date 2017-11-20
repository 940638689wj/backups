<template>
  <div class="my-filter-tabs" v-minHeight="minHeight">
    <div class="label">{{ title }}</div>
    <div class="list" :style="listStyle">
      <span v-if="allData" @click="Toggle(allData)" style="font-weight: bold;" :class="{active: active.id == allData.id}">全部</span>
      <span v-for="vo in list" @click="Toggle(vo)" :class="{active: active.id == vo.id}">{{ vo.name }}</span>
    </div>
    <div class="more" @click="showAll = !showAll">
      <i v-if="showAll" class="el-icon-arrow-up"></i>
      <i v-else class="el-icon-arrow-down"></i>
    </div>
  </div>
</template>


<script>
  import E from 'oui-dom-events'

  export default {
    data () {
      return {
        showAll: false
      }
    },
    props: {
      minHeight: {
        type: Number,
        default: 141
      },
      title: String,
      list: Array,
      active: Object,
      allData: Object
    },
    directives: {
      minHeight: {
        inserted (el, binding, vnode) {
          let list = el.getElementsByClassName('list')[0]
          let more = el.getElementsByClassName('more')[0]
          const fn = event => {
            if (list.offsetHeight < binding.value) {
              more.hidden = true
              list.style.maxHeight = null
            }
            else {
              more.hidden = false
              list.style.maxHeight = binding.value + 'px'
            }
          }
          E.on(window, 'resize', fn)
          fn()
        }
      }
    },
    computed: {
      listStyle () {
        if (this.showAll) {
          return {}
        }
        else {
          return {
            maxHeight: this.minHeight + 'px'
          }
        }
      }
    },
    methods: {
      Toggle (vo) {
        this.$emit('toggle', vo)
      }
    }
  }
</script>


<style lang="less">
  @import '~global/variable.less';
  @cardLabelLeft: 20px;

  .my-filter-tabs {
      position: relative;
      border: solid 1px @borderColor;
      overflow: hidden;
      background-color: @bgColor;

      .label {
        float: left;
        color: #333;
        margin: 16px @cardLabelLeft;
      }

      .list {
        margin: 5px 0 5px 122px;
        overflow: hidden;
        color: #4D79BD;

        span {
          display: inline-block;
          float: left;
          margin: 11px 0;
          width: 115px;
          height: 21px;
          cursor: pointer;

          &:hover, &.active {
            color: @moneyColor;
          }
        }
      }

      .more {
        position: absolute;
        bottom: 0;
        width: 100%;
        color: #999;
        text-align: center;
        cursor: pointer;
        font-size: 12px;
        
        &:hover {
          background-color: #eee;
        }
      }
    }
</style>