<template>
  <el-tabs v-model="activeName" type="card">
    <el-tab-pane label="三层 & BUI表格" name="first">
      <el-form ref="form" :model="form" :rules="rules" label-width="150px">
        <el-form ref="fieldsForm" label-width="80px" :inline="true">
        <h3>
          &nbsp;&nbsp;字段信息
          <el-button @click="addField()">添加字段</el-button>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从数据库导入：
          <el-popover ref="popover1" placement="right" width="300" trigger="click">
            <el-form ref="database" :model="form" label-width="100px">
              <el-form-item label="数据库名">
                <el-input v-model="database.databaseName"></el-input>
              </el-form-item>
              <el-form-item label="IP或主机">
                <el-input v-model="database.ipOrHost"></el-input>
              </el-form-item>
              <el-form-item label="端口">
                <el-input v-model="database.port"></el-input>
              </el-form-item>
              <el-form-item label="用户名">
                <el-input v-model="database.username"></el-input>
              </el-form-item>
              <el-form-item label="密码">
                <el-input v-model="database.password" type="password"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button :plain="true" type="info" @click="testDatabase()">测试连接</el-button>
                <el-button type="primary" @click="connectDatabase()">确认</el-button>
              </el-form-item>
            </el-form>
          </el-popover>
          <el-button :plain="true" type="info" v-popover:popover1>配置数据库源</el-button>
          &nbsp;选择表
          <el-select v-model="tableName" clearable filterable placeholder="可输入中英文表名模糊查询" @change="choseTable()">
            <el-option v-for="tableInfo in tableList" :label="tableInfo.label" :value="tableInfo.value">
            </el-option>
          </el-select>
        </h3>
        <transition-group name="list-complete" tag="p">
          <div v-for="(field,index) in form.fieldsForm" :key='field' class="list-complete-item">
            <el-form-item label="字段名">
              <el-input v-model="field.fieldName"></el-input>
            </el-form-item>
            <el-form-item label="中文名">
              <el-input v-model="field.fieldCnName"></el-input>
            </el-form-item>
            <el-form-item label="java类型">
              <el-select v-model="field.fieldType">
                <el-option v-for="option in fieldTypeOptions" :label="option.text" :value="option.value"></el-option>
              </el-select>
            </el-form-item>
            <el-button :plain="true" type="danger" @click="delField(index)">删除</el-button>
          </div>
        </transition-group>
      </el-form>
      <br/>
      <el-form-item label="表名" prop="tableName">
        <el-col :span="6"><el-input v-model="form.tableName"></el-input></el-col>
      </el-form-item>
      <el-form-item label="控制器URL">
        <el-col :span="6"><el-input v-model="form.controllerUrl" placeholder="可不填"></el-input></el-col>
      </el-form-item>
      <el-form-item label="主键自增">
        <el-radio-group v-model="form.isAutoIncrement">
          <el-radio :label="1">是</el-radio>
          <el-radio :label="0">否</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="update使用if">
        <el-radio-group v-model="form.isUpdateUseIf">
          <el-radio :label="1">是</el-radio>
          <el-radio :label="0">否</el-radio>
        </el-radio-group>
        <!-- （使用if则将最后一个字段作为必更新字段） -->
      </el-form-item>
      <el-form-item label="生成BUI表格页面">
        <el-radio-group v-model="form.isAdminTable">
          <el-radio :label="1">是</el-radio>
          <el-radio :label="0">否</el-radio>
        </el-radio-group>
      </el-form-item>
      <transition name="slide-fade">
        <div v-if='form.isAdminTable'>
          <el-form-item label="表格数据使用DTO">
            <el-radio-group v-model="form.isUseDto">
              <el-radio :label="1">是</el-radio>
              <el-radio :label="0">否</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="新增/修改">
            <el-radio-group v-model="form.isSave">
              <el-radio :label="1">是</el-radio>
              <el-radio :label="0">否</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="删除">
            <el-radio-group v-model="form.isDel">
              <el-radio :label="1">是</el-radio>
              <el-radio :label="0">否</el-radio>
            </el-radio-group>
          </el-form-item>
        </div>
      </transition>
      <el-form-item>
        <el-button type="primary" @click="download()">下载</el-button>
        <el-button :plain="true" type="warning" @click="reset()">重置</el-button>
      </el-form-item>
    </el-form>
    </el-tab-pane>
  </el-tabs>
</template>
<script>
  // var $ = require('jquery')
  export default {
    data () {
      return {
        form: {
          fieldsForm: [
            {fieldName: '', fieldCnName: '', fieldType: 'String'},
            {fieldName: '', fieldCnName: '', fieldType: 'String'}
          ],
          tableName: '',
          controllerUrl: '',
          isAutoIncrement: 1,
          isUpdateUseIf: 1,
          isAdminTable: 0,
          isUseDto: 0,
          isSave: 1,
          isDel: 1
        },
        rules: {
          tableName: [
            { required: true, message: '请输入表名', trigger: 'blur' },
            { min: 2, message: '至少 2 个字符', trigger: 'blur' }
          ]
        },
        fieldTypeOptions: [
          {value: 'String', text: 'String'},
          {value: 'Integer', text: 'Integer'},
          {value: 'Date', text: 'Date'},
          {value: 'Double', text: 'Double'},
          {value: 'BigDecimal', text: 'BigDecimal'},
          {value: 'Float', text: 'Float'},
          {value: 'Boolean', text: 'Boolean'}
        ],
        tableList: [],
        tableName: '',
        database: {
          databaseName: '',
          ipOrHost: '192.168.10.232',
          port: '',
          username: '',
          password: ''
        },
        activeName: 'first'
      }
    },
    methods: {
      // 添加字段
      addField: function () {
        this.form.fieldsForm.push({fieldName: '', fieldCnName: '', fieldType: 'String'})
      },
      // 删除字段
      delField: function (index) {
        this.form.fieldsForm.splice(index, 1)
      },
      // 点击下载
      download: function () {
        this.$refs['form'].validate((valid) => {
          if (!valid) {
            return false
          }
          // 简单表单验证
          if (this.form.fieldsForm.length < 2) {
            this.$message.error('字段不能少于两个噢~')
            return false
          }
          var fieldsForm = this.form.fieldsForm
          for (var i = 0; i < fieldsForm.length; i++) {
            if (fieldsForm[i].fieldName === '' || fieldsForm[i].fieldCnName === '') {
              this.$message.error('字段信息不能为空噢~')
              return false
            }
          }
          this.$http.post('/auto_code/generate_template', this.form, {emulateJSON: true}).then(
            function (res) {
              // 处理成功的结果
              this.$message.success('下载成功~')
              window.location.href = '/auto_code/download'
            }, function (res) {
              // 处理失败的结果
            this.$message.error('失败啦~不懂为啥T-T')
          }
          )
        })
      },
      // 重置
      reset: function () {
        // this.$refs['form'].resetFields()
        this.form = {
          fieldsForm: [
            // {fieldName: '', fieldCnName: '', fieldType: 'String'},
            // {fieldName: '', fieldCnName: '', fieldType: 'String'}
          ],
          tableName: '',
          controllerUrl: '',
          isAutoIncrement: 1,
          isUpdateUseIf: 1,
          isAdminTable: 1,
          isUseDto: 1,
          isSave: 1,
          isDel: 1
        }
        this.tableName = ''
      },
      // 选择数据库表后
      choseTable: function () {
        this.form.tableName = this.tableName
        // 清空下拉时不需要访问后台
        if (this.tableName === '') {
          this.form.fieldsForm = [
            {fieldName: '', fieldCnName: '', fieldType: 'String'},
            {fieldName: '', fieldCnName: '', fieldType: 'String'}
          ]
        } else {
          this.$http.post('/auto_code/table_struct', {'tableName': this.tableName}, {emulateJSON: true}).then(
            function (res) {
              // 处理成功的结果
              if (res.body.data.length > 0) {
                this.form.fieldsForm = res.body.data
              }
              // this.tableList = res.body.data
            }, function (res) {
              // 处理失败的结果
          }
          )
        }
      },
      // 测试数据库连接
      testDatabase: function () {
        if (this.database.ipOrHost === 'dev.xmyr.cn') {
          this.$message.error('ip或主机不可使用外网域名噢~')
          return false
        }
        this.$http.post('/auto_code/test_connect', this.database, {emulateJSON: true}).then(
            function (res) {
              // 处理成功的结果
              if (res.body.data.result) {
                this.$message.success('该连接可用~')
              } else {
                this.$message.error('连接不可用>_<')
              }
              // this.tableList = res.body.data
            }, function (res) {
              // 处理失败的结果
          this.$message.error('连接不可用>_<')
        }
        )
      },
      // 连接数据库
      connectDatabase: function () {
        this.tableName = ''
        this.tableList = []
        this.$http.post('/auto_code/create_connect', this.database, {emulateJSON: true}).then(
            function (res) {
              // 处理成功的结果
              if (res.body.data.result) {
                this.$message.success('连接数据库成功~')
                // 加载下拉数据
                this.$http.get('/auto_code/table_list', {emulateJSON: true}).then(
                  function (res) {
                    // 处理成功的结果

                    this.tableList = res.body.data
                  }, function (res) {
                    // 处理失败的结果
                  this.$message.error('获取表失败>_<')
                }
                )
              } else {
                this.$message.error('获取表失败>_<')
              }
              // this.tableList = res.body.data
            }, function (res) {
              // 处理失败的结果
          this.$message.error('连接失败>_<')
        }
        )
      }
    },
    // 页面初始化
    created () {
      console.log('created')
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
  transform: translateX(30px);
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
</style>
