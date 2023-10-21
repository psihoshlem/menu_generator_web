<template>
  <div class="recipe_view">
    <HeaderComp />
        <div class="recipe">
                <div class="recipe__title">
                    <div class="recipe__title-name">
                        <span>Лазанья</span>
                    </div>
                    <div class="recipe__title-rating" data-total-value="4">
                        <div class="rating--item" data-item-value="5">&#9733;</div>
                        <div class="rating--item" data-item-value="4">&#9733;</div>
                        <div class="rating--item" data-item-value="3">&#9733;</div>
                        <div class="rating--item" data-item-value="2">&#9733;</div>
                        <div class="rating--item" data-item-value="1">&#9733;</div>
                    </div>
                    <div class="recipe__title-time">
                        <img src="./../img/recipe_clock.png" alt="">
                        <span>~20:00</span>
                    </div>
                </div>
                <div class="recipe__content">
                    <div class="recipe__content-info">
                        <div class="recipe__content-image">
                            <img src="./../img/recipe_lasagna.jpg" alt="">
                        </div>
                        <div class="recipe__composition">
                            <span>Состав:</span>
                            <div class="recipe__dishes">
                                <div class="dish">
                                    <div>Фарш мясной</div>
                                    <div></div>
                                    <div>800г</div>
                                </div>
                                <div class="dish">
                                    <div>Помидоры</div>
                                    <div></div>
                                    <div>2шт.</div>
                                </div>
                                <div class="dish">
                                    <div>Лук</div>
                                    <div></div>
                                    <div>2шт.</div>
                                </div>
                                <div class="dish">
                                    <div>Листья лазаньи</div>
                                    <div></div>
                                    <div>10шт.</div>
                                </div>
                                <div class="dish">
                                    <div>Чеснок</div>
                                    <div></div>
                                    <div>2шт.</div>
                                </div>
                                <div class="dish">
                                    <div>Томатная паста</div>
                                    <div></div>
                                    <div>2 ст.л</div>
                                </div>
                                <div class="dish">
                                    <div>Твёрдый сыр</div>
                                    <div></div>
                                    <div>100г</div>
                                </div>
                                <div class="dish">
                                    <div>Растительное масло</div>
                                    <div></div>
                                    <div>1ст.л</div>
                                </div>
                                <div class="dish">
                                    <div>Соль</div>
                                    <div></div>
                                    <div>0.5гр</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="recipe__description">
                        <div class="recipe__description-null"></div>
                        <div class="recipe__description-text">
                            <span>Описание:</span>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi ipsam vero ex aliquid dicta eligendi dolorem quam nesciunt, sequi illum, maiores porro doloremque. Facere, dolorem! Expedita tempore doloribus saepe quaerat?
                        </div>
                    </div>
                </div>
        </div>
    </div>
</template>
<script>
import HeaderComp from '../components/HeaderComp.vue';
export default {
  components: {
    HeaderComp
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
            color: #dcdcdc;
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
            height: 260px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            span{
                font-size: 24px;
                font-weight: 600;
            }

            .recipe__dishes{
                width: 540px;
                // height: 200px;
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
            }

            .dish {
                font-size: 16px;
                font-weight: 400;
                width: 250px;
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
            height: 300px;
            background-color: #18274B1F;
            border-radius: 25px;
            display: flex;
            z-index: 0;


            &-null{
                width: 1150px;
            }

            &-text{
                margin-top: 45px;
                margin-right: 62px;
            }

            @media screen and (max-width: 1600px){
                &-null{
                    width: 1350px;
                }
            }
            @media screen and (max-width: 1500px){
                &-null{
                    width: 1560px;
                }
            }
            @media screen and (max-width: 1400px){
                &-null{
                    width: 1750px;
                }
            }
            @media screen and (max-width: 1300px){
                &-null{
                    width: 1850px;
                }
            }
        }

        @media screen and (max-width: 1300px){
            .recipe__content-image{
                width: 300px;
            }
            .recipe__content-image img{
                width: 300px;
            }

        }
    }
}
</style>
