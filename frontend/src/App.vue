<template>
  <div id="page">
    <Layer id="layout"></Layer>
  </div>
</template>

<script>
import Layer from '@/components/Layer.vue'

export default({
  components: {
    Layer,
  },
  data() {
    return {

    }
  },
})
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#page {
  height: 100vh;
}

#layout{
  height: 100vh;
}
</style>
