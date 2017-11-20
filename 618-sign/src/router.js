import VueRouter                  from 'vue-router'
import index                      from './pages/index.vue'
// import order                      from './pages/order.vue'
// import user                       from './pages/user.vue'
// import confirmOrder               from './pages/confirmOrder.vue'
// import paySuccess                 from './pages/paySuccess.vue'
// import myOrder                    from './pages/myOrder.vue'
// import orderDetail                from './pages/orderDetail.vue'

const routes = [
  { path: '/index', component: index, meta: { t: 0 } },
  { path: '/', component: index, meta: { t: 0 } },
  /**
   * 用户中心
   */
  { path: '/user', component: resolve => require(['./pages/user.vue'], resolve), meta: { t: 0 } },
  /**
   * 登陆、注册、重置密码
   */
  { path: '/order/:orderId?', component: resolve => require(['./pages/order.vue'], resolve), meta: { t: 0 } },
  /**
   * 确认订单
   */
  { path: '/confirmOrder', component: resolve => require(['./pages/confirmOrder.vue'], resolve), meta: { t: 0 } },
  /**
   * 支付成功
   */
  { path: '/paySuccess/:orderId/', component: resolve => require(['./pages/paySuccess.vue'], resolve), meta: { t: 0 } },
  /**
   * 我的订单
   */
  { path: '/myOrder', component: resolve => require(['./pages/myOrder.vue'], resolve), meta: { t: 0 } },
  /**
   * 订单详情
   */
  { path: '/orderDetail', component: resolve => require(['./pages/orderDetail.vue'], resolve), meta: { t: 0 } }
]

const router = new VueRouter({
  routes,
  linkActiveClass: 'active'
})

export default router
