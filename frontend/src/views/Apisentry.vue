<template>
    <div id="apiresourcepage">
        <div id="top">
            <div id="topleft">
                <span id="title">ApiSentry</span>
            </div>
        </div>
        <a-alert
          v-if="warning"
          message="Warning"
          description="请先选择应用"
          type="warning"
          closable
          :after-close="closeWarning"
          show-icon
        />
        <a-divider></a-divider>
        <div id="filters">
            <div id="filterscontainer" v-if="currentapp">
                应用："{{currentapp.name}}"下API的异常记录
            </div>
            <div id="filterscontainer" v-else>
                请选择应用
            </div>
            <a-button @click="refresh" :loading="refresh_load" :size="size">刷新</a-button>
        </div>
        <a-divider></a-divider>
        <div id="datas">
            <a-table @change="checkPage" :pagination="pagination" :columns="columns" :data-source="data">
                <template #headerCell="{ column }">
                    <template v-if="column.key === 'name'">
                        <span>
                        {{column.name}}
                        </span>
                    </template>
                    <template v-else>
                        <span>
                        {{column.name}}
                        </span>
                    </template>
                </template>

                <template #bodyCell="{ column, record }">
                <template v-if="column.key === 'name'">
                    <a>
                    {{ record.name }}
                    </a>
                </template>
                <template v-else-if="column.key === 'action'">
                    <span @click=showDetail(record)>
                    <a>异常详情</a>
                    </span>
                </template>
                </template>
            </a-table>
        </div>
        <CreateApiModel ref="CreateApiModel"></CreateApiModel>
        <DetailPanel ref="detail" :title="调用详情">
          <p><b>异常ID：</b><br />{{current_apisentry.id}}</p>
          <a-divider></a-divider>
          <p><b>API-ID：</b><br />{{current_apisentry.api}}</p>
          <a-divider></a-divider>
          <p><b>API名称：</b><br />{{current_apisentry.name}}</p>
          <a-divider></a-divider>
          <p><b>Traceback：</b><br />{{current_apisentry.trace_msg}}</p>
          <a-divider></a-divider>
          <p><b>异常发生时间：</b><br />{{current_apisentry.create_time}}</p>
          <a-divider></a-divider>
        </DetailPanel>
    </div>
</template>

<script>
const columns = [
{
  name: 'API',
  dataIndex: 'name',
  key: 'name',
},
{
  name: '异常发生时间',
  dataIndex: 'create_time',
  key: 'create_time',
},
{
  name: 'Action',
  key: 'action',
}
];
import { mapActions, mapState } from 'vuex'
import CreateApiModel from '@/components/apiresource/CreateApi'
import DetailPanel from '@/components/DetailPanel'
export default({
    name:'ApiSentry',
    components: {
        CreateApiModel,
        DetailPanel
    },
    setup() {
      return {
      columns,
    };
  },
  data(){
      return {
        data:[],
        checked_get: false,
        checked_post: false,
        // 刷新按钮loading
        refresh_load: false,
        // 显示选择应用warning
        warning: false,
        // 分页器
        pagination: {}
      }
  },
  computed: {
    ...mapState({
        currentapp: state => state.currentapp
    })
  },
  created(){
      this.requestApiSentry()
  },
  watch:{
    currentapp(val) {
        this.requestApiSentry()
    }
  },
  methods:{
      ...mapActions('apisentry',[
          'loadApiSentry'
      ]),
      async requestApiSentry(limit=10, offset=0) {
          if(!this.currentapp){
            return
          }
          const params = {
              "sys":this.currentapp.app_id,
              "limit":limit,
              "offset":offset
          }
          const response = await this.loadApiSentry(params)
          this.data = response.results
          this.pagination.total = response.count
          this.pagination.pageSize = limit
      },
      // 切换分页
      async checkPage (pageinfo) {
        const limit = pageinfo.pageSize
        const offset = (pageinfo.current-1) * limit
        this.requestApiSentry(limit,offset)
      },
      // 刷新数据
      refresh() {
        //添加loading
        try{
          this.refresh_load = true
          this.requestApiSentry()
          this.refresh_load = false
        } catch(err) {
          this.refresh_load = false
        }
      },
      closeWarning() {
        this.warning = false
      },
      // 展示详情
      showDetail (record) {
        this.current_apisentry = record
        this.$refs.detail.show()
      }
  }
})
</script>

<style>
    #top{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    #topleft{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    #title{
        font-size: 36px;
    }
    .filteritem{
        display: flex;
        flex-direction: row;
    }
    #filters{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
    }
</style>
