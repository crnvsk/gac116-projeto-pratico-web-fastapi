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
        <button @click="editRecipe(recipe)" class="btn btn-warning">Editar</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["selectedUser"],
  data() {
    return { 
      recipes: [],
      newTitle: "",
      newDesc: "",
      editingRecipe: null,
    };
  },
  watch: {
    selectedUser(newUser) {
      axios.get(`http://localhost:8000/users/${newUser.id}/recipes`)
        .then(res => this.recipes = res.data);
    }
  },
  methods: {
    addRecipe() {
      axios.post(`http://localhost:8000/users/${this.selectedUser.id}/recipes/`, {
        title: this.newTitle,
        description: this.newDesc
      })
      .then(res => {
        this.recipes.push(res.data);
        this.newTitle = "";
        this.newDesc = "";
      });
    },
    deleteRecipe(id) {
      axios.delete(`http://localhost:8000/recipes/${id}`)
        .then(() => {
          this.recipes = this.recipes.filter(r => r.id !== id);
        });
    },
    editRecipe(recipe) {
      this.editingRecipe = recipe;
      this.newTitle = recipe.title;
      this.newDesc = recipe.description;
    },
    saveRecipe() {
      if (this.editingRecipe) {
        axios.put(`http://localhost:8000/recipes/${this.editingRecipe.id}`, {
          title: this.newTitle,
          description: this.newDesc
        })
        .then(res => {
          const index = this.recipes.findIndex(r => r.id === this.editingRecipe.id);
          this.recipes[index] = res.data;
          this.editingRecipe = null;
          this.newTitle = "";
          this.newDesc = "";
        });
      }
    }
  }
};
</script>
