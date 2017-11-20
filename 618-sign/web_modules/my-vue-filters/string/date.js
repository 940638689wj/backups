/**
 * 格式化时间戳
 * @param  {Number} timestamp 时间戳
 * @return {String}
 * @example
 * {{ xxx | date }}
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
  let year  = value.getFullYear()
  let month = value.getMonth() + 1
  let date  = value.getDate()
  return year + '-' + month + '-' + date
}
