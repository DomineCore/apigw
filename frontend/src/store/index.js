import { createStore } from 'vuex'
import http from '@/api/http'
import modules from './namespace'

export default createStore({
  state: {
    applist: [],
    // 当前选中的app
    currentapp: null,
  },
  mutations: {
    // 设置应用列表
    setAppList(state, applist) {
      state.applist = applist
    },
    // 修改当前选中的app
    setCurrentApp(state, app) {
      state.currentapp = app
    }
  },
  actions: {
    // 获取应用列表
    getAppList() {
      return http.get('/api/v1/app/').then(response => response)
    }
  },
  modules: modules
})
