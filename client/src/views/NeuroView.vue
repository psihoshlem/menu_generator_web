<template>
  <HeaderComp :style="style_for_header"/>
  <div class="neuro" >
    <div class="inner">
      <div class="neuro__info">
        <div class="neuro__info-title">
          <h3>Приготовлено <span>нейросетью</span> с ❤️</h3>
          <h1>Бургер - три сыра</h1>
          <div class="neuro__info-title-rating">
            <div>&#9733;</div>
            <div>&#9733;</div>
            <div>&#9733;</div>
            <div>&#9733;</div>
            <div>&#9733;</div>
            <!-- <div class="rating--item" v-for="star in recipe_star" :key="star.id">&#9733;</div> -->
          </div>
          <div>
            <img src="./../img/foodcard_clock.png" alt="">
            <span>~20 мин</span>
          </div>
        </div>
        <div class="neuro__content">
                    <div class="neuro__content-info">
                        <div class="neuro__content-image">
                            <!-- <img :src="img_for_recipe(recipe.picture_url)" alt=""> -->
                        </div>
                        <div class="neuro__composition">
                            <span>Ингредиенты :</span>
                            <div class="neuro__dishes">
                                <!-- <div class="dish" v-for="item in recipe.ingredients" :key="item.id">
                                    <div>{{ item.name }}</div>
                                    <div></div>
                                    <div>{{ output_count(item) }}</div>
                                </div> -->
                            </div>
                        </div>
                    </div>
                    <div class="neuro__description">
                        <div class="neuro__description-null"></div>
                        <div class="neuro__description-text">
                            <span>Описание:</span>
                            <!-- {{  recipe.description }} -->
                        </div>
                    </div>
                </div>
      </div>
      <div class="neuro__steps"></div>
    </div>
  </div>
</template>
<script>
import HeaderComp from '../components/HeaderComp.vue';
export default {
  components: {
    HeaderComp
  },
  data(){
    return{
      style_for_header: {
        color_text: "white",
        brackground_color: "black"
      }
    }
  }
}
</script>
<style lang="scss">
.neuro{
  color: #fff;
  font-family: Montserrat;

  &__info{
    display: flex;
    justify-content: center;
    flex-direction: column;

    &-title{
      display: flex;
      flex-direction: column;
      align-items: center;

      h3{
        margin-top: 56px;
        font-size: 36px;
        font-weight: 800;
        span{
          color: #FFA53C;
          text-decoration: underline;
        }
      }

      h1{
        margin: 30px 0;
        font-size: 40px;
        font-weight: 800;
      }

      & :nth-child(3){
        
      }

      &-rating{
            width: 180px;
            height: 20px;
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

      & :nth-child(4){
        display: flex;
        align-items: center;
        gap: 5px;
        font-size: 20px;
        font-style: italic;
        font-weight: 400;
      }
    }
  }
}
.neuro__content{
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

        .neuro__composition{
            height: 300px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            span{
                font-size: 24px;
                font-weight: 600;
            }

            .neuro__dishes{
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


        .neuro__description{
            margin: 0 auto;
            width: 1300px;
            max-height: 400px;
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
                padding-bottom: 30px;

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
            .neuro__content-image{
                width: 400px;
                height: auto;
            }
            .neuro__content-image img{
                width: 400px;
                height: auto;
            }

        }
}
</style>
