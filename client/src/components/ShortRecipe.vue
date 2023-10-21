<template>
  <div class="foodcard" style="background: url('../img/{{ recipe.img }}'))">
    <div class="foodcard__title">
      <div class="foodcard__title-name">
        <span>{{ recipe.name }}</span>
      </div>
      <div class="foodcard__title-rating">
        <div class="rating--item" v-for="star in recipe.grade" :key="star.id">
          &#9733;
        </div>
      </div>
    </div>
    <div class="foodcard__recipe">
      <div class="foodcard__recipe-time">
        <img src="../img/foodcard_clock.png" alt="">
        <span>~{{ recipe.time }}</span>
      </div>
      <div class="foodcard__recipe-composition">
        <span>Состав: {{ recipe.compound }}</span>
      </div>
      <div class="foodcard__recipe-description">
        <span>{{ recipe.description }}</span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ['recipe']
}
</script>
<style lang="scss">
.foodcard {
  background-color: #fff;

  max-width: 584px;
  // max-height: 450px;
  background: url('../img/foodcard_czezar.jpg') no-repeat center center;
  background-size: cover;
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
  color: #ffffff;
  border-radius: 25px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-bottom: 100px;

  .foodcard__title {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    background: linear-gradient(0deg, rgba(255, 255, 255, 0) 0%, rgba(0, 0, 0, 1) 70%);
    border-radius: 25px 25px 0 0;
    padding-bottom: 150px;

    &-name {
      margin-top: 34px;
      font-size: 36px;
      font-weight: 700;
    }

    .foodcard__title-rating {
      width: 180px;
      margin-bottom: 34px;
      display: inline-flex;
      flex-direction: row-reverse;
      justify-content: center;
      cursor: pointer;
      gap: 4px;
    }

    .foodcard__title-rating[data-total-value="1"] .rating--item:nth-child(n + 5),
    .foodcard__title-rating[data-total-value="2"] .rating--item:nth-child(n + 4),
    .foodcard__title-rating[data-total-value="3"] .rating--item:nth-child(n + 3),
    .foodcard__title-rating[data-total-value="4"] .rating--item:nth-child(n + 2),
    .foodcard__title-rating[data-total-value="5"] .rating--item:nth-child(n + 1) {
      color: rgb(255, 196, 0);
    }

    .rating--item {
      font-size: 25px;
      color: #FFC700;
      transition: .2s;
    }

    // .rating--item:hover,
    // .rating--item:hover~.rating--item {
    //   color: #FFC700;
    // }
  }
  
  .foodcard__recipe {
    width: 100%;
    height: 181px;
    padding: 20px;
    backdrop-filter: blur(20px);
    border-radius: 40px 40px 25px 25px;
    display: flex;
    flex-direction: column;
    gap: 15px;
    padding-bottom: 30px;

    .foodcard__recipe-time {
      display: flex;
      align-items: center;
      gap: 5px;
      font-size: 16px;
      font-weight: 300;
      font-style: italic;
    }

    .foodcard__recipe-composition {
      display: flex;
      align-items: center;
      font-size: 16px;
      font-weight: 300;
      font-style: italic;
    }

    .foodcard__recipe-description {
      display: flex;
      align-items: center;
      font-size: 16px;
      font-weight: 500;
    }
  }
}
</style>
