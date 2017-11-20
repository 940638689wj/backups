import Vue           from 'vue'
import VueRouter     from 'vue-router'
import VueResource   from 'vue-resource'
import VueX          from 'vuex'
// import ElementUI     from 'element-ui'
import router        from './router.js'
import App           from './base/app.vue'
import store         from './store'
import MyVueFilters  from 'my-vue-filters'
import MyVueAlertify from 'my-vue-alertify'
import MyVueUi       from 'my-vue-ui'
import AppDialogs    from 'app-dialogs'
// import 'RongIMLib'
Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(VueX)
// Vue.use(ElementUI)
Vue.use(MyVueFilters)
Vue.use(MyVueAlertify)
Vue.use(MyVueUi)
Vue.use(AppDialogs)

/**
 * 环境变量
 */
const env = process.env.NODE_ENV
const isProduction = env === 'production'

/**
 * 项目全局配置
 */
// api 访问前缀
// window.apiUrlPrefix = isProduction ? 'http://10.1.1.10/market/webmanage' : '/api' // 正式
// window.apiUrlPrefix = isProduction ? 'http://192.168.2.207:8080' : '/test' //
// window.apiUrlPrefix = isProduction ? 'http://test2.fjmxj.cn/activity/' : '/test' //
window.apiUrlPrefix = isProduction ? 'http://www.lanhaitianwang.com/weiphp/JSSDK_LIB/SERVER/' : '/api' // api 地址为 10.1.1.10:8066
// window.apiUrlPrefix = isProduction ? 'http://192.168.2.207:8066/' : '/local' // api 地址为 10.1.1.10:8066
/**
 * 资源通讯
 */
Vue.http.options.emulateJSON = true // 服务器无法正确处理 POST 传参时开启 FormData 模拟
Vue.http.options.root = window.apiUrlPrefix
Vue.http.interceptors.push((request, next) => {
  // 全局请求处理
  // 附带授权头
  // request.headers.map.Authorization = ['Bearer ' + window.localStorage.getItem(window.appPrefix + 'token')]
  // let JSESSIONID = window.localStorage.getItem('JSESSIONID')
  // if (request.body === null || request.body === undefined) {
  //   request.body = {unknown: 'unknown'}
  // }
  // request.params.JSESSIONID = JSESSIONID
  // 全局响应回调
  next(function (response) {
    // HTTP 特殊状态码过滤
    switch (response.status) {
      case 401:
        this.$error('登录超时，请重新登录')
        this.$router.push('/login')
        break
      // case 403:
      //   this.$error('权限不足')
      //   break
      case 404:
        this.$error('接口未找到')
        break
      case 405:
        this.$error('接口处理异常')
        break
      // case 429:
      //   this.$error('Too Many Requests')
      //   break
      case 500:
        this.$error('操作失败')
        break
      default:
        // 服务端没有推送 json 类型头，前端强制转换
        if (typeof response.data === 'string') {
          response.data = JSON.parse(response.data)
        }
        // code 错误码
        if (response.data.code === 302) {
          this.$error('您没有权限访问该页面,请重新登录')
          this.$router.push('/login')
        }
        response.ok = response.data.code === 1
        break
    }
  })
})

/**
 * 初始化
 */
/* eslint-disable no-new */
new Vue({
  store,
  router,
  el: '#app',
  render: h => h(App)
})
