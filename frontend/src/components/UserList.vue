<template>
    <div class="card shadow p-4">
      <h2 class="text-primary">Usuários</h2>
      <div class="input-group mb-3">
        <input v-model="newUser" placeholder="Nome do usuário" class="form-control">
        <button @click="addUser" class="btn btn-primary">Adicionar</button>
      </div>
      <ul class="list-group">
        <li v-for="user in users" :key="user.id" class="list-group-item d-flex justify-content-between">
          <span @click="selectUser(user)" class="cursor-pointer">
            <strong>{{ user.name }}</strong>
          </span>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return { users: [], newUser: "" };
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
        this.$emit("user-selected", user);
      }
    }
  };
  </script>
  