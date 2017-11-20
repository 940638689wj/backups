export default {
  alert: undefined,
  confirm: undefined,
  install (Vue) {
    this.alert = Vue.prototype.$alert
    this.confirm = Vue.prototype.$confirm
    /**
     * 模态提示框
     */
    Vue.prototype.$alert = (title, message, option = {}, onOk) => {
      if (message === undefined) {
        message = title
        title = '系统提示'
      }
      else if (typeof message === 'string') {
        if (typeof option === 'function') {
          onOk = option
        }
      }
      else if (typeof message === 'object') {
        onOk = option
        option = message
        message = title
        title = '系统提示'
      }
      else if (typeof message === 'function') {
        onOk = message
        message = title
        title = '系统提示'
      }
      if (typeof onOk !== 'function') {
        onOk = () => {}
      }
      this.alert(message, title, option).then(onOk)
    }
    /**
     * 模态选择框
     */
    Vue.prototype.$confirm = (title, message, option = {}, onOk, onCancel) => {
      if (message === undefined) {
        message = title
        title = '系统提示'
      }
      else if (typeof message === 'string') {
        if (typeof option === 'function') {
          onCancel = onOk
          onOk = option
        }
      }
      else if (typeof message === 'object') {
        onOk = option
        option = message
        message = title
        title = '系统提示'
      }
      else if (typeof message === 'function') {
        onCancel = option
        onOk = message
        message = title
        title = '系统提示'
      }
      if (typeof onOk !== 'function') {
        onOk = () => {}
      }
      if (typeof onCancel !== 'function') {
        onCancel = () => {}
      }
      this.confirm(message, title, option).then(onOk).catch(onCancel)
    }
    /**
     * 消息提示
     */
    Vue.prototype.$error = message => {
      Vue.prototype.$message({
        type: 'error',
        message
      })
    }
    Vue.prototype.$success = message => {
      Vue.prototype.$message({
        type: 'success',
        message
      })
    }
    Vue.prototype.$warning = message => {
      Vue.prototype.$message({
        type: 'warning',
        message
      })
    }
    /**
     * 消息通知
     */
    Vue.prototype.$$message = (title, message) => {
      if (message === undefined) {
        message = title
        title = '系统提示'
      }
      Vue.prototype.$notify({
        title,
        message
      })
    }
    Vue.prototype.$$error = (title, message) => {
      if (message === undefined) {
        message = title
        title = '系统提示'
      }
      Vue.prototype.$notify({
        title,
        message,
        type: 'error'
      })
    }
    Vue.prototype.$$success = (title, message) => {
      if (message === undefined) {
        message = title
        title = '系统提示'
      }
      Vue.prototype.$notify({
        title,
        message,
        type: 'success'
      })
    }
    Vue.prototype.$$warning = (title, message) => {
      if (message === undefined) {
        message = title
        title = '系统提示'
      }
      Vue.prototype.$notify({
        title,
        message,
        type: 'warning'
      })
    }
  }
}
