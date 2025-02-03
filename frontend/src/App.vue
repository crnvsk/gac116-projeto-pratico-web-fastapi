<script setup>
import UserList from './components/UserList.vue'
import RecipeList from './components/RecipeList.vue'
</script>

<template>
  <div class="container">
    <header class="bg-primary text-white text-center p-4 mb-4">
      <h1>Gerenciador de Receitas</h1>
    </header>

    <div class="row">
      <div class="col-md-6">
        <UserList />
      </div>
      <div class="col-md-6">
        <RecipeList />
      </div>
    </div>
  </div>
</template>