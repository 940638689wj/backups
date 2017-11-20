<template>
  <div>
    <div class="toolbar">
      <i class="el-icon-plus" @click="add"></i>
      <!-- <i class="el-icon-star-off"></i> -->
      <i class="el-icon-close" @click="del"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
      num: 0
    }
  },
  methods: {
    add () {
      this.$store.commit('addList', 'new note' + this.num)
      this.num++
    },
    del () {
      this.$store.commit('del')
    }
  },
  created () {
  }
}
</script>

<style scoped>
.toolbar{
  width: 100px;
  height: 100%;
  background-color: rgb(48,65,77);
  color: white;
  float: left;
}
.toolbar i{
  -moz-transform:scale(2,2); 
  -webkit-transform:scale(2,2); 
  -o-transform:scale(2,2); 
  margin: 40px;
  opacity: 0.5;
}
</style>
