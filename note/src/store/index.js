import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store(
  {
    state: {
      list: [],
      index: -1
    },
    mutations: {
      addList (state, val) {
        state.list.push(val)
      },
      setIndex (state, val) {
        state.index = val
      },
      del (state) {
        state.list.splice(state.index, 1)
      },
      changeList (state, val) {
        // state.list[state.index] = val
        Vue.set(state.list, state.index, val)
      }
    }
  }
)
