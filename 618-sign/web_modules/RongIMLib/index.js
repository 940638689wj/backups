/**
 * 需在入口 HTML 文件中，手动引入 SDK 脚本
 * <script src='http://cdn.ronghub.com/RongIMLib-2.2.4.min.js'></script>
 */
const AppKey = 'n19jmcy5nidd9'
let RongIMLib = window.RongIMLib
let RongIMClient = RongIMLib.RongIMClient

// 初始化 SDK
RongIMClient.init(AppKey)

// 连接状态监听器
RongIMClient.setConnectionStatusListener({
  onChanged: function (status) {
    switch (status) {
      case RongIMLib.ConnectionStatus.CONNECTED:
        console.log('链接成功')
        break
      case RongIMLib.ConnectionStatus.CONNECTING:
        console.log('正在链接')
        break
      case RongIMLib.ConnectionStatus.DISCONNECTED:
        console.log('断开连接')
        break
      case RongIMLib.ConnectionStatus.KICKED_OFFLINE_BY_OTHER_CLIENT:
        console.log('其他设备登录')
        break
      case RongIMLib.ConnectionStatus.DOMAIN_INCORRECT:
        console.log('域名不正确')
        break
      case RongIMLib.ConnectionStatus.NETWORK_UNAVAILABLE:
        console.log('网络不可用')
        break
    }
  }
})

// 消息监听器
RongIMClient.setOnReceiveMessageListener({
  // 接收到的消息
  onReceived: function (message) {
    // 判断消息类型
    switch (message.messageType) {
      case RongIMClient.MessageType.TextMessage:
        // message.content.content => 消息内容
        console.log(message, message.content.content)
        break
      case RongIMClient.MessageType.VoiceMessage:
        // 对声音进行预加载
        // message.content.content 格式为 AMR 格式的 base64 码
        break
      case RongIMClient.MessageType.ImageMessage:
        // message.content.content => 图片缩略图 base64。
        // message.content.imageUri => 原图 URL。
        break
      case RongIMClient.MessageType.DiscussionNotificationMessage:
        // message.content.extension => 讨论组中的人员。
        break
      case RongIMClient.MessageType.LocationMessage:
        // message.content.latiude => 纬度。
        // message.content.longitude => 经度。
        // message.content.content => 位置图片 base64。
        break
      case RongIMClient.MessageType.RichContentMessage:
        // message.content.content => 文本消息内容。
        // message.content.imageUri => 图片 base64。
        // message.content.url => 原图 URL。
        console.log('RichContentMessage', message.content)
        break
      case RongIMClient.MessageType.InformationNotificationMessage:
        // do something...
        break
      case RongIMClient.MessageType.ContactNotificationMessage:
        // do something...
        break
      case RongIMClient.MessageType.ProfileNotificationMessage:
        // do something...
        break
      case RongIMClient.MessageType.CommandNotificationMessage:
        // do something...
        break
      case RongIMClient.MessageType.CommandMessage:
        // do something...
        break
      case RongIMClient.MessageType.UnknownMessage:
        // do something...
        break
      default:
        // do something...
    }
  }
})

let token = 'edXE7SC0lHMwJMKocOjzMDd2wWm8+WNingkcDq1g2Fxgc9uFcnV3jN1q2guSsIoTO077U2M82ofEnq86kYgNqQ==' // mobile: 18959113989 id: 74
// let token = '/jJ0ehHeeG9q47zpWsCviDd2wWm8+WNingkcDq1g2Fxgc9uFcnV3jMRUJyeTvT0th0LR3fT1WkDEnq86kYgNqQ==' // mobile: 15060410838 id: 73

RongIMClient.connect(token, {
  onSuccess (userId) {
    console.log('Login successfully.' + userId)
  },
  onTokenIncorrect () {
    console.log('token无效')
  },
  onError (errorCode) {
    let info = ''
    switch (errorCode) {
      case RongIMLib.ErrorCode.TIMEOUT:
        info = '超时'
        break
      case RongIMLib.ErrorCode.UNKNOWN_ERROR:
        info = '未知错误'
        break
      case RongIMLib.ErrorCode.UNACCEPTABLE_PaROTOCOL_VERSION:
        info = '不可接受的协议版本'
        break
      case RongIMLib.ErrorCode.IDENTIFIER_REJECTED:
        info = 'appkey不正确'
        break
      case RongIMLib.ErrorCode.SERVER_UNAVAILABLE:
        info = '服务器不可用'
        break
    }
    console.log(errorCode, info)
  }
})

/**
 * 发送文本消息
 */
function sendMessage () {
  let msg = new RongIMLib.TextMessage({
    content: 'hello RongCloud! 蓝海天网',
    extra: '附加信息 - TEST'
  })
  let conversationType = RongIMLib.ConversationType.PRIVATE // 私聊,其他会话选择相应的消息类型即可。
  let targetId = '73' // 目标 Id
  RongIMClient.getInstance().sendMessage(conversationType, targetId, msg, {
    onSuccess (message) {
      // message 为发送的消息对象并且包含服务器返回的消息唯一Id和发送消息时间戳
      console.log('Send successfully')
    },
    onError (errorCode, message) {
      let info = ''
      switch (errorCode) {
        case RongIMLib.ErrorCode.TIMEOUT:
          info = '超时'
          break
        case RongIMLib.ErrorCode.UNKNOWN_ERROR:
          info = '未知错误'
          break
        case RongIMLib.ErrorCode.REJECTED_BY_BLACKLIST:
          info = '在黑名单中，无法向对方发送消息'
          break
        case RongIMLib.ErrorCode.NOT_IN_DISCUSSION:
          info = '不在讨论组中'
          break
        case RongIMLib.ErrorCode.NOT_IN_GROUP:
          info = '不在群组中'
          break
        case RongIMLib.ErrorCode.NOT_IN_CHATROOM:
          info = '不在聊天室中'
          break
        default:
          info = 'XX default'
          break
      }
      console.log('发送失败:' + info)
    }
  })
}

window.aa = sendMessage

/**
 * 获取历史消息
 * @param  {String} targetId 想获取自己和谁的历史消息，targetId 赋值为对方的 Id
 * @return {Array}
 */
function getHistoryMessages (targetId = '73') {
  let conversationType = RongIMLib.ConversationType.PRIVATE // 私聊,其他会话选择相应的消息类型即可
  let timestrap = 0 // null // 默认传 null，若从头开始获取历史消息，请赋值为 0 ,timestrap = 0
  let count = 20 // 每次获取的历史消息条数，范围 0-20 条，可以多次获取
  RongIMLib.RongIMClient.getInstance().getHistoryMessages(conversationType, targetId, timestrap, count, {
    /**
     * 获取成功
     * @param  {Array}   list   消息数组
     * @param  {Boolean} hasMsg 是否还有历史消息可以获取
     */
    onSuccess (list, hasMsg) {
      console.log(list, hasMsg)
    },
    onError (error) {
      console.log('GetHistoryMessages,errorcode:' + error)
    }
  })
}

window.bb = getHistoryMessages
