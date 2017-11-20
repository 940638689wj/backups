import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export default new Vuex.Store(
  {
    state: {
      nginxMenuIndex: '1'
    },
    mutations: {
      setNginxMenuIndex (state, msg) {
        state.nginxMenuIndex = msg
      }
    }
  }
)
