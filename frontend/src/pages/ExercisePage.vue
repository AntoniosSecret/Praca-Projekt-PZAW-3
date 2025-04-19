<script setup>
    import { useRoute } from 'vue-router';
    import { ref, onMounted } from 'vue'
    import axios from 'axios'
    import Navigation from '@/components/Navigation.vue';
    import Footer from '@/components/Footer.vue';
    import DarkModeToggle from '@/components/DarkModeToggle.vue';

    const exercise = ref(null)
    const route = useRoute()

    onMounted(async () => {
        try {
            const exerciseId = route.params.id
            const res = await axios.get('http://127.0.0.1:8000/api/exercise/' + exerciseId)
            exercise.value = res.data
        } catch (error) {
            console.error('Error fetching exercise:', error)
        }
    })

</script>

<template>
    <Navigation/>
    <DarkModeToggle/>
    <main>
        <div class="exercise-container" v-if="exercise">
            <div id="left">
                <img :src="exercise.image_url" alt="Exercise Image" />
                <div id="heading-container">
                    <h1>{{ exercise.name }}</h1>
                    <span id="equipment">({{ exercise.equipment }})</span>
                </div>
                <p class="exercise-details" id="target-muscle">{{ exercise.target_muscle }}</p>
                <p class="exercise-details" id="desc">{{ exercise.description }}</p>
            </div>
            <div id="right">
                <h2>Instructions</h2>
                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Aliquam fugit quas, laborum doloribus ipsa at maiores recusandae ut praesentium dolorem! Voluptatum quia accusantium enim adipisci numquam accusamus inventore excepturi quod!</p>
            </div>
            
        </div>
        <div v-else>
            <p>Loading exercise...</p>
        </div>
    </main>
    <Footer/>
</template>