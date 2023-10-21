<template>
  <div class="wrapper">
    <div class="recipe">
      <div class="recipe__title">
        <div class="recipe__title-name">
          <span>Лазанья {{ $route.params.item_info }}</span>
        </div>
        <div class="recipe__title-rating" data-total-value="4">
          <div class="rating--item" data-item-value="5">&#9733;</div>
          <div class="rating--item" data-item-value="4">&#9733;</div>
          <div class="rating--item" data-item-value="3">&#9733;</div>
          <div class="rating--item" data-item-value="2">&#9733;</div>
          <div class="rating--item" data-item-value="1">&#9733;</div>
        </div>
        <div class="recipe__title-time">
          <img src="../img/recipe_clock.png" alt="">
          <span>~20:00</span>
        </div>
      </div>
      <div class="recipe__content">
        <div class="recipe__content-descript">
          <div class="recipe__content-image">
            <img src="../img/recipe_lasagna.jpg" alt="">
          </div>
          <div class="recipe__composition">
            <span>Состав:</span>
            <li>Яблоко.............5шт.</li>
            <li>Яблоко.............5шт.</li>
            <li>Яблоко.............5шт.</li>
            <li>Яблоко.............5шт.</li>
            <li>Яблоко.............5шт.</li>
            <div class="recipe__description-text">
              <span>Описание:</span>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi
              ipsam vero ex aliquid dicta eligendi dolorem quam nesciunt, sequi
              illum, maiores porro doloremque. Facere, dolorem! Expedita tempore
              doloribus saepe quaerat?
            </div>
          </div>
        </div>
        <div class="recipe__description">
          <div class="recipe__description-null"></div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
</script>
<style lang="scss">
.recipe {
  margin: 0 auto;
  max-width: 1600px;
  font-family: 'Montserrat', sans-serif;
  padding-top: 100px;

  .recipe__title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    &-name {
      font-size: 40px;
      font-weight: 800;
      letter-spacing: 2px;
    }

    &-time {
      display: flex;
      align-items: center;
      gap: 5px;
      font-weight: 400px;
      font-size: 20px;
      font-style: italic;
    }

    &-rating {
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
    &-rating[data-total-value="5"] .rating--item:nth-child(n + 1) {
      color: rgb(255, 196, 0);
    }

    .rating--item {
      font-size: 25px;
      color: #dcdcdc;
      transition: .2s;
    }

    .rating--item:hover,
    .rating--item:hover~.rating--item {
      color: #FFC700;
    }
  }

  .recipe__content {
    margin-top: 30px;
    display: flex;
    flex-direction: column;

    &-descript {
      display: flex;
      flex-direction: row;
      gap: 35px;
    }

    &-image {
      z-index: 1;
      min-width: 580px;
      min-height: 200px;
    }

    &-image img {
      width: 580px;
      height: 450px;
      position: absolute;
      border-radius: 25px;
    }

    .recipe__description {
      margin: 0 auto;
      width: 1300px;
      height: 300px;
      background-color: #18274B1F;
      border-radius: 25px;
      display: flex;
      z-index: 0;


      &-null {
        width: 1000px;
      }

      &-text {}
    }
  }
}
</style>
