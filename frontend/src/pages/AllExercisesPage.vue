<script setup>
    import { ref, onMounted } from 'vue'
    import { RouterLink } from 'vue-router'
    import axios from 'axios'
    import Navigation from '@/components/Navigation.vue'
    import ExerciseBlock from '@/components/ExerciseBlock.vue'
    import Footer from '@/components/Footer.vue'
    import DarkModeToggle from '@/components/DarkModeToggle.vue'

    const exercises = ref([])

    onMounted(async () => {
        try {
            const res = await axios.get('http://127.0.0.1:8000/api/all-exercises/')
            exercises.value = res.data
        } catch (error) {
            console.error('Error fetching exercises:', error)
        }
    })
</script>

<template>
    <Navigation/>
    <DarkModeToggle/>
    <main>
        <div class="wrapper">
            <h1>All Exercises</h1>
            
            <section class="exercises-grid">
                <RouterLink :to="`/exercise/${exercise.id}/`" v-for="(exercise, index) in exercises" :key="index">
                    <!-- {{ exercise.name }}<br>
                    {{ exercise.description }}<br>
                    {{ exercise.category }}<br>
                    {{ exercise.equipment }}<br>
                    {{ exercise.target_muscle }}<br> -->
                    <ExerciseBlock :imageSrc="exercise.image_url"/>
                </RouterLink>
            </section>
        </div>
    </main>
    <Footer/>
</template>