<template>
  <div>
    <a-modal
      v-model:visible="visible"
      title="API接入"
      :confirm-loading="confirmLoading"
      @ok="handleOk"
    >
      <a-form
        ref="formRef"
        :model="formState"
        :rules="rules"
        :label-col="labelCol"
        :wrapper-col="wrapperCol"
      >
        <a-form-item ref="name" required label="API名称" name="name">
          <a-input v-model:value="formState.name" />
        </a-form-item>
        <!-- <a-form-item label="所属应用" required name="from_sys">
          <a-select v-model:value="formState.from_sys" placeholder="请选择应用">
            <a-select-option
              v-for="option in applist"
              :key="option"
              :value="option.app_id"
              >{{ option.name }}</a-select-option
            >
          </a-select>
        </a-form-item> -->
        <a-form-item label="请求方法" required name="method">
          <a-select
            v-model:value="formState.method"
            placeholder="请选择请求方法"
          >
            <a-select-option
              v-for="option in supportMethods"
              :key="option"
              :value="option"
              >{{ option }}</a-select-option
            >
          </a-select>
        </a-form-item>
        <a-form-item
          ref="origin_url"
          required
          label="原始URL"
          name="origin_url"
        >
          <a-input v-model:value="formState.origin_url" />
        </a-form-item>
        <a-form-item ref="apigw_url" required label="网关URL" name="origin_url">
          <a-input v-model:value="formState.apigw_url" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>
<script>
import { defineComponent, reactive, ref } from "vue";
import { mapActions, mapState } from "vuex";
export default defineComponent({
  name: "CreateApiModel",
  setup() {
    const visible = ref(false);
    const showModal = () => {
      visible.value = true;
    };
    const hideModal = () => {
        visible.value = false;
    }
    return {
      visible,
      showModal,
      hideModal,
      labelCol: {
        span: 4,
      },
      wrapperCol: {
        span: 14,
      },
      other: "",
    };
  },
  data() {
    return {
      supportMethods: ["GET", "POST"],
      confirmLoading: false,
      rules: {
        name: [
          {
            required: true,
            message: "请输入api名称",
            trigger: "blur",
          },
          {
            min: 3,
            max: 20,
            message: "长度3-20位",
            trigger: "blur",
          },
        ],
        origin_url: [
          {
            required: true,
            message: "请输入原系统API请求url",
            trigger: "change",
          },
        ],
        apigw_url: [
          {
            required: true,
            message: "请输入网关URL",
            trigger: "change",
          },
        ],
        method: [
          {
            required: true,
            message: "请选择请求方法",
            trigger: "change",
          },
        ],
        from_sys: [
          {
            type: "number",
            required: true,
            message: "请选择API所属应用",
            trigger: "change",
          },
        ],
      },
      formState: reactive({
        name: undefined,
        origin_url: undefined,
        apigw_url: undefined,
        from_sys: undefined,
        method: undefined,
      }),
    };
  },
  computed: {
      formRef(){
          return ref();
      },
    ...mapState({
      currentapp: (state) => state.currentapp,
      applist: (state) => state.applist,
    }),
  },
  methods: {
    ...mapActions("apiresource", ["createApiResource"]),
    async onSubmit() {
        // 注入app
    console.log(this.currentapp)
    this.formState.from_sys = this.currentapp.app_id;
    this.$refs.formRef
        .validate()
        .then(() => {
            try{
                this.createApiResource(this.formState)
                this.hideModal()
            } catch (err) {
                // 展示错误
            }
            
        })
        .catch((error) => {});
    },
    handleOk() {
      this.onSubmit();
      this.confirmLoading = true;
      setTimeout(() => {
        this.confirmLoading = false;
      }, 2000);
    },
    resetForm() {
      this.formRef.value.resetFields();
    },
  },
});
</script>