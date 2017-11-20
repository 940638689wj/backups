<template>
  <el-date-picker :value="value" @input="Input" :type="type" :editable="false" :placeholder="placeholder" :picker-options="pickerOptions || defaultPickerOptions">
  </el-date-picker>
</template>

<script>
  export default {
    props: {
      value: '',
      type: {
        type: String,
        default: 'datetime'
      },
      placeholder: String,
      pickerOptions: Object
    },
    data () {
      return {
        defaultPickerOptions: {
          disabledDate (time) {
            return time.getTime() > Date.now()
          }
        }
      }
    },
    methods: {
      /**
       * 输入，触发 v-model 绑定
       * @param {object} value 原生 Date 对象
       */
      Input (value) {
        if (this.type === 'daterange') {
          this.$emit('input', value)
        }
        else {
          this.$emit('input', Date.parse(value))
        }
      }
    }
  }
</script>