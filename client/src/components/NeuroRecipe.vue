<template>
  <section class="recomendation">
    <div class="inner">
      <div class="recomendation__title">
        Хотите чего то нового?
      </div>
      <div class="recomendation__desc">
        Посмотрите что приготовила для вас наша <span>нейросеть</span>:
      </div>
      <div class="recomendation__card" v-for="item in recipe_neuro"
        :key="item.id">
        <div class="card__title">
          {{ item.name }}
        </div>
        <div class="card__block">
          <img src="../img/burger.png" alt="" class="card__img">
          <div class="card__desc">
            <span class="card__desc--time">
              ~{{ item.time }}
            </span>
            Состав
            <span class="card__desc--sostav">
              {{ item.compound }}
            </span>
            Описание
            <p class="card__desc--history">
              {{ item.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  data() {
    return {
      recipe_neuro: [{ name: "Бургер - три сыра", time: "20:00", compound: 'Сыр масдам, Помидоры, Сыр пармезан, Сыр твердый, Листья салата, Хлеб, Котлета, Кунжут', description: 'Только настоящий сырный мозг мог создать такой бургер! В его основе лежат три сыра, которые распределены между нежнейшей котлетой, ломтиком помидора, листьями салата. А сверху посыпано кунжутом. Вы точно не останетесь равнодушным!' }],
      focused: false,
      value_input: ''
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

  background-color: #000;
  color: #fff;
  margin-top: 137px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-top: 32px;
  padding-bottom: 68px;
  // display: none;

  &__title {
    text-align: center;
    color: #FFF;
    font-family: Montserrat;
    font-size: 24px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
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
      color: #FF8139
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
    color: #FFF;
    font-family: Montserrat;
    font-size: 32px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
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
  }

  &__desc {
    display: flex;
    row-gap: 24px;
    flex-direction: column;
  }
}
</style>
