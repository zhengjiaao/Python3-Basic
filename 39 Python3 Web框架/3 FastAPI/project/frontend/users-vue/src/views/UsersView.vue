<script setup>
import UsersComponent from '../components/UsersComponent.vue'
</script>

<template>
  <main>
    <UsersComponent/>
  </main>

<!--  <div>
    <h1>Users Page</h1>
    <UsersComponent/>
  </div>-->
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
