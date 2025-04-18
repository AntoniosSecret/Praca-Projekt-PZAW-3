<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'
    import Navigation from '@/components/Navigation.vue'

    const message = ref('Loading...')

    onMounted(async () => {
        const res = await axios.get('http://127.0.0.1:8000/api/profile/')
        message.value = res.data.message
    })
</script>

<template>
    <Navigation/>
    {{ message }}
    <!--
    
    - header / sidebar ( depending on the layout )
    - main
    - footer ( typical copyright info / tos )
    
    -->
</template>