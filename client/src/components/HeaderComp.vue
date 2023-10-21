<template>
  <header class="header">
    <div class="inner">
      <div class="header__block">
        <div class="header__logo">
          <img src="./../img/mainUmomLogo.png" @click="go_home()">
        </div>
        <div class="header__nav">
          <a href="" class="header__nav--link" @click="go_home()">Главная</a>
          <a href="" class="header__nav--link">Все рецепты</a>
          <a href="" class="header__nav--link">Съедено</a>
          <a href="" class="header__nav--link" @click="go_seach()">Поиск</a>
          <a href="" class="header__nav--link">Избранное</a>
        </div>
        <div class="header__info header__nav--link" v-if="auth" @click="go_exit()">
          Выход
        </div>
        <div class="header__info header__nav--link" v-else @click="go_auth">
          Вход / Регистрация
        </div>
      </div>
    </div>
  </header>
</template>
<script>
import router from '@/router';

export default {
  data() {
    return {
      auth: false
    }
  },
  methods: {
    go_auth() {
      router.push('/auth')
    },
    go_exit(){
      this.auth = false
      localStorage.setItem('auth_status', "false")
    },
    go_home(){
      router.push('/')
    },
    go_seach(){
      router.push('/search')
    }
  },
  async mounted(){
    if (localStorage.getItem('auth_status') == "true"){
      this.auth = true
    } else {
      this.auth = false
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

.header {
  background-color: #fff;


  &__block {
    padding-top: 22px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }

  &__nav {
    display: flex;
    flex-direction: row;
    column-gap: 50px;

    &--link {
      text-decoration: none;
      color: #000;
      font-family: Montserrat;
      font-size: 24px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
    }
  }

  &__info {
    cursor: pointer;

  }
}
</style>
