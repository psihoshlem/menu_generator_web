<template>
  <router-view></router-view>
  <FooderComp />
</template>
<script>
import FooderComp from './components/FooderComp.vue';
export default {
  components: {
    FooderComp,
  }
}
</script>
<style>
</style>
