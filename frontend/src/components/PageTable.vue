<template>
  <a-table :columns="Head" :data-source="data">
    <a slot="action" slot-scope="text" href="javascript:;">Delete</a>
    <p slot="expandedRowRender" slot-scope="record" style="margin: 0">
      {{ record.description }}
    </p>
  </a-table>
</template>
<script>

export default {
  props: {
      data: Array,
      Head: Array 
  }
};
</script>