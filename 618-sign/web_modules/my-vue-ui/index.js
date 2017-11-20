import inputNumber   from './components/inputNumber/inputNumber.vue'
import simplePage    from './components/simplePage/simplePage.vue'
import dataTable     from './components/dataTable/dataTable.vue'
import scene         from './components/scene/scene.vue'
import providerTable from './components/providerTable/providerTable.vue'
import datePicker    from './components/datePicker/datePicker.vue'
import filterTabs    from './components/filterTabs/filterTabs.vue'
import zoomImg       from './components/zoomImg/zoomImg.vue'
import panel         from './components/panel/panel.vue'
import echartsLine   from './components/echarts/lineChart.vue'
import pageTitle   from './components/pageTitle/pageTitle.vue'

export default {
  install: function (Vue) {
    Vue.component('my-input-number', inputNumber)
    Vue.component('my-simple-page', simplePage)
    Vue.component('my-data-table', dataTable)
    Vue.component('my-scene', scene)
    Vue.component('my-provider-table', providerTable)
    Vue.component('my-date-picker', datePicker)
    Vue.component('my-filter-tabs', filterTabs)
    Vue.component('my-zoom-img', zoomImg)
    Vue.component('my-panel', panel)
    Vue.component('my-echartsLine', echartsLine)
    Vue.component('my-pageTitle', pageTitle)
  }
}
