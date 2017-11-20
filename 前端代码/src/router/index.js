import Vue from 'vue'
import Router from 'vue-router'

import CodeTemplateIndex from '@/components/code_template/Index'
import UpdateServerIndex from '@/components/update_server/Index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'CodeTemplateIndex',
      component: CodeTemplateIndex
    },
    {
      path: '/update_server',
      name: 'UpdateServerIndex',
      component: UpdateServerIndex
    }
  ]
})
