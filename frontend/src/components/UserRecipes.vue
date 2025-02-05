<template>
  <div v-if="selectedUser" class="card shadow p-4">
    <h2 class="text-success">Receitas de {{ selectedUser.name }}</h2>
    <div v-if="recipes.length === 0">
      <p>Nenhuma receita encontrada.</p>
      <button @click="showAddRecipeForm" class="btn btn-success">Adicionar Receita</button>
    </div>
    <div v-else>
      <ul class="list-group">
        <li v-for="recipe in recipes" :key="recipe.id" class="list-group-item d-flex justify-content-between align-items-center">
          <span>
            <strong>{{ recipe.title }}</strong> - {{ recipe.description }}
          </span>
          <button @click="selectRecipe(recipe)" class="btn btn-danger">Excluir</button>
        </li>
      </ul>
      <button @click="showAddRecipeForm" class="btn btn-success mt-3">Adicionar Receita</button>
    </div>

    <!-- Formulário para adicionar receita -->
    <div v-if="showForm" class="mt-3">
      <input v-model="newRecipe.title" placeholder="Título" class="form-control mb-2">
      <input v-model="newRecipe.description" placeholder="Descrição" class="form-control mb-2">
      <button @click="addRecipe" class="btn btn-success">Salvar</button>
      <button @click="hideAddRecipeForm" class="btn btn-secondary">Cancelar</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["selectedUser"],
  data() {
    return { 
      recipes: [], 
      selectedRecipe: null,
      showForm: false,
      newRecipe: {
        title: "",
        description: ""
      }
    };
  },
  watch: {
    selectedUser(newUser) {
      axios.get(`http://localhost:8000/users/${newUser.id}/recipes`)
        .then(res => this.recipes = res.data);
    }
  },
  methods: {
    showAddRecipeForm() {
      this.showForm = true;
    },
    hideAddRecipeForm() {
      this.showForm = false;
      this.newRecipe = { title: "", description: "" };
    },
    addRecipe() {
      axios.post(`http://localhost:8000/users/${this.selectedUser.id}/recipes/`, this.newRecipe)
        .then(res => {
          this.recipes.push(res.data);
          this.hideAddRecipeForm();
        });
    },
    selectRecipe(recipe) {
      this.selectedRecipe = recipe;
      if (confirm(`Deseja excluir a receita "${recipe.title}"?`)) {
        this.deleteRecipe(recipe.id);
      }
    },
    deleteRecipe(id) {
      axios.delete(`http://localhost:8000/recipes/${id}`).then(() => {
        this.recipes = this.recipes.filter(r => r.id !== id);
        this.selectedRecipe = null;
      });
    }
  }
};
</script>