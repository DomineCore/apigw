<template>
    <div id="apiresourcepage">
        <div id="top">
            <div id="topleft">
                <span id="title">API Resource</span>
            </div>
            <div id="topright">
                <a-button @click="CreateApi" type="primary" shape="round" :size="size">
                    <template #icon>
                    <plus-circle-filled />
                    接入API
                    </template>
                </a-button>
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
                您在应用："{{currentapp.name}}"注册的API
            </div>
            <div id="filterscontainer" v-else>
                请选择应用
            </div>
            <a-button @click="refresh" :loading="refresh_load" :size="size">刷新</a-button>
        </div>
        <a-divider></a-divider>
        <div id="datas">
            <a-table :columns="columns" :data-source="data">
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
                    <span>
                    <a>调用文档</a>
                    </span>
                </template>
                </template>
            </a-table>
        </div>
        <CreateApiModel ref="CreateApiModel"></CreateApiModel>
    </div>
</template>

<script>
const columns = [
{
  name: 'Name',
  dataIndex: 'name',
  key: 'name',
},
{
  name: 'Url',
  dataIndex: 'apigw_url',
  key: 'apigw_url',
},
{
  name: '请求方法',
  dataIndex: 'method',
  key: 'method',
  filters: [{
    text: 'GET',
    value: 'GET',
  },
  {
    text: 'POST',
    value: 'POST',
  }],
  onFilter: (value, record) => record.method.includes(value),
},
{
  name: '所属应用',
  dataIndex: 'from_sys',
  key: 'from_sys',
},
{
  name: '原始url',
  dataIndex: 'origin_url',
  key: 'origin_url',
},
{
  name: 'Action',
  key: 'action',
}
];
import { mapActions, mapState } from 'vuex'
import CreateApiModel from '@/components/apiresource/CreateApi'
export default({
    name:'ApiResource',
    components: {
        CreateApiModel
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
        warning: false
      }
  },
  computed: {
    ...mapState({
        currentapp: state => state.currentapp
    })
  },
  created(){
      this.requestApiResource()
  },
  watch:{
    currentapp(val) {
        this.requestApiResource()
    }
  },
  methods:{
      ...mapActions('apiresource',[
          'loadApiResource'
      ]),
      async requestApiResource() {
          // default sys
          let sys = 1
          if(this.currentapp){
            sys = this.currentapp.id
          }
          const params = {
              "from_sys":sys
          }
          const response = await this.loadApiResource(params)
          this.data = response
      },
      // 刷新数据
      refresh() {
        //添加loading
        try{
          this.refresh_load = true
          this.requestApiResource()
          this.refresh_load = false
        } catch(err) {
          this.refresh_load = false
        }
      },
      // 接入网关api
      CreateApi() {
          // 检测是否选择应用
          if(this.currentapp){
            this.$refs.CreateApiModel.showModal()
          } else {
            this.warning = true
          }
      },
      closeWarning() {
        this.warning = false
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
