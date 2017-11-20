# vue-alertify

- 简化 element 消息组件的调用方式

---

## 实际用例

### 模态提示框

```js
this.$alert([title], message, [option], [callback])

this.$alert('模态提示框')
this.$alert('模态提示框', () => {})
```

### 模态选择框

```js
this.$confirm([title], message, [option], [onOk], [onCancel])

this.$confirm('模态选择框', () => {
  this.$message('消息提示 ok')
}, () => {
  this.$message('消息提示 cancel')
})
```

### 消息提示

```js
this.$error('错误')
this.$success('成功')
this.$message('消息')
this.$warning('警告')
```

### 消息通知

```js
this.$$error([title], message)

this.$$error('错误')
this.$$success('成功')
this.$$message('消息')
this.$$warning('警告')
```
