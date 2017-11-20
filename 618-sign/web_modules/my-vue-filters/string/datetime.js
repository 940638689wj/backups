/**
 * 格式化时间戳
 * @param  {Number} timestamp 时间戳
 * @return {String}
 * @example
 * {{ xxx | datetime }}
 */
export default function (timestamp) {
  if (timestamp) {
    return DateObjToString(new Date(timestamp))
  }
  else {
    return timestamp
  }
}

/**
 * @param {object} value 原生 Date 对象
 */
function DateObjToString (value) {
  let year   = value.getFullYear()
  let month  = value.getMonth() + 1
  let date   = value.getDate()
  let hour   = FormatTime(value.getHours())
  let minute = FormatTime(value.getMinutes())
  let second = FormatTime(value.getSeconds())
  return year + '-' + month + '-' + date + ' ' + hour + ':' + minute + ':' + second
}

/**
 * 格式化时间
 * @param {integer} value 时间值
 */
function FormatTime (value) {
  if (value < 10) {
    value = '0' + value
  }
  return value
}
