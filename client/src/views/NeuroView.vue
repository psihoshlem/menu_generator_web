<template>
  <HeaderComp :back_color="color"/>
</template>
<script>
import HeaderComp from '../components/HeaderComp.vue';
export default {
  components: {
    HeaderComp
  },
  data(){
    return{
      color: "black"
    }
  }
}
</script>
<style lang="scss">
</style>
