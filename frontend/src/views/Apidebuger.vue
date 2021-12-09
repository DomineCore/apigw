<template>
    <div id="apiresourcepage">
        <div id="top">
            <div id="topleft">
                <span id="title">ApiDebuger</span>
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
                api选择器
            </div>
            <div id="filterscontainer" v-else>
                请选择应用
            </div>
        </div>
        <a-divider>Request</a-divider>
        <div id="requestBoard">
            <div id="paramBar">
                <ParamBoard></ParamBoard>
            </div>
            <div id="paramBtnBar">
                <a-button size="large" type="ghost">RESET</a-button>
                <a-divider style="height:100%;" type="vertical"></a-divider>
                <a-button type="primary" size="large">SEND</a-button>
            </div>
        </div>
        <a-divider>Response</a-divider>
        <div id="responseBoard">
            <a-card id="responseCard">
                请先发起请求
            </a-card>
        </div>
    </div>
</template>

<script>

import { mapActions, mapState } from 'vuex'
import ParamBoard from '@/components/apidebuger/ParamBoard.vue'
export default({
    name:'ApiDebuger',
    components:{
        ParamBoard
    },
    setup() {
      return {
    };
  },
  data(){
      return {
        data:[],
        checked_get: false,
        checked_post: false,
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
      async requestApiSentry() {
          // default sys
          let sys = 1
          if(this.currentapp){
            sys = this.currentapp.id
          }
          const params = {
              "sys":sys
          }
          const response = await this.loadApiSentry(params)
          this.data = response
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
    #requestBoard{
        /* background-color: #eee; */
        width:100%;
        /* background-color: #eee; */
        display: flex;
        flex-direction: column;
        justify-content:space-between;
        height:18vh;
        align-items: flex-end;
    }
    #paramBar{
        width: 100%;
    }
    #paramBtnBar{
        width: 100%;
        display: flex;
        justify-content: flex-end;
        flex-direction:row;
    }
    #responseBoard{
        background-color: #eee;
        width: 100%;
    }
    #responseCard{
        height: 30vh;
        /* background-color: #eee; */
        width: 100%;
    }
</style>
