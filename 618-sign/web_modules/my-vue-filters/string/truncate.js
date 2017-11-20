/**
 * 文本截取
 * @param  {String} text   原始文本
 * @param  {Number} length 限制显示的长度
 * @param  {String} clamp  隐藏部分的替换字符串
 * @return {String}
 * @example
 * {{ address.address | truncate(10) }}
 */
export default function (text, length, clamp = '…') {
  if (text) {
    if (text.length <= length) return text
    let tcText = text.slice(0, length - clamp.length)
    return tcText + clamp
  }
  else {
    return text
  }
}
