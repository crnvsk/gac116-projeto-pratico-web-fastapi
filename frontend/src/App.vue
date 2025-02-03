<template>
  <div class="container">
    <header class="bg-primary text-white text-center p-4 mb-4">
      <h1>Gerenciador de Receitas</h1>
    </header>

    <div class="row">
      <div class="col-md-6">
        <UserList @user-selected="handleUserSelected" />
      </div>
      <div class="col-md-6">
        <UserRecipes v-if="selectedUser" :selectedUser="selectedUser" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import UserList from './components/UserList.vue';
import UserRecipes from './components/UserRecipes.vue';

const selectedUser = ref(null);

function handleUserSelected(user) {
  selectedUser.value = user;
}
</script>
