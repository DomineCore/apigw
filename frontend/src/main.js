import { createApp } from 'vue'
import App from './App.vue'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
// 剪贴板复制
import VueClipboard from 'vue-clipboard2'
import router from './router'
import store from './store'

const app = createApp(App);
app.use(store).use(router).use(Antd).use(VueClipboard).mount('#app')
