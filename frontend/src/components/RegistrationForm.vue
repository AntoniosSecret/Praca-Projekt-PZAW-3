<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'

    const username = ref('')
    const email = ref('')
    const password = ref('')
    const errorMessage = ref('')
    const successMessage = ref('')

    const handleRegister = async () => {
        try {
            const res = await axios.post('http://127.0.0.1:8000/api/register/', {
                username: username.value,
                email: email.value,
                password: password.value,
            })
            successMessage.value = 'Registration successful! Please check your email to verify your account.'
            errorMessage.value = ''
        } catch (error) {
            errorMessage.value = 'Registration failed. Please try again.'
            successMessage.value = ''
        }
    }
</script>

<template>
    <form @submit.prevent="handleRegister" class="registration-form">
        <input type="text" v-model="username" placeholder="Username" required />
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Register</button>
        <div v-if="errorMessage" style="color:red;">{{ errorMessage }}</div>
        <div v-if="successMessage" style="color:green;">{{ successMessage }}</div>
    </form>
</template>