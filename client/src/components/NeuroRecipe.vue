<template>
  <section class="recomendation">
    <div class="inner">
      <div class="recomendation__title">
        <img src="./../img/neuro_want_new.png" alt="">
        <div class="recomendation__title-text">
          <span class="recomendation__title-span1">–– Чего-то необычного?!</span>
          <span class="recomendation__title-span2">–– А вы когда нибудь пробовали...</span>
        </div>
      </div>
      <div class="recomendation__card" v-for="item in recipe_neuro"
      :key="item.id">
      <div class="card__title">
        <img src="./../img/neuro-line.png" alt="">
        {{ item.name }}
      </div>
      <div class="recomendation__desc">
        (🧠 Приготовлено <span>нейросетью</span>)
      </div>
      <div class="card__block">
          <img src="../img/neuro-soup.png" alt="" class="soup">
          <div class="card__desc">
            <span class="card__desc-time">
              <img src="./../img/foodcard_clock.png" alt="">
              ~{{ item.time }} мин
            </span>
            <span class="card__desc-sostav">
              <span>Состав:</span>
              {{ item.compound }}
            </span>
            <p class="card__desc-history">
              <span>Описание:</span>
              {{ item.description }}
            </p>
          </div>
        </div>
      </div>
      <div class="neuro_btn">
        <button @click="go_to_neuro">Подробнее</button>
      </div>
    </div>
  </section>
</template>
<script>
import router from '@/router';

export default {
  data() {
    return {
      recipe_neuro: [{ name: "Бургер - три сыра", time: "20:00", compound: 'Сыр масдам, Помидоры, Сыр пармезан, Сыр твердый, Листья салата, Хлеб, Котлета, Кунжут', description: 'Только настоящий сырный мозг мог создать такой бургер! В его основе лежат три сыра, которые распределены между нежнейшей котлетой, ломтиком помидора, листьями салата. А сверху посыпано кунжутом. Вы точно не останетесь равнодушным!' }],
      focused: false,
      value_input: ''
    }
  },
  methods:{
    go_to_neuro(){
      router.push('/neuro_recipe')
    }
  }
}
</script>
<style lang="scss">
.inner {
  margin: 0 auto;
  max-width: 1600px;
  width: 95%;
}

.recomendation {
  backdrop-filter: blur(5px);

  background: linear-gradient(180deg, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 1%, rgba(255,255,255,0) 99%, rgba(255,255,255,1) 100%);  color: #fff;
  // margin-top: 137px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-top: 32px;
  padding-bottom: 68px;
  // display: none;

  &__title {
    color: #FFF;
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin: 50px 0;

    & img{
      width: 534px;
      height: 35px;
      margin: 0 auto;
      margin-bottom: 25px;
    }

    &-text{
      font-family: Montserrat;
      font-size: 24px;
      font-style: normal;
      font-weight: 600;
      line-height: normal;
      margin: 0 auto;
      width: 1000px;
      display: flex;
      flex-direction: column;

    }
    &-span1{
      text-align: start;
      font-family: Montserrat;
      font-size: 24px;
      font-style: italic;
      font-weight: 300;
    }
    &-span2{
      text-align: end;
      font-family: Montserrat;
      font-size: 24px;
      font-style: italic;
      font-weight: 300;
    }
  }

  &__desc {
    text-align: center;
    margin-top: 6px;
    color: #FFF;
    font-family: Montserrat;
    font-size: 24px;
    font-style: italic;
    font-weight: 300;
    line-height: normal;
    
    span {
      text-decoration: underline;
      color: #FF64E6;
    }
  }
  &__card {
    margin-top: 52px;
  }
}

.card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  
  &__title {
    text-align: center;
    // color: linear-gradient(180deg, rgba(255,129,57,1) 0%, rgba(223,80,0,1) 100%);
    font-family: Montserrat;
    font-size: 48px;
    font-style: normal;
    font-weight: 800;
    line-height: normal;
    color: rgba(255, 129, 57, 1);
    transform: translateX(-40px);
  }
  &__block {
    display: flex;
    flex-direction: row;
    margin-top: 36px;
    color: #FFF;
    font-family: Montserrat;
    font-size: 20px;
    font-style: italic;
    font-weight: 400;
    line-height: normal;
    
    .soup{
      position: absolute;
      transform: translateY(-40px);
    }
  }
  
  &__desc {
    padding: 30px;
    width: 1200px;
    height: 333px;
    margin: 0 auto;
    padding-left: 180px;
    background-color: #ffffff51;
    border-radius: 25px;
    display: flex;
    row-gap: 24px;
    flex-direction: column;

    &-time{
      display: flex;
      flex-direction: row;
      gap: 5px;
    }

    &-sostav{
      display: flex;
      flex-direction: column;
      gap: 10px;

      span{
        font-weight: 800;
      }
    }
    
    &-history{
      display: flex;
      flex-direction: column;
      gap: 10px;
      
      span{
        font-weight: 800;
      }
    }
  }
}
.neuro_btn{
  margin-top: 50px;
  font-family: Montserrat;
  display: flex;
  justify-content: center;
  button{
    background-color: #ff8139;
    padding: 10px 20px;
    border-radius: 25px;
    font-size: 25px;
  }
}

</style>
