<template>
  <div class="my-data-table">
    <table width="100%">
      <thead>
        <slot name="thead"></slot>
      </thead>
      <tbody>
        <slot name="tbody"></slot>
      </tbody>
    </table>
    <div class="data-empty-text" v-show="$slots.tbody === undefined"><span v-text="emptyText"></span></div>
  </div>
</template>

<script>
  export default {
    props: {
      emptyText: {default: '暂无数据'}
    }
  }
</script>

<style lang="less">
  /** 自定义数据表样式 **/
  .my-data-table {
    margin: 0;
    padding: 0;
    font-size: 0;
    

    .data-empty-text{
      height: 400px;
      text-align: center;
      position: relative;
      border: 1px solid #d9e6fa;
      border-top-width: 4px;
      background-color: #f7f8fa;

      span {
        font-size: 14px;
        top: 50%;
        left: 50%;
        position: absolute;
        background-color: #f7f8fa;
        transform: translate(-50%,-50%);
        -ms-transform: translate(-50%,-50%);
      }
    }


    table {
       border-collapse:collapse;

       .el-select {
        .el-input__inner {
          border: 1px solid #d9e6fa;
          border-radius: 1px;
        }
       }
    }

    thead {
      background-color: #f2f5fa;
      border-bottom: 3px solid #d9e6fa;

      tr {
        height: 41px;
      }

      th {
        font-size: 14px;
        font-weight: bold;
        text-align: center;
      }
    }

    tbody {
      background-color: #ccc;
      border-left: 1px solid #d9e6fa;
      border-right: 2px solid #d9e6fa;

      tr {
        height: 47px;
        background-color: #f2f5fa;
        border-bottom: 1px solid #d9e6fa;
      }

      tr:nth-child(odd){
          background-color: #f7f8fa;
      }

      td {
        font-size: 14px;
        text-align: center;
      }
      
      input {
        height: 28px;
      }

      .el-input {
        .el-input__inner {
          height: 28px;
          border-radius: 1px;
          border: 1px solid #d9e6fa;
        }
      }
    }
    .span {
      display: inline-block;
    }

  }
</style>