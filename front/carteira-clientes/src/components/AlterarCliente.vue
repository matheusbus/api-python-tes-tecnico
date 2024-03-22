<template>
    <div class="container my-5">
        <h1>Alterar Cliente #{{ cliente.id }}</h1>
    </div>

    <div class="container my-5">
        <form class="form-group">
            <label for="cnpj">Cadastro Nacional de Pessoas Jurídicas</label>
            <input type="text" class="form-control mb-2" id="cnpj" aria-describedby="cnpjHelp" readonly :value="cliente.cnpj">

            <label for="situacao">Situação Cadastral</label>
            <input type="text" class="form-control mb-2" id="situacao" readonly :value="cliente.situacao">

            <label for="tipo">Tipo</label>
            <input type="text" class="form-control mb-2" id="tipo" readonly  :value="cliente.tipo">

            <label for="razao_social">Razão Social</label>
            <input type="text" class="form-control mb-2" id="razao_social" readonly  :value="cliente.razao_social">

            <label for="nome_fantasia">Nome Fantasia</label>
            <input type="text" class="form-control mb-2" id="nome_fantasia" readonly  :value="cliente.nome_fantasia">

            <label for="estado">Estado</label>
            <input type="text" class="form-control mb-2" id="estado" readonly  :value="cliente.estado">

            <label for="municipio">Município</label>
            <input type="text" class="form-control mb-2" id="municipio" readonly  :value="cliente.municipio">

            <label for="logradouro">Logradouro</label>
            <input type="text" class="form-control mb-2" id="logradouro" readonly  :value="cliente.logradouro">

            <label for="bairro">Bairro</label>
            <input type="text" class="form-control mb-2" id="bairro" readonly  :value="cliente.bairro">

            <label for="numero">Número</label>
            <input type="text" class="form-control mb-2" id="numero" readonly  :value="cliente.numero">

            <label for="complemento">Complemento</label>
            <input type="text" class="form-control mb-2" id="complemento" readonly  :value="cliente.complemento">

            <label for="natureza_juridica">Natureza Jurídica</label>
            <input type="text" class="form-control mb-2" id="natureza_juridica" readonly :value="cliente.natureza_juridica">

            <label for="porte">Porte</label>
            <input type="text" class="form-control mb-2" id="porte" readonly :value="cliente.porte">

            <label for="atividade_principal">Atividade Principal</label>
            <textarea class="form-control mb-2" name="atividade_principal" id="atividade_principal" cols="30" rows="10" readonly>{{ cliente.atividade_principal }}</textarea>

            <label for="telefone">Telefone</label>
            <input type="text" class="form-control mb-2" id="telefone" readonly :value="cliente.telefone">

            <label for="numero_funcionarios">Número de funcionários</label>
            <input type="number" class="form-control mb-2" id="numero_funcionarios" v-model="numeroFuncionarios">

            <label for="faturamento_anual_estimado">Faturamento anual estimado</label>
            <input type="number" class="form-control mb-2" id="faturamento_anual_estimado" v-model="faturamentoAnualEstimado">
            
            <label for="vendedor_responsavel">Vendedor Responsável</label>
            <input type="text" class="form-control mb-2" id="vendedor_responsavel" v-model="vendedorResponsavel">
        </form>
        <button class="btn btn-success mr-2" @click="confirmarAlteracao">Confirmar</button>
        <button class="btn btn-danger" @click="cancelarAlteracao">Cancelar</button>
    </div> 
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  computed: {
    ...mapState({
      cliente: state => state.clienteSelecionado
    }),
    numeroFuncionarios: {
      get() {
        return this.cliente ? this.cliente.numero_funcionarios : null;
      },
      set(value) {
        this.atualizarNumeroFuncionarios(value);
      }
    },
    faturamentoAnualEstimado: {
      get() {
        return this.cliente ? this.cliente.faturamento_anual_estimado : null;
      },
      set(value) {
        this.atualizarFaturamentoAnualEstimado(value);
      }
    },
    vendedorResponsavel: {
      get() {
        return this.cliente ? this.cliente.vendedor_responsavel : null;
      },
      set(value) {
        this.atualizarVendedorResponsavel(value);
      }
    }
  },
  methods: {
    ...mapActions([
      'atualizarNumeroFuncionarios',
      'atualizarFaturamentoAnualEstimado',
      'atualizarVendedorResponsavel'
    ]),
    cancelarAlteracao() {
      this.$router.push({ path: '/clientes' })
    },
    confirmarAlteracao() {
        fetch(`http://127.0.0.1:8000/api/cliente/update/${this.cliente.id}/`, {
            method: 'PUT',
            headers: {
                'Content-type': 'application/json',
            },
            body: JSON.stringify({
                "numero_funcionarios": this.numeroFuncionarios,
                "faturamento_anual_estimado": this.faturamentoAnualEstimado,
                "vendedor_responsavel": this.vendedorResponsavel
            })
        })
        .then(response => {
            if(response.status == 201) {
                console.log('Cliente alterado com sucesso!')
                this.$router.push({ path: `/clientes`})
            } else if(response.status == 400) {
                throw new Error('Erro ao cadastrar cliente')
            }
        })
        .catch(error => {
            this.erroRequisicao = error.message
        })
      this.$router.push({ path: '/clientes' });
    }
  }
};
</script>

<style></style>