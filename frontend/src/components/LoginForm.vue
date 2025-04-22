<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'

    const username = ref('')
    const password = ref('')
    const errorMessage = ref('')

    const handleLogin = async () => {
        try {
            const res = await axios.post('http://127.0.0.1/api/token/', {
                username: username.value,
                password: password.value
            })
            localStorage.setItem('access_token', res.data.access)
            localStorage.setItem('refresh_token', res.data.refresh)
            error.value = ''
        } catch (error) {
            error.value = 'Invalid username or password'
        }
    }
</script>

<template>
    <form @submit.prevent="handleLogin" class="login-form">
        <input type="text" v-model="username" placeholder="Username" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Login</button>
        <div v-if="error" style="color:red;">{{ error }}</div>
    </form>
</template>