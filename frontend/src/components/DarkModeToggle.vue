<script setup>
    import { onMounted } from 'vue'

    let navigationHeader = null
    let footer = null
    let navigationLabel = null
    let darkmodeSwitch = null

    const body = document.body

    const applyDarkMode = () => {
        const isDarkMode = localStorage.getItem('dark-mode') === 'enabled'
        if (isDarkMode) {
            body.classList.add('dark-mode')
            navigationHeader?.classList.add('dark-mode')
            footer?.classList.add('dark-mode')
            navigationLabel?.classList.add('dark-mode')
            darkmodeSwitch?.classList.add('dark-mode')
        }
    }

    const toggleDarkMode = () => {
        body.classList.toggle('dark-mode')
        navigationHeader?.classList.toggle('dark-mode')
        footer?.classList.toggle('dark-mode')
        navigationLabel?.classList.toggle('dark-mode')
        darkmodeSwitch?.classList.toggle('dark-mode')
        const isDarkMode = body.classList.contains('dark-mode')
        localStorage.setItem('dark-mode', isDarkMode ? 'enabled' : 'disabled')
    }

    onMounted(() => {
        navigationHeader = document.querySelector('.navigation-header')
        footer = document.querySelector('.page-footer')
        navigationLabel = document.getElementById('navigation-hamburger-label')
        darkmodeSwitch = document.getElementById('dark-mode-toggle')

        applyDarkMode()
    })
</script>

<template>
    <div id="dark-mode-toggle">
        <label for="dark-mode-checkbox">&#9788;</label>
        <input type="checkbox" id="dark-mode-checkbox" @change="toggleDarkMode" />
    </div>
</template>