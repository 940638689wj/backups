import $$ from '../plugins/storage'

$$.setNamespace('user')

// initial state
const state = {
  info: $$.get('info') || {},
  isLogin: $$.get('isLogin') || false
}

// mutations
const mutations = {
  info (state, value) {
    state.info = value
  },
  isLogin (state, value) {
    state.isLogin = value
  }
}

// getters
const getters = {
  _user: state => {
    if (!state.info.secTree) {
      // 如果没有用户信息,跳回登陆
      window.location.href = '/'
      return
    }
    return state.info
  },      // 用户信息
  _isLogin: state => state.isLogin // 用户是否登陆
}

// actions
const actions = {
  /**
   * 登录
   * @param {object} userInfo 用户信息对象
   */
  _Login ({ commit, state }, userInfo) {
    if (!state.isLogin) {
      commit('isLogin', true)
      commit('info', userInfo)
    }
    // window.localStorage.setItem('JSESSIONID', userInfo.JSESSIONID)
  },
  /**
   * 登出
   */
  _Logout ({ commit, state }) {
    if (state.isLogin) {
      commit('isLogin', false)
      commit('info', {})
    }
  }
}

export default { namespaced: true, state, mutations, getters, actions }
