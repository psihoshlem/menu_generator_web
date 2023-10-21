<template>
  <section class="Auth">
    <div class="inner">
      <div class="Auth__block">
        <div class="auth authWrap">
          <img class="woman" src="./../img/woman.png" alt="">
          <div class="auth__title">Вход</div>
          <div class="auth__login field">
            <label for="login">Логин</label>
            <input name="login" type="text" v-model="log_auth">
          </div>
          <div class="auth__password field">
            <label for="password">Пароль</label>
            <input name="password" type="password" v-model="pass_auth">
          </div>
          <div class="btn" @click="go_auth()">Войти</div>
          <div v-if="error_auth">{{ error_msg }}</div>
        </div>
        <hr>
        <div class="registration authWrap">
          <img class="cheif" src="./../img/cheif.png" alt="">
          <div class="registration__title">
            Регистрация
          </div>
          <div class="registration__login field">
            <label for="login">
              Логин
            </label>
            <input name="login" type="text" v-model="log_reg">
          </div>
          <div class="registration__password field">
            <label for="password">
              Пароль
            </label>
            <input name="password" type="password" v-model="pass_reg">
          </div>
          <div class="registration__repeat field">
            <label for="password_repeat">
              Повторите пароль
            </label>
            <input name="password_repeat" type="text" v-model="pass_repeat_reg">
          </div>
          <div class="btn" @click="go_reg()">
            Зарегистрироваться
          </div>
          <div v-if="error_reg">{{ error_msg }}</div>
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
      pass_reg: '',
      pass_repeat_reg: '',
      log_reg: '',
      log_auth: '',
      pass_auth: '',
      error_auth: false,
      error_reg: false,
      error_msg: ''
    }
  },
  methods:{
    go_reg(){
      if (this.pass_reg == this.pass_repeat_reg){
        axios.post('http://localhost:8000/reg', {
            login: this.log_reg,
            password: this.pass_reg
        })
        .then((response) => {
          if (response.data == true) {
            localStorage.setItem('auth_status', response.data)
            router.push('/')
          } else {
            this.error_reg = true
            this.error_msg = "Такой логин уже существует"
          }
        })
      } else {
        this.error_reg = true
        this.error_msg = "Пароли не совпадают ебан"
      }
    },
    go_auth(){
      axios.post('http://localhost:8000/auth', {
          login: this.log_auth,
          password: this.pass_auth
      })
      .then((response) => {
        if (response.data == true) {
          localStorage.setItem('auth_status', response.data)
          router.push('/')
        } else {
          this.error_auth = true
          this.error_msg = "Не верный логин или пароль"
        }
      })
    },
  }
}
</script>
<style lang="scss">
  .woman{
    z-index: 0;
    position: absolute;
    left: 0;
    bottom: 0;
  }

  .cheif{
    z-index: 0;
    position: absolute;
    right: 0;
    bottom: 0;
  }
.Auth {
  background-color: #FFF;
  padding-top: 150px;

  input{
    font-family: Montserrat;
    font-size: 20px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
  }

  &__block {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    //padding-left: 280px;
    align-items: center;
  }

  .auth {
    min-width: 380px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    &__title {
      color: #000;
      font-family: Montserrat;
      font-size: 36px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
      z-index: 1;
    }
  }

  .registration {
    max-width: 500px;
    display: flex;
    flex-direction: column;
    align-items: center;

    &__title {
      text-align: center;
      color: #000;
      font-family: Montserrat;
      font-size: 36px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
      z-index: 1;
    }
  }

  label {
    color: #000;
    font-family: Montserrat;
    font-size: 20px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
  }

  input {
    width: 350px;
    padding: 12px;
    border-radius: 20px;
    border: 3px solid #FF8139;
    background: #FFF;
    box-shadow: 0px 0px 30px 0px rgba(0, 0, 0, 0.10);

  }
  .field {
    z-index: 1;
    display: flex;
    flex-direction: column;
    row-gap: 14px;
    // width: 100%;
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
    z-index: 1;
  }

  hr {
    transform: rotate(90deg);
    height: 3px;
    background: #D8D8D8;
    width: 480px;
  }
}
</style>
