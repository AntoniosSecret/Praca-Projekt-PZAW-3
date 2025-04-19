<script setup>
    import { RouterLink } from 'vue-router'
</script>

<template>
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