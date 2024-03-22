<template>
    <div class="container my-5">
      <h1 class="px-3"><i class="fas fa-user bg-primary p-3 rounded whitecoloricon"></i> Carteira de Clientes</h1>
    </div>
    <div class="container">
      <div class="form-group px-3">
        <div class="row">
          <div class="col">
            <input type="text" v-model="filtro" class="form-control mb-2" id="filtro" placeholder="Nome do vendedor...">
          </div>
          <div class="col">
            <button @click="aplicarFiltro" class="btn btn-primary"><i class="fas fa-filter"></i> Filtrar</button>
            <button @click="limparFiltro" class="btn btn-primary mx-2"><i class="fas fa-times"></i> Limpar</button>
          </div>
        </div>
      </div>
      <div class="container mb-5">
        <a class="btn btn-success" :href="'/clientes/register'"><i class="fas fa-plus"></i> Novo Cliente</a>
      </div>
      <div class="container">
        <div class="table-responsive">
          <table class="table table-stripedtable table-striped table-hover table table-bordered">
            <thead class="thead-dark">
              <tr>
                <th scope="col">#</th>
                <th scope="col">CNPJ</th>
                <th scope="col">Razão Social</th>
                <th scope="col">Situação</th>
                <th scope="col">Faturamento</th>
                <th scope="col">Funcionários</th>
                <th scope="col">Vendedor</th>
                <th scope="col">#</th>
                <th scope="col">#</th>
                <th scope="col">#</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="cliente in clientes" :key="cliente.id">
                <th scope="row">{{ cliente.id }}</th>
                <td>{{ cliente.cnpj }}</td>
                <td>{{ cliente.nome_fantasia ? cliente.nome_fantasia : cliente.razao_social }}</td>
                <td>{{ cliente.situacao }}</td>
                <td>R${{ cliente.faturamento_anual_estimado ? cliente.faturamento_anual_estimado : '0.00'  }}</td>
                <td>{{ cliente.numero_funcionarios }}</td>
                <td>{{ cliente.vendedor_responsavel }}</td>
                <td>
                  <button class="btn btn-secondary" @click="visualizarItem(cliente)" title="Visualizar detalhes"><i class="fas fa-eye"></i></button>
                </td>
                <td>
                  <button class="btn btn-warning" @click="alterarItem(cliente)" title="Alterar cadastro"><i class="fas fa-pencil-alt"></i></button>
                </td>
                <td>
                  <button class="btn btn-danger" @click="excluirItem(cliente.id)" title="Excluir cadastro"><i class="fas fa-trash"></i></button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <router-view></router-view>
    </div>
  </template>
  
<script>
    export default {
        data() {
            return {
                filtro: '',
                clientes: [],
                clienteSelecionado: null
            };
        },
        mounted() {
            this.obterClientes();
        },
        methods: {
            selecionarCliente(cliente) {
              this.clienteSelecionado = cliente;
            },
            aplicarFiltro() {
                if(!this.filtro.trim()) {
                    this.obterClientes();
                } else {
                    this.filtrarClientes();
                }
            },
            obterClientes() {
                fetch('http://localhost:8000/api/clientes/')
                    .then(response => response.json())
                    .then(data => {
                        this.clientes = data;
                });
            },
            filtrarClientes() {
                fetch('http://localhost:8000/api/clientes/')
                    .then(response => response.json())
                    .then(data => {
                        this.clientes = data.filter(cliente => cliente.vendedor_responsavel.toLowerCase().trim() == this.filtro.toLowerCase().trim());
                    })
                    .catch(error => {
                        alert(error)
                    });
            },
            limparFiltro() {
                this.filtro = ''
                this.obterClientes();
            },
            visualizarItem(cliente) {
                this.$store.dispatch('selecionarCliente', cliente);
                this.$router.push({ name: 'detalhes', params: { id: cliente.id } });
            },
            alterarItem(cliente) {
                this.$store.dispatch('selecionarCliente', cliente);
                this.$router.push({ name: 'alterar', params: { id: cliente.id } });
            },
            excluirItem(cliente_id) {
              fetch(`http://localhost:8000/api/clientes/${cliente_id}/`, {
                  method: 'DELETE',
              })
              .then(response => {
                  if(response.status === 204) {
                      this.obterClientes();
                  } else {
                      throw new Error('Resposta inesperada do servidor: ' + response.status);
                  }
              })
              .catch(error => {
                  console.log(error);
              });
            }
        }
    };
</script>
  
<style>
  .whitecoloricon {
    color: white;
  }
</style>
