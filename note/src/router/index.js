import Vue from 'vue'
import Router from 'vue-router'
// import Hello from '@/components/Hello'
// import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      // component: Hello
      component: resolve => require(['@/components/Hello'], resolve)
    },
    {
      path: '/hello',
      name: 'Hello',
      component: resolve => require(['@/components/Hello'], resolve)
    },
    {
      path: '/login',
      name: 'Login',
      component: resolve => require(['@/components/Login'], resolve)
    }
  ]
})
