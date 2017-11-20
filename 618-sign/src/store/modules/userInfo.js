import $$ from '../plugins/storage'

$$.setNamespace('userInfo')

// initial state
const state = {
  userInfo: $$.get('userInfo') || {}
}

// mutations
const mutations = {
  userInfo (state, value) {
    state.userInfo = value
  }
}

// getters
const getters = {
  _userInfo: state => state.userInfo      // 用户信息
}

// actions
const actions = {
  /**
   * 查看用户信息
   * @param {object} userInfo 用户信息对象
   */
  _AddUserInfo ({ commit, state }, userInfo) {
    commit('userInfo', userInfo)
  }
}

export default { namespaced: true, state, mutations, getters, actions }
