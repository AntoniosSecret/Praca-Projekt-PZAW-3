<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'
    import Navigation from '@/components/Navigation.vue'
    import Footer from '@/components/Footer.vue'
    import DarkModeToggle from '@/components/DarkModeToggle.vue'

    const message = ref('Loading...')
    const exercises = ref([])

    onMounted(async () => {
        try {
            const res = await axios.get('http://127.0.0.1:8000/api/home/')
            const res2 = await axios.get('http://127.0.0.1:8000/api/all-exercises/')
            message.value = res.data.message
            exercises.value = res2.data
        } catch (error) {
            console.error('Error fetching message:', error)
        }
    })
</script>

<template>
    <Navigation/>
    <DarkModeToggle/>
    <main>
        <div class="wrapper">
            <h1>Home</h1>
        </div>
        {{ message }}
        <!--
        
        - header / sidebar ( depending on the layout )
        - main
        - footer ( typical copyright info / tos )
        
        -->
    </main>
    <Footer/>
</template>