<!-- App.vue -->
<template>
  <div class="container">
    <div class="card">
      <header class="card-header">
        Busca de Operadoras
      </header>
      
      <div class="search-section">
        <div class="search-wrapper">
          <input 
            v-model="searchQuery" 
            @keyup.enter="buscarOperadora"
            type="text" 
            placeholder="Digite nome ou CNPJ"
          />
          <button 
            @click="buscarOperadora"
            :disabled="loading"
          >
            Buscar
          </button>
        </div>
      </div>

      <div v-if="operadora" class="result-section">
        <div class="result-header">
          Informações da Operadora
        </div>
        <div class="result-content">
          <div class="json-display">
            <pre class="json-text">{{ JSON.stringify(operadora, null, 2) }}</pre>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      searchQuery: '',
      operadora: null,
      loading: false,
      error: null
    }
  },
  methods: {
    async buscarOperadora() {
      // Limpar resultados anteriores
      this.operadora = null;

      // Validar entrada
      if (!this.searchQuery.trim()) {
        return;
      }

      // Iniciar loading
      this.loading = true;

      try {
        // Fazer a requisição
        const response = await axios.get(`http://127.0.0.1:5000/buscar_operadora`, {
          params: { q: this.searchQuery }
        });

        // Atualizar dados
        this.operadora = response.data;
      } catch (err) {
        // Tratar erros
        console.error(err);
      } finally {
        // Finalizar loading
        this.loading = false;
      }
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
  font-family: 'Arial', sans-serif;
}

.card {
  width: 100%;
  max-width: 500px;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  overflow: hidden;
}

.card-header {
  background-color: #007bff;
  color: white;
  padding: 15px;
  text-align: center;
  font-weight: bold;
}

.search-section {
  padding: 15px;
}

.search-wrapper {
  display: flex;
}

.search-wrapper input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px 0 0 4px;
}

.search-wrapper button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 0 4px 4px 0;
}

.result-section {
  background-color: #f8f9fa;
  padding: 15px;
}

.result-header {
  margin-bottom: 10px;
  color: #333;
  font-weight: bold;
}

.json-display {
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  max-height: 300px;
  overflow-y: auto;
}

.json-text {
  color: #333;
  margin: 0;
  padding: 10px;
  white-space: pre-wrap;
  word-break: break-word;
  font-size: 13px;
  line-height: 1.4;
}
</style>