import Vue          from 'vue'
import Vuex         from 'vuex'
import plugins      from './plugins/plugins'
import global       from './modules/global'
import user         from './modules/user'
import region       from './modules/region'
import userInfo     from './modules/userInfo'
import goodsInfo    from './modules/goodsInfo'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    global,
    user,
    region,
    userInfo,
    goodsInfo
  },
  plugins,
  strict: debug
})

// computed: {
//   /**
//    * 映射 Getter
//    */
//   ...mapGetters('namespace', [
//     '_user'
//   ])
// }

// methods: {
//   /**
//    * 分发 Action
//    */
//   ...mapActions('namespace', [
//     '_LogoutUser'
//   ])
// }
