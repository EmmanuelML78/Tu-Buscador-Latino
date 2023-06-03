<template>
  <Loading
    v-model:active="isLoading"
    :can-cancel="false"
    :is-full-page="true" />
  <div class="flex flex-col items-center justify-center pt-10">
    <h2 class="text-white text-2xl font-bold mb-4">INFORME</h2>

    <table class="table-fixed w-[80%] mx-auto">
      <thead>
        <tr>
          <th class="justify-center text-left text-white px-4 py-2">
            Palabra buscada
          </th>
          <th class="flex justify-center text-left text-white px-4 py-2">
            Cantidad de búsquedas
          </th>
          <th class="justify-center text-left text-white px-4 py-2">
            Primera búsqueda
          </th>
          <th class="justify-center text-left text-white px-4 py-2">
            Última búsqueda
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="consulta in consultas" :key="consulta.id">
          <td class="text-white px-4 py-2">{{ consulta.palabra_buscada }}</td>
          <td class="flex justify-center text-white px-4 py-2 items-center">
            {{ consulta.cantidad_busquedas }}
          </td>
          <td class="justify-center text-white px-4 py-2">
            {{ formatDate(consulta.primera_busqueda) }}
          </td>
          <td class="justify-center text-white px-4 py-2">
            {{ formatDate(consulta.ultima_busqueda) }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/css/index.css";

export default {
  name: "Informe",
  components: {
    Loading,
  },
  data() {
    return {
      consultas: [],
      isLoading: true,
    };
  },
  mounted() {
    this.getConsultas();
  },
  methods: {
    getConsultas() {
      axios
        .get("http://localhost:8000/consultas/")
        .then((response) => {
          this.consultas = response.data;
          this.isLoading = false;
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    formatDate(dateString) {
      const options = {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
      };
      return new Date(dateString).toLocaleDateString("es-ES", options);
    },
  },
};
</script>
