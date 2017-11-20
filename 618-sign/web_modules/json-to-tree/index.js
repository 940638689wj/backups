module.exports = function (json) {

  return {

    json   : json,
    groups : [],
    lists  : [],

    getGroups : function (callback) {
      this.generateGroup(callback);
      return this.groups;
    },

    generateGroup : function (callback) {
      for (var i in this.json) {

        var vo = typeof callback === 'function'
          ? callback(this.json[i])
          : this.json[i];

        if (this.groups[vo.pid]) {
          this.groups[vo.pid].push(vo);
        }
        else {
          this.groups[vo.pid] = [];
          this.groups[vo.pid].push(vo);
        }

      }
    },

    getLists : function (callback) {
      for (var i in this.json) {

        var vo = typeof callback === 'function'
          ? callback(this.json[i])
          : this.json[i];

        this.lists[vo.id] = vo;
      }
      return this.lists;
    }

  };
};