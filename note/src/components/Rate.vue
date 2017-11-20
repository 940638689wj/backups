<template>
  <div class="hello">
  {{msg}}
  <el-rate
    v-model="value2"
    :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
  </el-rate>
  </div>
</template>

<script>
export default {
  name: 'hello',
  props: ['msg'],
  data () {
    return {
    }
  },
  components: {
  },
  created () {
    this.$emit('call', 1)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
