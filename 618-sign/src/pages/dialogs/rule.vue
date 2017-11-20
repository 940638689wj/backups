<template>
  <div class="dialogs-rule">
    <dialogs :title="title" v-model="visible">
      <div class="rule-content">
        1.用户利用手机号（必填）、年龄+职业（选填）进行登录并创建个人相册；
        <br>
        2.用户上传活鱼照片，每天不少于5张，积累上传15或30天将获得相对应的奖品；
        <br>
        3.用户上传图片必须为亲自拍摄的鱼类图片，否则将视为无效上传；
        <br>
        4.用户邀请好友来参与活动，根据邀请好友数量可获得相对应的奖品；
        <br>
        5.邀请好友规则：邀请好友创建个人相册并上传5张拍摄的鱼类图片则视为成功邀请；
        <br>
        6.用户可邀请好友来对相册进行点赞，点赞数最多的前三位用户将获得点赞大奖，用户通过手机号验证即可参与点赞，一天可为点赞数为
        3次；禁止一切违规刷票行为，一经发现将视
        为无效；
        <br>
        7.活动奖品将以快递的方式进行发放；
        <br>
        8.活动第一阶段时间：2017.06.15-07.25；
        <br>
        9.活动奖品发放时间：2017.07.30；
        <br>
         “蓝海天网”微信公众号后台留言，将有活动人员与您取得联系。
      </div>
    </dialogs>
  </div> 
</template>

<script>
  import dialogs from './base.vue'
  export default {
    components: { dialogs },
    props: {
      value: {default: false, type: Boolean}
    },
    data () {
      return {
        visible: false,
        title: '活动规则'
      }
    },
    watch: {
      value: function (val) {
        this.visible = val
      },
      visible: function (val) {
        this.$emit('input', val)
      }
    },
    methods: {}
  }
</script>

<style lang="less">
.dialogs-rule {
  .rule-content {
    text-align: left;
    font-size: 24rem / 20;
    line-height: 38rem / 20;
  }
}
  
</style>