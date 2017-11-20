<template>
  <div class="app-default-template">
    <div v-show="!($route.path === '/')" class="go-back" @click="GoBack">
      <i class="fa fa-angle-left"></i>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  export default {
    data () {
      return {
      }
    },
    created () {
    },
    computed: {
      /**
       * 映射 Getter
       */
      ...mapGetters('global', [
        '_goBackRouter'
      ])
    },
    methods: {
      /**
       * 分发 Action
       */
      ...mapActions('global', [
        '_ClearGoBackRouter'
      ]),
      /**
       * 返回上一级
       */
      GoBack () {
        if (this._goBackRouter === '') {
          window.history.back()
        }
        else {
          let goBackRouter = this._goBackRouter
          this._ClearGoBackRouter()
          this.$router.push(goBackRouter)
        }
      }
    }
  }
</script>

<style lang="less">
  @import '~global/variable.less';
  .app-default-template {
    .go-back {
      position: absolute;
      text-align: center;
      width: 100rem / 20;
      line-height: 100rem / 20;
      font-size: 40rem / 20;
    }
  }
</style>

