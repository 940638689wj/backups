// see http://vuejs-templates.github.io/webpack for documentation.
var path = require('path')

module.exports = {
  build: {
    env: require('./prod.env'),
    index: path.resolve(__dirname, '../dist/index.html'),
    assetsRoot: path.resolve(__dirname, '../dist'),
    assetsSubDirectory: 'static',
    assetsPublicPath: '',
    productionSourceMap: false,
    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to `true`, make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false,
    productionGzipExtensions: ['js', 'css']
  },
  dev: {
    env: require('./dev.env'),
    port: 8084,
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
    proxyTable: {
      // proxy all requests starting with /api to server
      '/test': {
        // target: 'http://192.168.2.207:8066',
        target: 'http://test2.fjmxj.cn/activity/',
        changeOrigin: true,
        pathRewrite: {
          '^/test': '/'
        }
      },
      '/api': {
        // target: 'http://apib.yifishes.com', // 解决跨域问题，服务代转发，使用window.location.host访问
        target: 'http://www.lanhaitianwang.com/weiphp/JSSDK_LIB/SERVER/',
        changeOrigin: true,
        pathRewrite: {
          '^/api': '/'
        }
      },
      '/local': {
        target: 'http://192.168.2.207:8066/',
        // target: 'http://10.1.1.10',
        changeOrigin: true,
        pathRewrite: {
          '^/local': '/'
          // '^/local': '/'
        }
      }
    },
    // CSS Sourcemaps off by default because relative paths are "buggy"
    // with this option, according to the CSS-Loader README
    // (https://github.com/webpack/css-loader#sourcemaps)
    // In our experience, they generally work as expected,
    // just be aware of this issue when enabling this option.
    cssSourceMap: false
  }
}
