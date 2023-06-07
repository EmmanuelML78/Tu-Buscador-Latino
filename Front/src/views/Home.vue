<template>
  <div class="flex flex-col justify-center items-center min-h-96">
    <div class="mt-2 max-w-lg w-full bg-white rounded-lg shadow-md p-6">
      <form @submit="handleSearch" class="flex">
        <input
          class="flex-grow rounded-l-lg px-4 py-2 border border-gray-300 focus:outline-none focus:border-indigo-500"
          type="text"
          placeholder="Ingrese su búsqueda"
          v-model="searchWord" />
        <button
          type="submit"
          class="bg-indigo-500 text-white px-6 py-2 rounded-r-lg font-bold hover:bg-indigo-600 transition duration-300">
          Buscar
        </button>
      </form>
    </div>

    <div v-if="searchResults.length > 0" class="mt-4">
      <h2 class="text-xl font-bold text-center text-white">
        Resultados de búsqueda:
      </h2>
      <ul class="mt-2">
        <li
          v-for="result in searchResults"
          :key="result.pageid"
          class="mb-4 bg-white p-4 rounded-lg shadow-md">
          <h3 class="text-lg font-semibold text-black">
            {{ result.title }}
          </h3>
          <p v-html="result.snippet"></p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

export default {
  data() {
    return {
      searchWord: "",
      searchResults: [],
    };
  },
  methods: {
    async handleSearch(event) {
      event.preventDefault();

      if (this.searchWord.trim() === "") {
        toast.error("Por favor, ingrese un valor de búsqueda", {
          position: "bottom-right",
        });
        return;
      }

      try {
        const response = await axios.post("http://localhost:8000/consulta/", {
          palabra_buscada: this.searchWord,
        });

        toast.success("Búsqueda realizada con éxito", {
          position: "bottom-right",
        });

        this.searchWord = "";

        this.searchResults = response.data;
      } catch (error) {
        console.error(error);
        toast.error("Algo salió mal", {
          position: "bottom-right",
        });
      }
    },
  },
};
</script>
