<template>
  <div>
    <a-drawer
      :title="title"
      :placement="placement"
      :closable="false"
      :visible="visible"
      @close="onClose"
    >
      <slot></slot>
    </a-drawer>
  </div>
</template>
<script>
export default {
  data() {
    return {
      visible: false,
      placement: 'left',
    };
  },
  props:{
    title: String,
  },
  methods: {
    show() {
      this.visible = true;
    },
    onClose() {
      this.visible = false;
    },
    onChange(e) {
      this.placement = e.target.value;
    },
  },
};
</script>
