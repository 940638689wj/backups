# Less

## less 导入说明
引入样式一个项目在全局引用一次即可
>@import '~global/main.less';

引入统一变量如色值, 尺寸等信息便于主题管理
>@import '~global/variable.less';

## less 目录/文件说明

./main.less (项目引用样式入口文件)

./variable.less (项目公用变量配置文件)

./less (为方便管理less 文件统一存放目录)

./less/elementExt (对饿了么UI组建进行扩展文件存放路径)

./less/custom (自定义样式块存放目录)