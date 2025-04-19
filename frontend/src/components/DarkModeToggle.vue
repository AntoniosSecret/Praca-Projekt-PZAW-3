<script setup>
    import { onMounted } from 'vue'

    let navigationHeader = null
    let footer = null
    let darkmodeSwitch = null

    const body = document.body

    const applyDarkMode = () => {
        // Check if body already has the dark-mode class
        if (body.classList.contains('dark-mode')) {
            navigationHeader?.classList.add('dark-mode')
            footer?.classList.add('dark-mode')
            darkmodeSwitch?.classList.add('dark-mode')
        }
    }

    const toggleDarkMode = () => {
        body.classList.toggle('dark-mode')
        navigationHeader?.classList.toggle('dark-mode')
        footer?.classList.toggle('dark-mode')
        darkmodeSwitch?.classList.toggle('dark-mode')
        const isDarkMode = body.classList.contains('dark-mode')
        localStorage.setItem('dark-mode', isDarkMode ? 'enabled' : 'disabled')
    }

    onMounted(() => {
        // Initialize references to elements
        navigationHeader = document.querySelector('.navigation-header')
        footer = document.querySelector('.page-footer')
        darkmodeSwitch = document.getElementById('dark-mode-toggle')

        // Apply dark mode if it is already enabled
        applyDarkMode()
    })
</script>

<template>
    <div id="dark-mode-toggle">
        <label for="dark-mode-checkbox">&#9788;</label>
        <input type="checkbox" id="dark-mode-checkbox" @change="toggleDarkMode" />
    </div>
</template>