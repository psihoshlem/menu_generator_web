<template>
  <div class="finder">
    <div class="inner">
      <div class="search">
        <div class="search__view">
          <img src="./../img/main-man-logo.png" alt="">
          <input type="text" class="search__input"
            placeholder="Давайте найдем что то вкусное" @focus="openModal"
            v-model="value_input"
            @input="input_writing()"
          >
        </div>
        <span v-if="focused" class="modal" @click="closeModal"></span>
        <div class="search__block" v-if="focused" @click.stop>
          <div class="search__products">
            <a href="" v-for="item in item_search" :key="item.id">
              <span class="product">
                {{ item.title }},
              </span>
            </a>
          </div>
          <div class="search__time-block" @blur="focused = false">
            <div class="time__title">Параметры поиска</div>
            <div class="search__params">
              <div class="search__params-add-products">
                <span>+ Включить продукты:</span>
                <div class="add-product">
                  <input type="text" placeholder="Введите желаемый продукт" v-model="input_add_product" v-on:keyup.enter="add_product(input_add_product)">
                  <button class="add-btn" @click="add_product(input_add_product)">Добавить</button>
                </div>
                <span>Добавлено:</span>
                <div class="adds_products">
                  <label class="adds_product" v-for="item in added_products" :key="item.id">
                    {{item}}
                  </label>
                </div>
              </div>
              <div class="search__params-del-products">
                <span>- Исключить продукты:</span>
                <div class="del-product">
                  <input type="text" placeholder="Введите нежелаемый продукт" v-model="input_exclude_product" v-on:keyup.enter="exclude_product(input_exclude_product)">
                  <button class="del-btn" @click="exclude_product(input_exclude_product)">Исключить</button>
                </div>
                <span>Исключено:</span>
                <div class="dels_products">
                  <label class="dels_product" v-for="item in excluded_products" :key="item.id">
                    {{ item }}
                  </label>
                </div>
              </div>
            </div>
            <div class="time__desc">Время готовки в минутах:
              <div class="time__slide">
                <input type="range" name="participants" min="5" max="120" value="20" oninput="rangeValue.innerText = this.value">
                <div>
                  <span id="rangeValue">20</span> мин
                </div>
              </div>
            </div>
          </div>
          <div class="search__grade">
            Рейтинг
            <div class="search__grade-block">
              <label for="grade">Звезд:</label>
              <input type="number" max="5" value="0">
            </div>
          </div>
          <div class="search__block--btn btn" @click="go_to_search()">Поиск</div>
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
      excluded_products: [],
      finish_search: [],
      item_search: []
    }
  },
  methods:{
    add_product(input_add_product){
      this.added_products.push(input_add_product)
      this.input_add_product = ''
      this.input_writing()
    },
    exclude_product(input_exclude_product){
      this.excluded_products.push(input_exclude_product)
      this.input_exclude_product = ''
      this.input_writing()
    },
    input_writing(){
      if (localStorage.getItem('login')){
        axios.post('http://localhost:8000/recipes', {
          login: String(localStorage.getItem('login')),
          query: this.value_input,
          desirable_ingredients: this.added_products,
          excluded_ingredients: this.excluded_products
        })
        .then((response) => {
          this.finish_search = response.data
          this.item_search = this.finish_search.slice(0,5)
        })
      }
    },
    go_to_search(){
      this.focused = false
      const str_output = JSON.stringify({login: String(localStorage.getItem('login')), query: this.value_input, desirable_ingredients: this.added_products, excluded_ingredients: this.excluded_products})
      this.$router.push({ path: '/search', query:{output_data: str_output}});
    },
    openModal() {
      this.focused = true;
      window.addEventListener('click', this.closeModal);
    },
    closeModal(event) {
      if (!this.$el.contains(event.target)) {
        this.focused = false;
        window.removeEventListener('click', this.closeModal);
      }
    }
  }
}
</script>
<style lang="scss">
.time__slide input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none !important;
    background-color: #FF5733;
}
.time__slide input[type="range"] {
    width: 400px;
    background-color: #FF5733;
}

.search__params{
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 20px;
  font-family: Montserrat;

  &-add-products{
    border: 1px solid rgba(128, 128, 128, 0.5);
    border-radius: 25px;
    padding: 30px;

    span{
      font-size: 24px;
      font-weight: 400;
      margin-bottom: 20px;
    }

    .add-product{
      display: flex;
      align-items: center;
      gap: 20px;

      input{
        margin: 20px 0;
        width: 425px;
        height: 51px;
        border: 3px solid #FF8139;
        font-size: 24px;
      }

      button{
        width: 155px;
        height: 51px;
        color: #fff;
        background-color: #FF8139;
        border-radius: 15px;
        font-size: 20px;
      }
    }

    .adds_products{
      margin-top: 20px;
      display: flex;
      flex-direction: row;
      gap: 20px;

      .adds_product{
        border: 3px solid #FF8139;
        color: #FF8139;
        font-size: 24px;
        padding: 10px 20px;
        border-radius: 25px;
      }
    }
  }

  &-del-products{
    border: 1px solid rgba(128, 128, 128, 0.5);
    border-radius: 25px;
    padding: 30px;

    span{
      font-size: 24px;
      font-weight: 400;
      margin-bottom: 20px;
    }

    .del-product{
      display: flex;
      align-items: center;
      gap: 20px;

      input{
        margin: 20px 0;
        width: 425px;
        height: 51px;
        border: 3px solid #7E1700;
        font-size: 24px;
      }

      button{
        width: 155px;
        height: 51px;
        color: #fff;
        background-color: #7E1700;
        border-radius: 15px;
        font-size: 20px;
      }

    }
    .dels_products{
      margin-top: 20px;
      display: flex;
      flex-direction: row;
      gap: 20px;

      .dels_product{
        border: 3px solid #7E1700;
        color: #7E1700;
        font-size: 24px;
        padding: 10px 20px;
        border-radius: 25px;
      }
    }
  }
}

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
    z-index: 999;
    width: 980px;
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
      font-size: 16px;
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
    border-top: 1px solid rgba(128, 128, 128, 0.5);
    border-bottom: 1px solid rgba(128, 128, 128, 0.5);
    padding: 10px 0;
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
      border-top: 1px solid rgba(128, 128, 128, 0.5);
      border-bottom: 1px solid rgba(128, 128, 128, 0.5);
    }
  }

  &__grade {
    display: flex;
    flex-direction: column;
    color: #000;
    font-family: Montserrat;
    font-size: 24px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    border-bottom: 1px solid rgba(128, 128, 128, 0.5);
    padding: 10px 0;

    &-block {
      margin-top: 19px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      align-items: center;
      gap: 10px;

      input {
        width: 70px;
        height: 50px;
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

  .modal {
    position: fixed; 
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: rgba(0,0,0,0.5); 
    z-index: 1;
    // opacity: 0; 
    -webkit-transition: opacity 200ms ease-in; 
    -moz-transition: opacity 200ms ease-in;
    transition: opacity 200ms ease-in;
    pointer-events: none; 
    margin: 0;
    padding: 0;
  }
}
</style>
