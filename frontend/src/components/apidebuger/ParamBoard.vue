<template>
  <div>
    <a-tabs default-active-key="1" @change="callback">
      <a-tab-pane class="innercard" key="Param" tab="Param">
        <a-textarea placeholder="以json结构输入额外的param" :rows="4" />
      </a-tab-pane>
      <a-tab-pane class="innercard" key="Headers" tab="Headers" force-render>
        <a-textarea placeholder="以json结构输入额外的请求头" :rows="4" />
      </a-tab-pane>
      <a-tab-pane class="innercard" key="Data" tab="Data">
        <a-textarea placeholder="以json结构输入额外的data" :rows="4" />
      </a-tab-pane>
    </a-tabs>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  methods: {
    callback(key) {
      console.log(key);
    },
  },
};
</script>

<style>
</style>
