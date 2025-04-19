<script setup>
import { defineProps } from 'vue';

defineProps({
    imageSrc: {
        type: String,
        required: true
    }
})
</script>

<template>
    <section class="exercise-block">
        <img :src="imageSrc" alt="Exercise Image"/>
        <span>&#9432;</span>
    </section>
</template>