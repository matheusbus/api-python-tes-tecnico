import { createApp } from 'vue';
import App from './App.vue';
import store from './store';

import TabelaClientes from './components/TabelaClientes.vue';
import CadastroCliente from './components/CadastroCliente.vue';
import DetalhesCliente from './components/DetalhesCliente.vue';
import AlterarCliente from './components/AlterarCliente.vue';
import NotFound from './views/NotFound.vue';

const app = createApp(App);

app.component('TabelaClientes', TabelaClientes);

const routes = [
  { path: '/clientes', name:'clienes', component: TabelaClientes },
  { path: '/clientes/register', component: CadastroCliente },
  { path: '/detalhes/:id', name: 'detalhes', component: DetalhesCliente, props: true },
  { path: '/alterar/:id', name: 'alterar', component: AlterarCliente, props: true },
  { path: '/:catchAll(.*)', name: 'notfound', component: NotFound }
];

import { createRouter, createWebHistory } from 'vue-router';
const router = createRouter({
  history: createWebHistory(),
  routes
});

window.addEventListener('beforeunload', () => {
  store.dispatch('saveStateToLocalStorage');
});

const savedState = localStorage.getItem('vuex_state');
if (savedState) {
  store.replaceState(JSON.parse(savedState));
}

app.use(router);
app.use(store);

app.mount('#app');