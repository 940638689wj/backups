<template>
  <el-row class="tac">
    <el-menu :default-active="nginxMenuIndex" @select="changeMenu">
      <div class="nav-height">
        <el-menu-item index="1"><i class="el-icon-document"></i>更新项目</el-menu-item>
        <el-menu-item index="2"><i class="el-icon-setting"></i>编辑nginx配置</el-menu-item>
        <!-- <el-submenu index="3">
          <template slot="title"><i class="el-icon-delete2"></i>zzzZZZ...</template>
          <el-menu-item-group>
            <template slot="title">一组~zzzZZZ...</template>
            <el-menu-item index="3-1">zzzZZZ...</el-menu-item>
            <el-menu-item index="3-2">zzzZZZ...</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="二组~分组2">
            <el-menu-item index="3-3">zzzZZZ...</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="3-4">
            <template slot="title">zzzZZZ...</template>
            <el-menu-item index="3-4-1">zzzZZZ...</el-menu-item>
          </el-submenu>
        </el-submenu> -->
      </div>
    </el-menu>
  </el-row>
</template>

<script>
export default{
  name: 'Nav',
  computed: {
    nginxMenuIndex () {
      return this.$store.state.nginxMenuIndex
    }
  },
  methods: {
    changeMenu (key) {
      this.$store.commit('setNginxMenuIndex', key)
    }
  }
}
</script>

<style scope>

</style>
