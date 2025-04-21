<script setup>
    import { RouterLink } from 'vue-router'
    import { onMounted } from 'vue'

    let navigationHeader = null
    let hamburgerLabel = null
    let hamburgerInput = null

    const toggleHamburgerMenu = () => {
        if (!hamburgerInput.checked) {
            navigationHeader?.classList.add('closed')
        } else {
            navigationHeader?.classList.remove('closed')
        }
    }
        

    onMounted(() => {
        navigationHeader = document.querySelector('.navigation-header')
        hamburgerInput = document.getElementById('navigation-hamburger-input')
        hamburgerLabel = document.getElementById('navigation-hamburger-label')

        if (window.innerHeight > window.innerWidth) {
            //navigationHeader.classList.add('mobile')
            //alert('Mobile view detected')
        }
        else {
            //navigationHeader.classList.remove('mobile')
        }
    })
</script>

<template>
    <label for="navigation-hamburger-input" id="navigation-hamburger-label">
        <span class="hamburger-icon">&#9776;</span>
    </label>
    <input type="checkbox" value="Open" @click="toggleHamburgerMenu" checked id="navigation-hamburger-input"/>
    <header class="navigation-header">
        <nav>
            <ul>
                <li>
                    <RouterLink to="/home">Home</RouterLink>
                </li>
                <li>
                    <RouterLink to="/profile">Profile</RouterLink>
                </li>
                <li>
                    <RouterLink to="/all-exercises">All Exercises</RouterLink>
                </li>
            </ul>
        </nav>
    </header>
</template>