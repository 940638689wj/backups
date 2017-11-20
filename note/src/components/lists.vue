<template>
  <div>
    <div class="list">
      <div class="list-title">列表{{msg}}</div>
      <div class="list-content" v-for="(note,i) in list" @click="check(i)">{{note}}</div>
      <!-- <el-input v-model="input" placeholder="请输入内容"></el-input> -->
    </div>
      
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
    }
  },
  computed: {
    list () {
      return this.$store.state.list
    }
  },
  methods: {
    check (i) {
      this.$store.commit('setIndex', i)
    }
  },
  created () {
    // this.$store.state.msg = 'abc'
  }
}
</script>

<style scoped>
.list{
      width: 300px;
      height: 600px;
      background-color: rgb(245,245,245);
      float: left;
    }
    .list-title{
      margin: 30px 0 50px 100px;
      font-size: 20px;
    }
    .list-content{
      width: 100%;
      height: 40px;
      font-size: 20px;
      background-color: white;
      border-bottom: 1px solid #cccccc;
      padding-top: 15px;
    }
</style>
