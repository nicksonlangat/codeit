import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  
  {
    path: '/',
    name: 'hero',
    component: () => import('../views/Hero.vue')
  },
  {
    path: '/new',
    name: 'new',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/link/:id',
    name: 'link',
    component: () => import('../views/Link.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
