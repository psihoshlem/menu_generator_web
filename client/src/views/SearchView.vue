<template>
  <HeaderComp />
  <section class="receptions">
    <div class="inner">
      <div class="receptions__title">{{ msg }}</div>
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

import ShortRecipe from '../components/ShortRecipe.vue';
import HeaderComp from '../components/HeaderComp.vue';
export default {
  components: {
    ShortRecipe,
    HeaderComp
  },
  data() {
    return {
      all_recipes: [],
      msg: ''
    }
  },
  methods: {
    go_to_recipe(item) {
      this.$router.push({ name: 'recipe', params: { item_info: item._id } })
    }
  },
  async created() {
    const queryString = this.$route.query.output_data
    if (queryString){
      const searchItems = JSON.parse(queryString)
      axios.post('http://localhost:8000/recipes',searchItems)
      .then((response) => {
        this.all_recipes = response.data
        if (response.data.length > 0){
          this.msg = "Рецепты по вашему запросу:"
        } else {
          this.msg = "Ничего не найдено"
        }
      })
    } else {
      this.msg = "Перейдите на главную страницу и сделайте запрос..."
    }
  }
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
