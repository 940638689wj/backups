<template>
  <div class="hello">
    <h1>标题</h1>
    <span>一些内容
      <p>小段落</p>
    </span>
    {{order}}
  </div>
  <!-- <el-carousel indicator-position="outside">
    <el-carousel-item v-for="item in picList" :key="item">
      <h3>{{ item }}</h3>
    </el-carousel-item>
  </el-carousel> -->
</template>

<script>
  export default{
    data () {
      return {
        order: {}
        // picList: [1, 2, 3, 4]
      }
    },
    methods: {
    },
    created () {
      // this.conNum = (0, this.updNum)(1000, this.updNum2)
      this.$http.get('/orderHeader/orderHeaderDetail?orderId=1049').then(
        res => {
          this.order = res.body
        }
        )
      this.$http.get('/orderHeader/orderHeaderDetail?orderId=1049').then(
        res => {
          this.order = res.body
        }
        )
    },
    mounted () {
    }
  }
</script>

<style lang="less">
@fontColor: blue;
.hello{
  font-size: 25px;

  span{
    color: @fontColor;

    p{
      font-weight: bold;
    }

  }
}
/*  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }*/
</style>
