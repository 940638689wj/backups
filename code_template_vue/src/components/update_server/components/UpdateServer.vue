<template>
  <el-tabs v-model="activeName" type="card" @tab-click="changeTab">
  <!-- 页签一 -->
    <el-tab-pane label="更新项目" name="update_server">
      <el-form ref="form" label-width="150px" id="form">
        <el-form-item label="war文件" prop="">
          <el-col :span="6">
            <!-- <el-input type="file" name="file" id="file"></el-input> -->
            <el-upload
              class="upload-demo"
              action="/update_server/upload_war"
              :on-success="onSuccess"
              :on-remove="onRemove"
              :before-upload='beforeUpload'>
              <el-button size="small" type="primary" icon="upload2">上传</el-button>
              <div slot="tip" class="el-upload__tip"></div>
            </el-upload>
          </el-col>
          <el-checkbox v-model="updateAfterUpload">上传完成后自动开始更新</el-checkbox>
        </el-form-item>
        <el-form-item label="文件夹名称" prop="dir">
          <el-col :span="6">
            <el-select v-model="form.dir" filterable clearable placeholder="可输入内容模糊搜索" style="width:100%">
              <el-option
                v-for="dir in dirList"
                :key="dir"
                :label="dir"
                :value="dir">
              </el-option>
            </el-select>
            <!-- <el-input v-model="form.dir" icon="circle-cross" :on-icon-click="resetDir"></el-input> -->
          </el-col>
        </el-form-item>
        <el-form-item label="密码" prop="dir">
          <el-col :span="6">
            <el-input v-model="form.password" type="password" icon="circle-cross" :on-icon-click="resetPassword"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="update()">更新</el-button>
        </el-form-item>
        <el-form-item>
          <div v-if="step == 1"><i class="el-icon-loading"></i><span style="margin-left:10px">解压中</span></div>
          <div v-if="step == 2"><i class="el-icon-success"></i><span style="margin-left:10px">解压覆盖完成，已关闭服务器</span></div>
          <div v-if="step == 2"><i class="el-icon-warning"></i><span style="margin-left:10px">重启服务器中,请自行查看是否重启完成</span></div>
          <div v-if="step == 3"><i class="el-icon-success"></i><span style="margin-left:10px">重启成功</span></div>
        </el-form-item>
      </el-form>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="line-height: 36px;float:left;" class="log-toolbar">查看日志</span>
          <el-col :span="3" class="log-toolbar">
            <el-input v-model="logsForm.dir" icon="circle-cross" :on-icon-click="resetLogsDir"></el-input>
          </el-col>
          <span style="line-height: 36px;float:left;margin:0 20px 0 2px">文件夹</span>
          <el-button class="log-toolbar" @click="readLogs" type="primary" :loading="logsRefreshing">刷新</el-button>
          {{restartStatus}}
        </div>
        <el-input type="textarea" v-model="logs" :rows="18" id="logs"></el-input>
      </el-card>
    </el-tab-pane>
    <!-- 页签二 -->
    <el-tab-pane label="编辑nginx配置" name="edit_nginx">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="line-height: 36px;float:left;" class="log-toolbar">nginx配置</span>
          <el-button class="log-toolbar" @click="getNginx" type="primary" :loading="nginxRefreshingList[0]">加载</el-button>
          <el-button class="log-toolbar" @click="saveNginx" type="primary" :loading="nginxRefreshingList[1]">保存</el-button>
          <el-button class="log-toolbar" @click="checkNginx" type="primary" :loading="nginxRefreshingList[2]">检查</el-button>
          <el-button class="log-toolbar" @click="reloadNginx" type="primary" :loading="nginxRefreshingList[3]">重启</el-button>
          <span style="line-height: 36px;float:left;margin-left: 20px">密码</span>
          <el-col :span="2" style="margin:0 20px 0 1px">
            <el-input v-model="nginxPassowrd" type="password" icon="circle-cross" :on-icon-click="resetNginxPassword"></el-input>
          </el-col>
        </div>
        <el-input type="textarea" v-model="nginxProperties" :rows="25" id="nginx"></el-input>
        <div style="margin-top: 10px" v-html="validateNginx"></div>
      </el-card>
    </el-tab-pane>
  </el-tabs>
</template>
<script>
  import $ from 'jquery'
  import Vue from 'vue'

  export default {
    data () {
      return {
        activeName: 'update_server',
        dirList: [], // 文件夹列表
        form: {
          dir: '',
          password: '',
          fileName: ''
        },
        logsForm: {
          dir: ''
        },
        hasUpload: 0, // 上传数量
        step: 0,
        logs: '',
        logsRefreshing: false,
        nginxRefreshingList: [false, false, false, false],
        nginxPassowrd: '',
        nginxProperties: '',
        validateNginx: '',
        updateAfterUpload: true,
        restartStatus: '',
        readLogsForRestartId: '',
        readLogsForRestartSeconds: 0
      }
    },
    computed: {
      nginxMenuIndex () {
        return this.$store.state.nginxMenuIndex
      }
    },
    watch: {
      nginxMenuIndex (val) {
        if (val === '1') {
          this.activeName = 'update_server'
        } else if (val === '2') {
          this.activeName = 'edit_nginx'
        }
      },
      'form.dir': {
        handler (val, oldVal) {
          if (oldVal === this.logsForm.dir) {
            this.logsForm.dir = val
          }
        }
      }
    },
    methods: {
      // 切换标签页
      changeTab (tab) {
        this.$store.commit('setNginxMenuIndex', parseInt(tab.index) + 1 + '')
      },
      // 开始更新
      update () {
        this.restartStatus = ''
        if (this.hasUpload !== 2) {
          this.$message.error('上传完成后才能更新')
          return false
        }
        if (!this.form.dir) {
          this.$message.error('文件夹不能为空')
          return false
        }
        if (!this.form.password) {
          this.$message.error('密码不能为空')
          return false
        }
        this.$http.post('/update_server/validate_password', {
          password: this.form.password
        }, {
          emulateJSON: true
        }).then(
        res => {
          if (res.body === 'true') {
            this.step = 1
            this.$http.post('/update_server/start_update', this.form, {emulateJSON: true}).then(
              res => {
                this.step = 2
                // 不断刷新日志判断是否重启成功
                this.readLogsForRestartSeconds = 0
                this.readLogsForRestartId = setInterval(readLogsForRestart, 2000)
                let _this = this
                function readLogsForRestart () {
                  _this.readLogs(true)
                }
              }
              )
          } else {
            this.$message.error('密码错误')
          }
        }
        )
      },
      // 清除文件夹名称
      resetDir () {
        this.form.dir = ''
      },
      // 清除密码
      resetPassword () {
        this.form.password = ''
      },
      // 清除日志的文件夹名称
      resetLogsDir () {
        this.logsForm.dir = ''
      },
      // 清除编辑nginx模块密码
      resetNginxPassword () {
        this.nginxPassowrd = ''
      },
      // 限制上传数量为一个
      beforeUpload (file) {
        // war包名称和下拉模糊匹配
        let defaultIndex = -1
        let defaultMax = 0
        for (let k = 0; k < this.dirList.length; k++) {
          let dir = this.dirList[k]
          let isContinue = true
          for (let i = dir.length; isContinue && i >= 3; i--) {
            for (let j = 0; j <= dir.length - i; j++) {
              if (file.name.indexOf(dir.substr(j, i)) >= 0) {
                if (i > defaultMax) {
                  defaultIndex = k
                  defaultMax = i
                }
                isContinue = false
                break
              }
            }
          }
        }

        if (defaultIndex >= 0) {
          this.form.dir = this.dirList[defaultIndex]
        }

        // 上传条件判断
        if (this.hasUpload !== 0) {
          this.$message.error('只能上传单个文件')
          return false
        }
        let fileNameSplit = file.name.split('.')
        if (fileNameSplit[fileNameSplit.length - 1] !== 'war') {
          this.$message.error('只能上传war文件')
          return false
        }
        this.hasUpload++
      },
      // 上传成功回调
      onSuccess (res, file) {
        this.hasUpload++
        this.form.fileName = file.name

        if (this.updateAfterUpload) {
          this.update()
        }
      },
      // 移除回调
      onRemove (file, fileList) {
        if (fileList.length === 0) {
          this.hasUpload = 0
        }
      },
      // 读取日志
      readLogs (isRestart = false) {
        this.logsRefreshing = true
        this.$http.get('/update_server/read_logs', {
          params: this.logsForm
        }).then(
          res => {
            this.logs = res.body
            Vue.nextTick(() => {
              let textarea = $('#logs textarea')
              textarea.scrollTop(textarea[0].scrollHeight - textarea.height())
              this.logsRefreshing = false
              if (!isRestart) {
                this.$message.success('刷新成功')
              } else {
                this.readLogsForRestartSeconds++
                if (this.readLogsForRestartSeconds > 30) {
                  clearInterval(this.readLogsForRestartId)
                }
                let logsLen = this.logs.length
                if (this.logs.substr(logsLen - 101, 100).indexOf('Server startup in') >= 0) {
                  // this.$message.success('重启完成')
                  this.step = 3
                  clearInterval(this.readLogsForRestartId)
                }
              }
            })
          }
          )
      },
      // 加载nginx配置文件
      getNginx () {
        this.$http.post('/update_server/validate_password', {
          password: this.nginxPassowrd
        }, {
          emulateJSON: true
        }).then(
        res => {
          if (res.body === 'true') {
            this.nginxRefreshingList[0] = true
            this.$http.get('/edit_nginx/get_nginx').then(
              res => {
                this.nginxProperties = res.body
                this.nginxRefreshingList[0] = false
                this.$message.success('加载成功')
                /* eslint-disable*/
                setTimeout('$(\'#nginx textarea\').keydown()', 500)
                /* eslint-enable*/
                // setTimeout(textareaKeydown, 500)
                // function textareaKeydown () {
                //   $('#nginx textarea').keydown()
                // }
              }
              )
          } else {
            this.$message.error('密码错误')
          }
        }
        )
      },
      // 保存nginx配置
      saveNginx () {
        if (!this.nginxProperties) {
          this.$message.error('内容不可为空')
          return false
        }
        this.$http.post('/update_server/validate_password', {
          password: this.nginxPassowrd
        }, {
          emulateJSON: true
        }).then(
        res => {
          if (res.body === 'true') {
            this.nginxRefreshingList[1] = true
            this.$http.post('/edit_nginx/save_nginx', {
              nginxProperties: this.nginxProperties
            }, {
              emulateJSON: true
            }).then(
              res => {
                if (res.body === 'true') {
                  this.nginxRefreshingList[1] = false
                  this.$message.success('保存成功')
                } else {
                  this.$message.error('保存失败')
                }
              }
              )
          } else {
            this.$message.error('密码错误')
          }
        }
        )
      },
      // 检查编译nginx配置文件
      checkNginx () {
        this.validateNginx = ''
        this.$http.post('/update_server/validate_password', {
          password: this.nginxPassowrd
        }, {
          emulateJSON: true
        }).then(
        res => {
          if (res.body === 'true') {
            this.nginxRefreshingList[2] = true
            this.$http.get('/edit_nginx/validate_nginx').then(
              res => {
                this.validateNginx = res.body
                this.nginxRefreshingList[2] = false
                this.$message.success('检查完成')
              }
              )
          } else {
            this.$message.error('密码错误')
          }
        }
        )
      },
      // 重启nginx
      reloadNginx () {
        this.$http.post('/update_server/validate_password', {
          password: this.nginxPassowrd
        }, {
          emulateJSON: true
        }).then(
        res => {
          if (res.body === 'true') {
            this.nginxRefreshingList[3] = true
            this.$http.post('/edit_nginx/reload_nginx').then(
              res => {
                if (res.body === 'true') {
                  this.$message.success('重启成功')
                  this.nginxRefreshingList[3] = false
                } else {
                  this.$message.error('重启失败')
                }
              }
              )
          } else {
            this.$message.error('密码错误')
          }
        }
        )
      }
    },
    created () {
      // 获取文件列表
      this.$http.get('/update_server/get_dir_list').then(
        res => {
          let dirList = res.body.split(',')
          this.dirList = dirList.splice(0, dirList.length - 1)
        }
        )
    }
  }
</script>

<style>
/*添加/删除字段动画*/
.list-complete-item {
  transition: all 1s;
  display: inline-block;
  margin-right: 10px;
}
.list-complete-enter, .list-complete-leave-active {
  opacity: 0;
  transform: translateY(30px);
}
.list-complete-leave-active {
  position: absolute;
}

/*BUI表格额外配置动画*/
.slide-fade-enter-active {
  transition: all .4s ease;
}
.slide-fade-leave-active {
  transition: all .2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-active {
  transform: translateX(10px);
  opacity: 0;
}

/*日志框*/
.box-card{
  margin: 40px;
}
.log-toolbar{
  margin-left: 20px;
}
</style>
