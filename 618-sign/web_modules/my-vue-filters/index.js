/**
 * 整合开源组件
 */
import * as stringFilters from './string/index'

export default {
  install: function (Vue) {
    for (let key in stringFilters) {
      Vue.filter(key, stringFilters[key])
    }
  }
}
