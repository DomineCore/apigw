import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard'
import ApiResource from '@/views/Apiresource'
import ApiSentry from '@/views/Apisentry'
import RequestRec from '@/views/Requestrec'
import ApiDebuger from '@/views/Apidebuger'

const routes = [
  // 工作台
  {
    path: '',
    component:Dashboard,
    name: 'Dashboard',
    alias: '/Dashboard/'
  },
  // api资源
  {
    path: '/apiresource/',
    component:ApiResource,
    name: 'ApiResource'
  },
  // api健康监测
  {
    path: '/apisentry/',
    component:ApiSentry,
    name: 'ApiSentry'
  },
  // 请求记录
  {
    path: '/requestrec/',
    component:RequestRec,
    name: 'RequestRec'
  },
  // api-debuger-panel
  {
    path: '/apidebuger/',
    component:ApiDebuger,
    name: 'ApiDebuger'
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
