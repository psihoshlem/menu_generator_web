<template>
  <HeaderComp :style="style_for_header"/>
  <div class="neuro" >
    <div class="neuro__info">
      <div class="neuro__info-title">
        <h3>Приготовлено <span>нейросетью</span> с ❤️</h3>
        <h1>Бургер - три сыра</h1>
        <div>Stars</div>
        <div>
          <span>~20 мин</span>
        </div>
      </div>
    </div>
    <div class="neuro__steps"></div>
  </div>
</template>
<script>
import HeaderComp from '../components/HeaderComp.vue';
export default {
  components: {
    HeaderComp
  },
  data(){
    return{
      style_for_header: {
        color_text: "white",
        brackground_color: "black"
      }
    }
  }
}
</script>
<style lang="scss">

</style>
