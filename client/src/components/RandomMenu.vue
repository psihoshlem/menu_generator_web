<template>
  <section class="receptions">
    <div class="inner">
      <div class="receptions__title">Посмотрите на эти рецепты:</div>
      <div class="receptions__products">
        <div class="product" v-for="item in all_recipes" :key="item.id">
          <ShortRecipe :recipe='item' @click="go_to_recipe(item)" />
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import axios from 'axios';

import ShortRecipe from './ShortRecipe.vue';
export default {
  components: {
    ShortRecipe
  },
  data() {
    return {
      all_recipes: [],
    }
  },
  methods: {
    go_to_recipe(item) {
      this.$router.push({ name: 'recipe', params: { item_info: item._id } })
    }
  },
  async created() {
    await axios.get('http://localhost:8000/recipes', {
    })
      .then((response) => {
        if (response.status == 200) {
          this.all_recipes = response.data
        }
      })
  },
}
</script>
<style lang="scss">
.inner {
  margin: 0 auto;
  max-width: 1600px;
  // width: 95%;
}

.receptions {
  // display: none;
  background-color: #fff;
  &__products{
    display: flex;
    gap: 30px;
    justify-content: center;
    flex-flow: column wrap;
  }
  
  &__title {
    text-align: center;
    // margin-top: 80px;
    padding-top: 100px;
    color: #000;
    font-family: Montserrat;
    font-size: 36px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
  }
  
  &__products {
    display: flex;
    flex-direction: row;
    margin-top: 55px;
    // column: gap 38px;
    
    .product{
      width: 30%;
      height: 450px;
      margin-bottom: 30px;
    }
    @media screen and (max-width: 1650px){
      .product{
        width: 34%;
      }
    }
    @media screen and (max-width: 1450px){
      .product{
        width: 50%;
      }
    }
  }
}
</style>
