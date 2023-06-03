<template>
  <div class="flex justify-center items-center h-96">
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
      } catch (error) {
        console.error(error);
        toast.error("Algo salio mal", {
          position: "bottom-right",
        });
      }
    },
  },
};
</script>
