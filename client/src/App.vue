<template>
  <div class="general-wrapper">
    <div class="main-cont">
      <router-view></router-view>
    </div>
    <div class="middle-cont"></div>
    <div class="footer-cont">
      <FooderComp />
    </div>
  </div>
</template>
<script>
import FooderComp from './components/FooderComp.vue';
export default {
  components: {
    FooderComp,
  }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;1,300&display=swap');
body{
  background: url('./img/parallax.png');
  background-repeat: repeat repeat;
  background-position: center;
  background-size: cover;
  background-attachment: fixed;
  margin-left: auto;
  margin-right: auto;
  backdrop-filter: blur(5px);
}

body,
html{
  height: 100%;
}

.general-wrapper{
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.middle-cont{
  background-color: #fff;
  flex: 1 1 auto;
}

body::-webkit-scrollbar {
  width: 4px;
}
body::-webkit-scrollbar-track {
  background: transparent;
}
body::-webkit-scrollbar-thumb {
  background-color: #FF8139;
  border-radius: 20px;
}
/* Reset and base styles  */
* {
	padding: 0px;
	margin: 0px;
	border: none;
}

*,
*::before,
*::after {
	box-sizing: border-box;
}

/* Links */

a, a:link, a:visited  {
    text-decoration: none;
}

a:hover  {
    text-decoration: none;
}

/* Common */

aside, nav, footer, header, section, main {
	display: block;
}

h1, h2, h3, h4, h5, h6, p {
    font-size: inherit;
	font-weight: inherit;
}

ul, ul li {
	list-style: none;
}

img {
	vertical-align: top;
}

img, svg {
	max-width: 100%;
	height: auto;
}

address {
  font-style: normal;
}

/* Form */

input, textarea, button, select {
	font-family: inherit;
    font-size: inherit;
    color: inherit;
    background-color: transparent;
}

input::-ms-clear {
	display: none;
}

button, input[type="submit"] {
    display: inline-block;
    box-shadow: none;
    background-color: transparent;
    background: none;
    cursor: pointer;
}

input:focus, input:active,
button:focus, button:active {
    outline: none;
}

button::-moz-focus-inner {
	padding: 0;
	border: 0;
}

label {
	cursor: pointer;
}

legend {
	display: block;
}

</style>
