import { createStore } from 'vuex';

export default createStore({
  state: {
    clienteSelecionado: null
  },
  mutations: {
    setClienteSelecionado(state, cliente) {
      state.clienteSelecionado = cliente;
    },
    setNumeroFuncionarios(state, numeroFuncionarios) {
      state.clienteSelecionado.numero_funcionarios = numeroFuncionarios;
    },
    setFaturamentoAnualEstimado(state, faturamentoAnualEstimado) {
      state.clienteSelecionado.faturamento_anual_estimado = faturamentoAnualEstimado;
    },
    setVendedorResponsavel(state, vendedorResponsavel) {
      state.clienteSelecionado.vendedor_responsavel = vendedorResponsavel;
    }
  },
  actions: {
    selecionarCliente({ commit }, cliente) {
      commit('setClienteSelecionado', cliente);
    },
    atualizarNumeroFuncionarios({ commit }, numeroFuncionarios) {
      commit('setNumeroFuncionarios', numeroFuncionarios);
    },
    atualizarFaturamentoAnualEstimado({ commit }, faturamentoAnualEstimado) {
      commit('setFaturamentoAnualEstimado', faturamentoAnualEstimado);
    },
    atualizarVendedorResponsavel({ commit }, vendedorResponsavel) {
      commit('setVendedorResponsavel', vendedorResponsavel);
    },
    saveStateToLocalStorage({ state }) {
      localStorage.setItem('vuex_state', JSON.stringify(state));
    }
  },
  modules: {
  }
});