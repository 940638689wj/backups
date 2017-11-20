import $$ from '../plugins/storage'

$$.setNamespace('region')

// initial state
const state = {
  list: $$.get('list') || [],
  regionList: $$.get('regionList') || {},
  provinceList: $$.get('provinceList') || {},
  cityList: $$.get('cityList') || {},
  districtList: $$.get('districtList') || {}
}

// mutations
const mutations = {
  list (state, value) {
    state.list = value
  },
  regionList (state, value) {
    state.regionList = value
  },
  provinceList (state, value) {
    state.provinceList = value
  },
  cityList (state, value) {
    state.cityList = value
  },
  districtList (state, value) {
    state.districtList = value
  }
}

// getters
const getters = {
  _region: state => state.list,               // 地区信息源数据
  _regionList: state => state.regionList,     // 以id为键存储地区信息
  _provinceList: state => state.provinceList, // 省份信息
  _cityList: state => state.cityList,         // 城市信息
  _districtList: state => state.districtList  // 区县信息
}

// actions
const actions = {
  /**
   * 设置地区源数据
   */
  _SetRegion ({ commit, state }, list) {
    commit('list', list)
  },
  /**
   * 将地区数据以地区id为键保存
   */
  _SetRegionList ({ commit, state }, regionList) {
    commit('regionList', regionList)
  },
  /**
   * 设置省份列表
   */
  _SetProvinceList ({ commit, state }, provinceList) {
    commit('provinceList', provinceList)
  },
  /**
   * 设置城市列表
   */
  _SetCityList ({ commit, state }, cityList) {
    commit('cityList', cityList)
  },
  /**
   * 设置市区列表
   */
  _SetDistrictList ({ commit, state }, districtList) {
    commit('districtList', districtList)
  }
}

export default { namespaced: true, state, mutations, getters, actions }
