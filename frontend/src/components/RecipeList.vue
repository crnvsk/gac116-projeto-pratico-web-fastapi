<template>
    <div v-if="selectedUser" class="card shadow p-4">
      <h2 class="text-success">Receitas de {{ selectedUser.name }}</h2>
      <div class="mb-3">
        <input v-model="newTitle" placeholder="Título" class="form-control mb-2">
        <input v-model="newDesc" placeholder="Descrição" class="form-control mb-2">
        <button @click="addRecipe" class="btn btn-success">Adicionar</button>
      </div>
      <ul class="list-group">
        <li v-for="recipe in recipes" :key="recipe.id" class="list-group-item d-flex justify-content-between align-items-center">
          <span>
            <strong>{{ recipe.title }}</strong> - {{ recipe.description }}
          </span>
          <button @click="deleteRecipe(recipe.id)" class="btn btn-danger">Deletar</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    props: ["selectedUser"],
    data() {
      return { recipes: [], newTitle: "", newDesc: "" };
    },
    watch: {
      selectedUser(newUser) {
        axios.get(`http://localhost:8000/users/${newUser.id}/recipes`).then(res => this.recipes = res.data);
      }
    },
    methods: {
      addRecipe() {
        axios.post(`http://localhost:8000/users/${this.selectedUser.id}/recipes/`, { title: this.newTitle, description: this.newDesc })
          .then(res => this.recipes.push(res.data));
      },
      deleteRecipe(id) {
        axios.delete(`http://localhost:8000/recipes/${id}`).then(() => {
          this.recipes = this.recipes.filter(r => r.id !== id);
        });
      }
    }
  };
  </script>
  