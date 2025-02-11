// example-frontend/frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Users from '../views/Users.vue'
import Files from '../views/Files.vue'

const routes = [
  {
    path: '/',
    name: 'Users',
    component: Users
  },
  {
    path: '/files',
    name: 'Files',
    component: Files
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
