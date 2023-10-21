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
import ShortRecipe from './ShortRecipe.vue';
export default {
  components: {
    ShortRecipe
  },
  data() {
    return {
      all_recipes: [
        {
          id: 0,
          name: "Салат цезарь",
          time: "20:00",
          compound: 'Оливковое масло, Лимонный сок, Помидоры, Яица, Салат, Сухарики, Сыр, Помидоры',
          description: 'Классический рецепт «Цезаря» – это листовой салат Романо, кусочки обжаренного хлеба, тертый сыр пармезан и особая заправка из желтков...',
          img: "foodcard_czezar.jpg",
          grade: 4
        },
        {
          id: 1,
          name: "Салат цезарь",
          time: "20:00",
          compound: 'Оливковое масло, Лимонный сок, Помидоры, Яица, Салат, Сухарики, Сыр, Помидоры',
          description: 'Классический рецепт «Цезаря» – это листовой салат Романо, кусочки обжаренного хлеба, тертый сыр пармезан и особая заправка из желтков...',
          img: "foodcard_czezar.jpg",
          grade: 5
        },
        {
          id: 2,
          name: "Салат цезарь",
          time: "20:00",
          compound: 'Оливковое масло, Лимонный сок, Помидоры, Яица, Салат, Сухарики, Сыр, Помидоры',
          description: 'Классический рецепт «Цезаря» – это листовой салат Романо, кусочки обжаренного хлеба, тертый сыр пармезан и особая заправка из желтков...',
          img: "foodcard_czezar.jpg",
          grade: 1
        }
      ],
    }
  },
  methods: {
    go_to_recipe(item) {
      this.$router.push({ name: 'recipe', params: { item_info: item.id } })
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
  }
}
</style>
