<template>
  <div class="provider-table">
    <table>
      <thead>
        <slot name="thead"></slot>
      </thead>
      <tbody>
        <slot name="tbody"></slot>
      </tbody>
    </table>
  </div>
</template>

<style lang="less" scoped>
  @import '~global/variable.less';

  .provider-table {

      table {
        width: 100%;
        border-collapse: collapse;
        font-size: 14px;

        a {
          text-decoration: none;
          cursor: pointer;
          color: #4b79bd;

          &:hover {
            color: #FF7F00;
          }
        }

        th {
          border-bottom: solid 3px #A1A8B3;
          font-weight: normal;
          height: 49px;
          line-height: 49px;
        }

        tbody {

          tr {
            border: solid 1px #CFCFD0;

            td {
              padding: 10px;
              color: #333;
              background-color: #F2F5FA;
              text-align: center;

              &.info {
                position: relative;
                min-width: 225px;
                text-align: left;

                img {
                  width: 80px;
                  height: 80px;
                  background-color: #EEEEEE;
                }

                > div {
                  position: absolute;
                  left: 100px;
                  top: 10px;
                  overflow: hidden;
                  height: 80px;
                  
                  p {
                    margin: 0;
                    font-size: 14px;
                    color: #333;
                  }

                  span {
                    position: absolute;
                    bottom: 0;
                    color: #999;
                  }
                }
              }

              &.rate {
                text-align: center;
                width: 126px;
                color: #999;

                .el-rate {
                  margin-bottom: 5px;
                }
              }
              
              &.amount {
                font-size: 18px;
                color: @moneyColor;
              }

            }
          }

          tr.empty {
            height: 10px;
          }

          tr.footer {
            .left {
              float: left;
              span {
                color: #ff1900;
                margin-right: .5em;
              }
            }
            .right {
              float: right;
              span {
                color: #ff1900;
                margin-right: .5em;
              }
            }
          }

        }

      }
  }
</style>