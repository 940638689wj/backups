<template>
  <div id="app">
    <el-col :span="4" class="colleft"><Nav></Nav></el-col>
    <el-col :span="20" class="colright"><UpdateServer></UpdateServer></el-col>
  </div>
</template>

<script>
import UpdateServer from './components/UpdateServer'
import Nav from './components/Nav'

export default {
  name: 'app',
  components: {
    UpdateServer,
    Nav
  }
}

</script>

<style>
body{
  margin: 0;
}
.colleft{
  position: fixed;
  top:0;
  left:0;
  bottom:0;
  background: #eef1f6;
}
.colright{
  margin-left: 16.66666666%;
}
</style>
