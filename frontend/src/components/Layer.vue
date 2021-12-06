<template>
  <a-layout id="components-layout-demo-custom-trigger">
    <a-layout-sider v-model="collapsed" :trigger="null" collapsible>
      <div id="logocontainer">
          APIGW
          <!-- <img alt="ApiGW" id="logo" src="../assets/apigw-logo.png"> -->
      </div>
      <a-menu @click="routerJump" theme="dark" mode="inline" :default-selected-keys="['1']">
        <a-menu-item key="Dashboard">
          <span>Dashboard</span>
        </a-menu-item>
        <a-menu-item key="ApiResource">
          <span>API资源</span>
        </a-menu-item>
        <a-menu-item key="RequestRec">
          <span>请求记录</span>
        </a-menu-item>
        <a-menu-item key="ApiSentry">
          <span>健康监测</span>
        </a-menu-item>
        <a-menu-item key="ApiDebuger">
          <span>API Debuger</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header id="headers" style="background: #fff; padding: 0">
        <div id="appselector">
            应用：
            <a-dropdown>
                <template #overlay>
                    <a-menu @click="handleMenuClick">
                        <a-menu-item v-for="app in applist" :key="app">
                            <UserOutlined />
                            {{app.name}}
                        </a-menu-item>
                    </a-menu>
                </template>
                <a-button>
                    {{currentApp.name}}
                    <DownOutlined />
                </a-button>
            </a-dropdown>
        </div>
      </a-layout-header>
      <a-layout-content
        :style="{ margin: '24px 16px', padding: '24px', background: '#fff', minHeight: '280px' }"
      >
        <router-view></router-view>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>
<script>
import { mapState,mapMutations,mapActions } from 'vuex'
export default {
  name: 'Layer',
  components: {
      
  },
  computed:{
    ...mapState({
      applist: state => state.applist
    }),
  },
  data() {
    return {
      collapsed: false,
      currentApp: {"name":""}
    };
  },
  created() {
    // 拉取应用列表
    this.requestAppList()
  },
  methods: {
    ...mapMutations([
      'setAppList',
      'setCurrentApp',
    ]),
    ...mapActions([
      'getAppList',
    ]),
    // 切换app
    handleMenuClick(current) {
      this.currentApp = current.key
      this.setCurrentApp(current.key)
    },
    // 路由跳转
    routerJump(menuitem) {
        const path = menuitem.key
        this.$router.push(path)
    },
    // 获取应用列表
    async requestAppList() {
      const resp = await this.getAppList()
      this.setAppList(resp)
    }
  }
};
</script>
<style>
#logocontainer {
    width: 100%;
    height:48px;
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    font-size: 16px;
    letter-spacing: 1px;
}
#components-layout-demo-custom-trigger .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: #1890ff;
}

#components-layout-demo-custom-trigger .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}

#headers {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    background-color: #eee;
    text-align: center;
    align-items: center;
}

#appselector{
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 0;
    margin-right: 32px;
}
</style>
