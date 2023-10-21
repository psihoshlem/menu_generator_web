<template>
  <section class="Auth">
    <div class="inner">
      <img src="./../img/woman.png" alt="">
      <img src="./../img/cheif.png" alt="">
      <div class="Auth__block">
        <div class="auth authWrap">
          <div class="auth__title">Вход</div>
          <div class="auth__login field">
            <label for="login">Логин</label>
            <input name="login" type="text">
          </div>
          <div class="auth__password field">
            <label for="password">Пароль</label>
            <input name="password" type="password">
          </div>
          <div class="btn" @click="go_auth()">Войти</div>
          <div v-if="error_auth">не правильный пароль или логин</div>
        </div>
        <hr>
        <div class="registration authWrap">
          <div class="registration__title">Регистрация</div>
          <div class="registration__email field ">
            <label for="mail">Email</label>
            <input name="mail" type="mail">
          </div>
          <div class="registration__login field">
            <label for="login">Логин</label>
            <input name="login" type="text" v-model="log">
          </div>
          <div class="registration__password field">
            <label for="password">Пароль</label>
            <input name="password" type="password" v-model="pass">
          </div>
          <div class="btn" @click="go_reg()">
            Регестрация
          </div>
          <div v-if="error_reg">
            существует такой логин
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import axios from 'axios';
import router from '@/router';

export default{
  data(){
    return{
      pass: '',
      log: '',
      error_auth: false,
      error_reg: false
    }
  },
  methods:{
    go_reg(){
      axios.post('http://localhost:8000/reg', {
          login: this.log,
          password: this.pass
      })
      .then((response) => {
        if (response.data == true) {
          localStorage.setItem('auth_status', response.data)
          router.push('/')
        } else {
          this.error_reg = true
        }
      })
    },
    go_auth(){
      axios.post('http://localhost:8000/auth', {
          login: this.log,
          password: this.pass
      })
      .then((response) => {
        if (response.data == true) {
          localStorage.setItem('auth_status', response.data)
          router.push('/')
        } else {
          this.error_auth = true
        }
      })
    },
  }
}
</script>
<style lang="scss">
.Auth {
  background-color: #FFF;
  padding-top: 150px;
  height: 100%;
  
  .inner{
    
  }

  & img{
    position: absolute;
    z-index: 0;
  }
  
  &__block {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    //padding-left: 280px;
    align-items: center;
  }
  
  .auth {
    z-index: 1;
    min-width: 380px;
    display: flex;
    flex-direction: column;
    align-items: center;

    
    &__title {
      color: #000;
      font-family: Montserrat;
      font-size: 36px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
    }
  }

  .registration {
    width: 500px;

    &__title {
      text-align: center;
      color: #000;
      font-family: Montserrat;
      font-size: 36px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
    }
  }

  .field {
    display: flex;
    flex-direction: column;
    row-gap: 14px;
    width: 100%;

    label {
      color: #000;
      font-family: Montserrat;
      font-size: 20px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
    }

    input {
      padding: 12px;
      border-radius: 20px;
      border: 3px solid #FF8139;
      background: #FFF;
      box-shadow: 0px 0px 30px 0px rgba(0, 0, 0, 0.10);
    }
  }

  .authWrap {
    display: flex;
    flex-direction: column;
    row-gap: 30px;
  }

  .btn {
    text-align: center;
    color: #FFF;
    font-family: Montserrat;
    font-size: 32px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    cursor: pointer;
    padding: 12px;
    border-radius: 20px;
    background: #FF8139;
    box-shadow: 0px 0px 30px 0px rgba(0, 0, 0, 0.25);
  }

  hr {
    transform: rotate(90deg);
    height: 3px;
    background: #D8D8D8;
    width: 480px;
  }
}
</style>
