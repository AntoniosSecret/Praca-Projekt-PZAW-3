<script setup>
import '@/assets/style.css'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const message = ref('Loading...')

onMounted(async () => {
  const res = await axios.get('http://127.0.0.1:8000/api/')
  message.value = res.data.message
})
</script>

<template>
  <!--
  <header>
    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>
  -->

  <router-view/>
</template>