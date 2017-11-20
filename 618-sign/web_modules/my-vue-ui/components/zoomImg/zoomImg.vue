<template>
<div class="zoomImg">
  <ul class="small-imgs">
    <li v-for="(vo, index) in smallImgs" @click="ActiveImg(index, $event)">
      <img :src="vo.src" :alt="vo.alt">
      <b></b>
    </li>
  </ul>
  <ul class="big-imgs">
    <li v-for="(vo, index) in bigImgs">
      <img :src="vo.src" :alt="vo.alt">
    </li>
  </ul>
</div>
</template>

<script>
  export default {
    props: {
      bigImgs: {default: []},
      smallImgs: {default: []}
    },
    methods: {
      /**
       * 小图被激活时触发
       */
      ActiveImg (index, event) {
        let thisDom = event.currentTarget
        let bigImgDom = thisDom.parentNode.parentNode.getElementsByClassName('big-imgs')[0]
        let smallImgDom = thisDom.parentNode
        let count = bigImgDom.getElementsByTagName('li').length
        for (let i = 0; i < count; i++) {
          bigImgDom.getElementsByTagName('li')[i].style.display = 'none'
          smallImgDom.getElementsByTagName('li')[i].className = ''
        }
        thisDom.className = 'active'
        bigImgDom.getElementsByTagName('li')[index].style.display = 'inline-block'
      }
    }
  }
</script>

<style lang="less">
@import '~global/variable.less';
.zoomImg {
  .small-imgs {
    padding: 0;
    li {
      width: 60px;
      height: 60px;
      display: inline-block;
      border: 2px solid @borderColor;
      position: relative;
      &.active {
         border: 2px solid @baseColor !important;
         & b {
          margin: 0;
          padding: 0;
          border: 8px dashed transparent;
          border-top: 8px solid @baseColor;
          position: absolute;
          left: 22px;
          bottom: -16px;
         }
      }
    }

    img {
      width: 55px;
      margin: 2px;
      height: 55px;
      background-color: #FCFCFC;
    }
  }

  .big-imgs {
    margin: 0;
    padding: 0;
    li {
      font-size: 0;
      display: none;
      // display: inline-block;
      max-width: 420px;
      border: 2px solid @borderColor !important;
    }

    img {
      margin: 4px;
      max-width: 410px;
    }
  }
}

</style>