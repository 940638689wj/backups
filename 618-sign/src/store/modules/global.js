import $$ from '../plugins/storage'

$$.setNamespace('global')

// initial state
const state = {
  activePurchScheme: $$.get('activePurchScheme') || {},
  activeOrderNumber: $$.get('activeOrderNumber'),
  tempOrdersMap: $$.get('tempOrdersMap') || [],
  stepOnePageSize: $$.get('stepOnePageSize') || 10,
  goBackRouter: $$.get('goBackRouter') || ''
}

// mutations
const mutations = {
  activePurchScheme (state, value) {
    state.activePurchScheme = value
  },
  activeOrderNumber (state, value) {
    state.activeOrderNumber = value
  },
  tempOrdersMap (state, value) {
    state.tempOrdersMap = value
  },
  stepOnePageSize (state, value) {
    state.stepOnePageSize = value
  },
  goBackRouter (state, value) {
    state.goBackRouter = value
  }
}

// getters
const getters = {
  _activePurchScheme: state => state.activePurchScheme, // 当前激活的采购单方案
  _activeOrderNumber: state => state.activeOrderNumber, // 当前激活的订单号
  _tempOrdersMap: state => state.tempOrdersMap,         // 采购单方案的匹配单索引
  _stepOnePageSize: state => state.stepOnePageSize,      // 采购第一步列表的每页显示条目
  _goBackRouter: state => state.goBackRouter      // 采购第一步列表的每页显示条目
}

// actions
const actions = {
  /**
   * 激活采购单方案
   */
  _ActivePurchScheme ({ commit, state }, purchScheme) {
    commit('activePurchScheme', purchScheme)
  },
  /**
   * 设置激活的匹配订单号
   */
  _SetActiveOrderNumber ({ commit, state }, orderNumber) {
    commit('activeOrderNumber', orderNumber)
  },
  /**
   * 缓存采购单方案对应的匹配单
   */
  _PushTempOrdersMap ({ commit, state }, tempOrderId) {
    let purchSchemeId = state.activePurchScheme.id
    let tempOrdersMap = state.tempOrdersMap
    tempOrdersMap[purchSchemeId] = tempOrderId
    commit('tempOrdersMap', tempOrdersMap)
  },
  /**
   * 清除指定采购单方案对应缓存的匹配单
   */
  _ClearTempOrderByPurchSchemeId ({ commit, state }, purchSchemeId) {
    let tempOrdersMap = state.tempOrdersMap
    delete tempOrdersMap[purchSchemeId]
    commit('tempOrdersMap', tempOrdersMap)
  },
  /**
   * 设置采购第一步列表的每页显示条目
   */
  _SetStepOnePageSize ({ commit, state }, pageSize) {
    commit('stepOnePageSize', Number(pageSize))
  },
  /**
   * 清除返回链接
   * @param  {[type]} options.commit [description]
   * @param  {[type]} options.state  [description]
   * @param  {[type]}                [description]
   * @return {[type]}                [description]
   */
  _ClearGoBackRouter ({ commit, state }) {
    commit('goBackRouter', '')
  },
  /**
   * 设置返回链接
   * @param  {[type]} options.commit [description]
   * @param  {[type]} options.state  [description]
   * @param  {[type]} link           [description]
   * @return {[type]}                [description]
   */
  _SetGoBackRouter ({ commit, state }, link) {
    commit('goBackRouter', link)
  }
}

export default { namespaced: true, state, mutations, getters, actions }
