<template>
  <div class="recipe_view">
    <HeaderComp />
        <div class="recipe">
                <div class="recipe__title">
                    <div class="recipe__title-name">
                        <span>{{  recipe.title }}</span>
                    </div>
                    <div class="recipe__title-rating">
                        <div class="rating--item" v-for="star in recipe_star" :key="star.id">&#9733;</div>
                    </div>
                    <div class="recipe__title-time">
                        <img src="./../img/recipe_clock.png" alt="">
                        <span>~{{  recipe.cooking_time }} мин</span>
                    </div>
                </div>
                <div class="recipe__content">
                    <div class="recipe__content-info">
                        <div class="recipe__content-image">
                            <img :src="img_for_recipe(recipe.picture_url)" alt="">
                        </div>
                        <div class="recipe__composition">
                            <span>Ингредиенты :</span>
                            <div class="recipe__dishes">
                                <div class="dish" v-for="item in recipe.ingredients" :key="item.id">
                                    <div>{{ item.name }}</div>
                                    <div></div>
                                    <div>{{ output_count(item) }}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="recipe__description">
                        <div class="recipe__description-null"></div>
                        <div class="recipe__description-text">
                            <span>Описание:</span>
                            {{  recipe.description }}
                        </div>
                    </div>
                </div>
                <div class="cook">
                  <div class="cook__title">
                      Способы приготовления
                  </div>
                  <div class="steps" v-for="(item, index) in recipe.recipe_instructions" :key="index">
                      <div class="step">
                          <div class="step__img"><img :src="img_for_recipe(item.img)" alt=""></div>
                          <div class="step__desc">
                              <div class="step__desc--counter">Шаг {{index + 1}}</div>
                              <div class="step__desc--instruct">
                                {{ item.text }}
                              </div>
                              <div class="bg"></div>
                          </div>
                      </div>
                  </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';

import HeaderComp from '../components/HeaderComp.vue';
export default {
  components: {
    HeaderComp
  },
  data(){
    return{
        recipe: {},
        recipe_star: 0
    }
  },
  async created() {
    await axios.get('http://localhost:8000/recipes/' +this.$route.params.item_info, {})
      .then((response) => {
        if (response.status == 200) {
            this.recipe = response.data
            this.recipe_star = this.recipe["number of servings"]
        }
      })
  },
  methods:{
    img_for_recipe(picture_url) {
        if (picture_url) {
            let name_picture = picture_url.split("/")[4];
            return "http://127.0.0.1:8000/pics/" + name_picture;
        } else {
            return "";
        }
    },
    output_count(item){
        if (item.count == 0){
            return item.unit
        } else {
            return item.count + item.unit
        }
    }
  }
}
</script>
<style lang="scss">
.recipe_view{
  background-color: #fff;
}

.recipe{
    margin: 0 auto;
    max-width: 1600px;
    font-family: 'Montserrat', sans-serif;
    padding-top: 100px;

    .recipe__title{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        &-name{
            font-size: 40px;
            font-weight: 800;
            letter-spacing: 2px;
        }

        &-time{
            display: flex;
            align-items: center;
            gap: 5px;
            font-weight: 400px;
            font-size: 20px;
            font-style: italic;
        }

        &-rating{
            width: 180px;
            margin-bottom: 22px;
            display: inline-flex;
            flex-direction: row-reverse;
            justify-content: center;
            cursor: pointer;
            gap: 4px;
        }
        &-rating[data-total-value="1"] .rating--item:nth-child(n + 5),
        &-rating[data-total-value="2"] .rating--item:nth-child(n + 4),
        &-rating[data-total-value="3"] .rating--item:nth-child(n + 3),
        &-rating[data-total-value="4"] .rating--item:nth-child(n + 2),
        &-rating[data-total-value="5"] .rating--item:nth-child(n + 1){
            color: rgb(255, 196, 0);
        }

        .rating--item{
            font-size: 25px;
            color: #FFC700;
            transition: .2s;
        }

        .rating--item:hover,
        .rating--item:hover ~ .rating--item{
            color: #FFC700;
        }
    }

    .recipe__content{
        margin-top: 30px;
        display: flex;
        flex-direction: column;

        &-info{
            display: flex;
            flex-direction: row;
            gap: 35px;

        }

        &-image{
            z-index: 1;
            width: 580px;
            height: 200px;
        }
        &-image img{
            width: 580px;
            height: 450px;
            position: absolute;
            border-radius: 25px;
        }

        .recipe__composition{
            height: 300px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            span{
                font-size: 24px;
                font-weight: 600;
            }

            .recipe__dishes{
                width: 850px;
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
            }

            .dish {
                font-size: 16px;
                font-weight: 400;
                width: 400px;
                height: 20px;
                display: flex;
                justify-content: space-between;
            }

            .dish div:nth-child(2){
                flex: 1 0;
                border-bottom: 1px dotted #000;
                height: 1em;
                margin: 0 .4em;
            }
        }


        .recipe__description{
            margin: 0 auto;
            width: 1300px;
            height: 400px;
            background-color: #18274B1F;
            border-radius: 25px;
            display: flex;
            z-index: 0;


            &-null{
                width: 500px;
            }

            &-text{
                width: 800px;
                margin-top: 45px;
                margin-right: 62px;
                margin-left: 20px;
                font-size: 20px;
                font-weight: 500;
                display: flex;
                flex-direction: column;
                gap: 20px;

                span{
                    font-weight: 800;
                    font-size: 25px;
                }
            }

            @media screen and (max-width: 1600px){
                &-null{
                    width: 500px;
                }
            }
            @media screen and (max-width: 1550px){
                &-null{
                    width: 550px;
                }
            }
            @media screen and (max-width: 1450px){
                &-null{
                    width: 650px;
                }
            }
            @media screen and (max-width: 1350px){
                &-null{
                    width: 750px;
                }
            }
        }

        @media screen and (max-width: 1300px){
            .recipe__content-image{
                width: 400px;
                height: auto;
            }
            .recipe__content-image img{
                width: 400px;
                height: auto;
            }

        }
    }

    .cook{
    display: flex;
    flex-direction: column;
    margin-top: 68px;
    &__title{
        text-align: center;
        color: #000;
        font-family: Montserrat;
        font-size: 36px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
    }
}
.steps{
    margin-top: 30px;
    display: flex;
    flex-direction: column;
    row-gap: 25px;
}
.step{
    margin: 50px auto;
    width: 1200px;
    // height: 272px;
    display: flex;
    flex-direction: row;
    gap: 24px;
    position: relative;
    border-radius: 40px;
    background:#18274B1F;
    // box-shadow: 0px 8px 18px -6px rgba(24, 39, 75, 0.12);
    backdrop-filter: blur(20px);
    padding: 40px;
    &__img{
        
        img{
            max-width: 350px;
            border-radius:20px;
            transform: translateZ();
        }
    }
    &__desc{
        display: flex;
        flex-direction: column;
        margin-top: 15px; 
        &--counter{
            color: #000;
            font-family: Montserrat;
            font-size: 40px;
            font-style: italic;
            font-weight: 900;
            line-height: normal;
        }
        &--instruct{
            color: #3F3F3F;
            margin-top: 30px;
            font-family: Montserrat;
            font-size: 20px;
            font-style: italic;
            font-weight: 800;
            line-height: normal;
        }
    }
    .bg{
        position: absolute;
    }
}
}
</style>
