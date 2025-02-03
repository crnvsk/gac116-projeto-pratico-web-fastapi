<template>
  <div v-if="selectedUser" class="card shadow p-4">
    <h2 class="text-success">Receitas de {{ selectedUser.name }}</h2>
    <div v-if="recipes.length === 0">
      <p>Nenhuma receita encontrada.</p>
      <button @click="addRecipe" class="btn btn-success">Adicionar Receita</button>
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
      <button @click="addRecipe" class="btn btn-success mt-3">Adicionar Receita</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["selectedUser"],
  data() {
    return { recipes: [], selectedRecipe: null };
  },
  watch: {
    selectedUser(newUser) {
      axios.get(`http://localhost:8000/users/${newUser.id}/recipes`)
        .then(res => this.recipes = res.data);
    }
  },
  methods: {
    addRecipe() {
      const newRecipe = {
        title: "Nova Receita",
        description: "Descrição da nova receita"
      };
      axios.post(`http://localhost:8000/users/${this.selectedUser.id}/recipes/`, newRecipe)
        .then(res => {
          this.recipes.push(res.data);
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
  