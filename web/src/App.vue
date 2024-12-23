<template>
  <el-container>
    <el-aside width="20%">
      <el-menu :default-active="activeIndex" @select="handleSelect" style="height: 100%">
        <el-menu-item index="/">
          <i class="el-icon-s-home"></i>
          日常对话练习
        </el-menu-item>
        <el-menu-item index="/about">
          <i class="el-icon-s-custom"></i>
          翻译
        </el-menu-item>
      </el-menu>
    </el-aside>

    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: '/',
    };
  },
  methods: {
    handleSelect(index, indexPath) {
      console.log(index)
      this.activeIndex = index;
      this.$router.push(this.activeIndex)
    },
  },
};
</script>

<style>
.el-aside {
  height: 100vh;
}
</style>