<template>
  <div class="hello">
    <toolbar/>
    <lists/>
    <detail/>
  </div>
</template>

<script>
import toolbar from './toolbar'
import lists from './lists'
import detail from './detail'

export default {
  name: 'hello',
  data () {
    return {
    }
  },
  components: {
    toolbar,
    lists,
    detail
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
