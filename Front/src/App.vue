<template>
  <header class="bg-gradient-to-r from-green-400 to-blue-500">
    <div class="container mx-auto py-6 flex justify-between items-center">
      <h1 class="text-4xl font-bold text-white text-center">
        Tu Buscador Latino
      </h1>
      <div>
        <router-link
          to="/"
          class="bg-white text-gray-800 font-bold py-2 px-4 rounded mr-2 hover:bg-blue-300">
          Home
        </router-link>
        <router-link
          to="/informes"
          class="bg-white text-gray-800 font-bold py-2 px-4 rounded hover:bg-blue-300">
          Informe
        </router-link>
      </div>
    </div>
  </header>
  <router-view></router-view>
</template>

<script>
import Home from "./views/Home.vue";
export default {
  name: "App",
  components: {
    Home,
  },
};
</script>
