<template>
  <div class="card shadow p-4">
    <h2 class="text-primary">Usuários</h2>
    <div class="input-group mb-3">
      <input v-model="newUser" placeholder="Nome do usuário" class="form-control">
      <button @click="addUser" class="btn btn-primary">Adicionar</button>
    </div>
    <ul class="list-group">
      <li v-for="user in users" :key="user.id" class="list-group-item d-flex justify-content-between">
        <div class="d-flex justify-content-between align-items-center w-100">
          <span @click="selectUser(user)" class="cursor-pointer">
            <strong>{{ user.name }}</strong>
          </span>
          
          <!-- Botões ao lado do nome do usuário -->
          <div class="btn-group">
            <button v-if="!isEditing || editedUser.id !== user.id" @click="editUser(user)" class="btn btn-warning btn-sm">Editar</button>

            <!-- Formulário de edição -->
            <div v-if="isEditing && editedUser.id === user.id">
              <input v-model="editedUser.name" placeholder="Nome do usuário" class="form-control">
              <button @click="updateUser" class="btn btn-success btn-sm">Salvar</button>
              <button @click="cancelEdit" class="btn btn-secondary btn-sm">Cancelar</button>
            </div>

            <button @click="deleteUser(user)" class="btn btn-danger btn-sm">Excluir</button>

            <button @click="selectUser(user)" class="btn btn-info btn-sm">Receitas</button>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return { 
      users: [], 
      newUser: "",
      isEditing: false,  // Flag para controle de edição
      editedUser: null,  // Usuario que está sendo editado
    };
  },
  mounted() {
    axios.get("http://localhost:8000/users/").then(res => this.users = res.data);
  },
  methods: {
    addUser() {
      axios.post("http://localhost:8000/users/", { name: this.newUser }).then(res => {
        this.users.push(res.data);
        this.newUser = "";
      });
    },
    selectUser(user) {
      this.$emit("user-selected", user);  // Emitir evento para o componente pai
    },
    editUser(user) {
      this.isEditing = true;
      this.editedUser = { ...user };  // Fazer uma cópia do usuário para editar
    },
    updateUser() {
      axios.put(`http://localhost:8000/users/${this.editedUser.id}/`, { name: this.editedUser.name })
        .then(res => {
          const index = this.users.findIndex(u => u.id === res.data.id);
          if (index !== -1) {
            this.users[index].name = res.data.name;
          }
          this.isEditing = false;
          this.editedUser = null;  // Limpa o usuário editado
        })
        .catch(error => {
          console.error("Erro ao atualizar usuário", error);
        });
    },
    cancelEdit() {
      this.isEditing = false;
      this.editedUser = null;
    },
    deleteUser(user) {
      if (confirm(`Tem certeza de que deseja excluir o usuário "${user.name}"?`)) {
        axios.delete(`http://localhost:8000/users/${user.id}/`)
          .then(() => {
            this.users = this.users.filter(u => u.id !== user.id);
          })
          .catch(error => {
            console.error("Erro ao excluir usuário", error);
          });
      }
    }
  }
};
</script>

<style scoped>
/* Estilos para o botão de editar e excluir */
.btn-group {
  display: flex;
  gap: 5px;
}
</style>