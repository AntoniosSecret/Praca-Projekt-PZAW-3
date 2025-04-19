<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'
    import Navigation from '@/components/Navigation.vue'
    import Footer from '@/components/Footer.vue'
    import DarkModeToggle from '@/components/DarkModeToggle.vue'

    const message = ref('Loading...')

    onMounted(async () => {
        const res = await axios.get('http://127.0.0.1:8000/api/home/')
        message.value = res.data.message
    })
</script>

<template>
    <Navigation/>
    <DarkModeToggle/>
    <main>
        {{ message }}
        <!--
        
        - header / sidebar ( depending on the layout )
        - main
        - footer ( typical copyright info / tos )
        
        -->
    </main>
    <Footer/>
</template>