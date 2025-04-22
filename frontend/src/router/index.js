import { createRouter, createWebHistory, useRoute } from 'vue-router'
import HomePage from '@/pages/HomePage.vue'

const route = useRoute()

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
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../pages/RegistrationPage.vue'),
      meta: { title: 'Register' },
    },
    {
      path: '/exercise/:id',
      name: 'exercise',
      component: () => import('../pages/ExercisePage.vue'),
      meta: { title: 'Exercise' },
    },
    {
      path: '/:notFound(.*)',
      name: 'not-found',
      component: import('../pages/NotFoundPage.vue'),
      meta: { title: '404 Not Found' },
    }
  ],
})

router.afterEach((to) => {
  const defaultTitle = 'Default Title'
  const id = (to.params.id) ? ` ${to.params.id}` : ''
  document.title = (to.meta.title + id + " :: GainzTrackr") || defaultTitle
})

export default router
