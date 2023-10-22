<template>
  <HeaderComp />
  <RecipesFinder />
  <NeuroRecipe />
  <RandomMenu />
</template>
<script>
import HeaderComp from '../components/HeaderComp.vue';
import RecipesFinder from '../components/RecipesFinder.vue';
import NeuroRecipe from '../components/NeuroRecipe.vue';
import RandomMenu from '../components/RandomMenu.vue';
export default {
  components: {
    NeuroRecipe,
    RecipesFinder,
    RandomMenu,
    HeaderComp
  }
}
</script>
<style lang="scss">

</style>
