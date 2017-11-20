<template>
  <div class="hello">
    <el-form :inline="true" :model="formInline" class="demo-form-inline">
      <el-form-item label="账号">
        <el-input v-model="formInline.user" placeholder="账号"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="formInline.password" placeholder="密码"></el-input>
      </el-form-item><el-form-item>
        <!-- <router-link :to="{name: 'Hello'}"> -->
        <el-button type="primary" @click="onSubmit">登录</el-button>
        <!-- </router-link> -->
      </el-form-item>
    </el-form>
    <Rate :msg="'这个是登录页面'" @call="ale"></Rate>
  </div>
</template>

<script>
import router from '@/router'
import Rate from './Rate'

export default {
  name: 'hello',
  data () {
    return {
      formInline: {
        user: '',
        password: ''
      }
    }
  },
  components: {
    Rate
  },
  methods: {
    onSubmit () {
      router.push({name: 'Hello'})
    },
    ale (num) {
      // alert('数据是' + num)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
