export default originelList => {

  const list = [...originelList]
  let groups = [], vo

  for (let i in list) {
    vo = Object.assign(list[i], {
      _subs   : [],
      _level  : 0,
      _parents: [],
    })

    if (groups[vo.pid] === undefined) groups[vo.pid] = []
    groups[vo.pid].push(vo)
  }

  const getTreeList = (subGroup, groups, level = 0, parents = []) => {
    let treeList = [], vo, thisSubGroup, subTreeList
    for (let i in subGroup) {
      vo = subGroup[i]
      vo._level   = level                // 嵌套级别（视图缩进）
      vo._subs    = []                   // 所有子ID
      vo._parents = [...parents, vo.pid] // 所有父ID
      treeList.push(vo)

      thisSubGroup = groups[vo.id] || false
      if (thisSubGroup) {
        subTreeList = getTreeList(thisSubGroup, groups, ++level, vo._parents)
        for (let i in subTreeList) {
          vo._subs.push(subTreeList[i].id)
          treeList.push(subTreeList[i])
        }
      }
    }
    return treeList
  }

  return getTreeList(groups[0], groups)
}