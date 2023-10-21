<template>
  <div class="finder">
    <div class="inner">
      <div class="search">
        <div class="search__view">
          <img src="./../img/main-man-logo.png" alt="">
          <input type="text" class="search__input"
            placeholder="Давайте найдем что то вкусное" @focus="focused = true"
            v-model="value_input"
            @input="test()"
          >
        </div>
        <span v-if="focused" class="modal"></span>
        <div class="search__block" v-if="focused" @focus="focused = true">
          <div class="search__products">
            <a href="" v-for="item in search_product" :key="item.id">
              <span class="product">
                {{ item.name }}
              </span>
            </a>
          </div>
          <div>
            включить продукты
            <input v-model="input_add_product" v-on:keyup.enter="add_product(input_add_product)">
            <button @click="add_product(input_add_product)">добавить</button>
            добавлено: <span v-for="item in added_products" :key="item.id">{{ item }}</span>
          </div>
          <div>
            исключить продукты
            <input v-model="input_exclude_product" v-on:keyup.enter="exclude_product(input_exclude_product)">
            <button @click="exclude_product(input_exclude_product)">исключить</button>
            исключено: <span v-for="item in excluded_products" :key="item.id">{{ item }}</span>
          </div>
          <div class="search__time-block" @blur="focused = false">
            <div class="time__title">Параметры поиска</div>
            <div class="time__desc">Время готовки в минутах:</div>
            <div class="time__slide slidecontainer">
              <input type="range" name="participants" min="0" max="120" value="20">
              <span class="rangeslider__tooltip" id="range-tooltip"></span>
            </div>
          </div>
          <div class="search__grade">
            Рейтинг
            <div class="search__grade-block">
              <label for="grade">Звезд</label>
              <input type="number" max="5" value="0">
            </div>
          </div>
          <div class="search__block--btn btn" @click="focused = false">Поиск</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      search_product: [{ name: "Пицца с анананасами" }, { name: "Пицца вкусняшка" }],
      focused: false,
      value_input: '',
      input_add_product: '',
      input_exclude_product: '',
      added_products: [],
      excluded_products: []
    }
  },
  methods:{
    add_product(input_add_product){
      this.added_products.push(input_add_product)
      this.input_add_product = ''
    },
    exclude_product(input_exclude_product){
      this.excluded_products.push(input_exclude_product)
      this.input_exclude_product = ''
    },
    test(){
      // console.log(typeof(localStorage.getItem('login')))
      // console.log(typeof(this.value_input))
      // console.log(typeof(this.added_products))
      if (localStorage.getItem('login')){
        axios.post('http://localhost:8000/recipes', {
          login: String(localStorage.getItem('login')),
          query: this.value_input,
          desirable_ingredients: this.added_products,
          excluded_ingredients: this.excluded_products
        })
        .then((response) => {
          console.log(response)
        })
      }
    }
  }
}
</script>
<style lang="scss">
.finder{
  background-color: #FFF;
}

.inner {
  margin: 0 auto;
  max-width: 1600px;
  width: 95%;
  
}

.search {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fff;
  
  &__view{
    display: flex;
    align-items: center;
    height: 444px;
    
    & img{
      height: 444px;
      position: absolute;
      z-index: 0;
      transform: translateX(-200px);
    }
  }
  
  input {
    z-index: 1;
    width: 900px;
    border-radius: 13px;
    border: 4px solid #FF8139;
    background: #FFF;
    box-shadow: 0px 0px 30px 0px rgba(0, 0, 0, 0.10);
    padding-top: 15px;
    padding-bottom: 15px;
    padding-left: 21px;
    font-family: Montserrat;
    font-weight: 300;
    font-style: italic;
    font-size: 24px;
    // position: relative;
  }

  &__block {
    position: absolute;
    z-index: 1;
    display: flex;
    flex-direction: column;
    width: 980px;
    top: 250px;
    border-radius: 13px;
    border: 3px solid #FF8139;
    background: #FFF;
    box-shadow: 0px 0px 30px 0px rgba(0, 0, 0, 0.10);
    padding: 23px;
    transform: translateY(66px);

    &--btn {
      margin-left: 360px;
      border-radius: 20px;
      background: #FF8139;
      box-shadow: 0px 0px 30px 0px rgba(0, 0, 0, 0.25);
      padding-top: 15px;
      padding-bottom: 15px;
      text-align: center;
      width: 230px;
      color: #FFF;
      font-family: Montserrat;
      font-size: 32px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
      margin-top: 39px;
    }
  }

  &__products {

    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    column-gap: 18px;

    .product {
      color: #000;
      font-family: Montserrat;
      font-size: 24px;
      font-style: italic;
      font-weight: 400;
      line-height: normal;
      text-decoration-line: underline;
    }
  }

  &__time-block {
    margin-top: 40px;
    display: flex;
    flex-direction: column;
  }

  .time {
    &__title {

      color: #000;
      font-family: Montserrat;
      font-size: 32px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
    }

    &__desc {
      margin-top: 32px;
      color: #000;
      font-family: Montserrat;
      font-size: 24px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
    }
  }

  &__grade {
    //margin-top: 40px;
    display: flex;
    flex-direction: column;
    color: #000;
    font-family: Montserrat;
    font-size: 24px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;

    &-block {
      margin-top: 19px;
      display: flex;
      flex-direction: row;
      //justify-content: center;
      align-items: flex-start;

      input {
        margin-left: 8px;
        padding: 0;
        padding-left: 5px;
        width: 30px;
        height: 30px;
      }

      label {
        color: #000;
        font-family: Montserrat;
        font-size: 24px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
      }
    }
  }

  .search__block{
  }
  .modal {
    position: fixed; /* фиксированное положение */
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: rgba(0,0,0,0.5); /* цвет фона */
    z-index: 1;
    // opacity: 0; /* по умолчанию модальное окно прозрачно */
    -webkit-transition: opacity 200ms ease-in; 
    -moz-transition: opacity 200ms ease-in;
    transition: opacity 200ms ease-in; /* анимация перехода */
    pointer-events: none; /* элемент невидим для событий мыши */
    margin: 0;
    padding: 0;
  }
}

.time__slide {

  .rangeslider__tooltip {
    display: block;
    margin-top: 2.5em;
    font-size: 12px;
    color: #a59eb5;
  }

  .rangeslider,
  input[type='range'] {
    max-width: 400px;
  }

  .rangeslider__handle {
    border-radius: 22px;
    line-height: 42px;
    text-align: center;
    font-weight: bold;

    &:after {
      background: 0;
    }
  }

  .rangeslider,
  .rangeslider__fill {
    display: block;
    border-radius: 10px;
  }

  .rangeslider {
    background: #e6e5ea;
    background-image:
      linear-gradient(to right,
        #4bc67d 30%, #f1c40f 45%, #b94a48 99%);
    position: relative;
  }

  .rangeslider--horizontal {
    height: 10px;
    width: 100%;
  }

  .rangeslider--vertical {
    width: 20px;
    min-height: 150px;
    max-height: 100%;
  }

  .rangeslider--disabled {
    filter: progid:DXImageTransform.Microsoft.Alpha(Opacity=40);
    opacity: 0.4;
  }

  .rangeslider__fill {
    // background: #4bc67d;
    position: absolute;
  }

  .rangeslider--horizontal .rangeslider__fill {
    top: 0;
    height: 100%;
  }

  .rangeslider--vertical .rangeslider__fill {
    bottom: 0;
    width: 100%;
  }

  .rangeslider__handle {
    background: white;
    border: 6px solid #4bc67d;
    cursor: pointer;
    display: inline-block;
    width: 40px;
    height: 40px;
    position: absolute;
    -moz-border-radius: 50%;
    -webkit-border-radius: 50%;
    border-radius: 50%;

    &.js-low {
      border-color: #4bc67d;
    }

    &.js-med {
      border-color: #f1c40f;
    }

    &.js-high {
      border-color: #b94a48;
    }
  }

  .rangeslider__handle:after {
    content: "";
    display: block;
    width: 18px;
    height: 18px;
    margin: auto;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    -moz-border-radius: 50%;
    -webkit-border-radius: 50%;
    border-radius: 50%;
  }

  .rangeslider__handle:active {}

  .rangeslider--horizontal .rangeslider__handle {
    top: -20px;
    touch-action: pan-y;
    -ms-touch-action: pan-y;
  }

  .rangeslider--vertical .rangeslider__handle {
    left: -10px;
    touch-action: pan-x;
    -ms-touch-action: pan-x;
  }

  input[type="range"]:focus+.rangeslider .rangeslider__handle {
    -moz-box-shadow: 0 0 8px rgba(255, 0, 255, 0.9);
    -webkit-box-shadow: 0 0 8px rgba(255, 0, 255, 0.9);
    box-shadow: 0 0 8px rgba(255, 0, 255, 0.9);
  }
}
</style>
