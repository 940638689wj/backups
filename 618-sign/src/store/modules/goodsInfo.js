import $$ from '../plugins/storage'

$$.setNamespace('goodsInfo')

// initial state
const state = {
  goodsInfo: $$.get('goodsInfo') || {}
}

// mutations
const mutations = {
  goodsInfo (state, value) {
    state.goodsInfo = value
  }
}

// getters
const getters = {
  _goodsInfo: state => {
    if (!state.goodsInfo.id) {
      // 如果没有用户信息,跳回登陆
      window.location.href = '/'
      return
    }
    return state.goodsInfo
  }
}

// actions
const actions = {
  /**
   * 查看用户信息
   * @param {object} goodsInfo 用户信息对象
   */
  _AddgoodsInfo ({ commit, state }, goodsInfo) {
    commit('goodsInfo', goodsInfo)
  }
}

export default { namespaced: true, state, mutations, getters, actions }
