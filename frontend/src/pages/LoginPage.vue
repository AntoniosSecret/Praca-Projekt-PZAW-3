<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'
    import Navigation from '@/components/Navigation.vue'
    import { useRouter } from 'vue-router'

    const email = ref('')
    const password = ref('')
    const errorMessage = ref('')
    const router = useRouter()

    const login = async () => {
        try {
            const res = await axios.post('http://')
            if (res.status === 200) {
                // Redirect to the home page or any other page after successful login
                router.push('/home')
            } else {
                errorMessage.value = 'Invalid credentials'
            }
        } catch (error) {
            errorMessage.value = 'An error occurred during login'
        }
    }
</script>

<template>
    
</template>

