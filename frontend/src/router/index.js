import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/pages/HomePage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: HomePage,
      meta: { title: 'Home' },
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../pages/ProfilePage.vue'),
      meta: { title: 'User Profile' },
    },
    {
      path: '/all-exercises',
      name: 'all-exercises',
      component: () => import('../pages/AllExercisesPage.vue'),
      meta: { title: 'All Exercises' },
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../pages/LoginPage.vue'),
      meta: { title: 'Login' },
    }
  ],
})

router.afterEach((to) => {
  const defaultTitle = 'Default Title'
  document.title = to.meta.title + " :: GainzTrackr" || defaultTitle
})

export default router
