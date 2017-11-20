<template>
  <div>
    <div class="detail">
      <textarea @input="input($event)" :value="list[index]"></textarea>
      <!-- <el-input
        type="textarea"
        autosize
        placeholder="请输入内容"
        v-model="textarea2">
      </el-input> -->
    </div>
    <Rate :msg="'内容页面'" @call="conso"></Rate>
  </div>
</template>

<script>
import Rate from './Rate'

export default {
  name: '',
  data () {
    return {
    }
  },
  components: {
    Rate
  },
  computed: {
    list () {
      return this.$store.state.list
    },
    index () {
      return this.$store.state.index
    }
  },
  watch: {
  },
  methods: {
    input (e) {
      this.$store.commit('changeList', e.target.value)
    },
    conso () {
      console.log('测试')
    }
  },
  created () {
  }
}
</script>

<style scoped>
.detail,.detail textarea{
      width: 500px;
      height: 500px;
      float: left;
    }
</style>
