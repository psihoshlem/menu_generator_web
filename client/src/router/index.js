import { createRouter, createWebHistory } from 'vue-router'
import HomePageView from '../views/HomePageView.vue'
import AuthView from '../views/AuthView.vue'
import SearchView from '../views/SearchView.vue'
import CreateRecipeView from '../views/CreateRecipeView.vue'
import EatenView from '../views/EatenView.vue'
import RecipeView from '../views/RecipeView.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePageView
  },
  {
    path: '/auth',
    name: 'auth',
    component: AuthView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/create_recipe',
    name: 'create_recipe',
    component: CreateRecipeView
  },
  {
    path: '/eaten',
    name: 'eaten',
    component: EatenView
  },
  {
    path: '/recipe:item_info',
    name: 'recipe',
    component: RecipeView
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
