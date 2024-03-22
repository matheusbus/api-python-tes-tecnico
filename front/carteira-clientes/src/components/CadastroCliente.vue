<template>
    <div class="container my-5">
      <h1 class="px-3">Novo Cliente</h1>
      <div class="form-group px-3">

        <div class="my-3 mb-3">
            <input type="text" v-model="cnpj_input" class="form-control mb-2" id="cnpj" placeholder="CNPJ...">
            <button @click="cadastrarCliente()" class="btn btn-primary">Cadastrar</button>
            <button @click="consultarCnpjReceita()" class="btn btn-warning mx-2">Consultar Receita</button>
        </div>
        <div class="mb-3">
            <textarea v-model="dados_receita" class="form-control" id="dados_receita" rows="20" placeholder="Retorno da consulta na receita..." readonly></textarea>
        </div>
        <a class="btn btn-primary text-white" :href="'/clientes'"><i class="fas fa-arrow-left"></i> Voltar para todos os clientes</a>
      </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                cnpj_input: '',
                dados_receita: '',
            }
        },
        methods: {
            consultarCnpjReceita() {
                let padrao = /[0-9]/g;
                let cnpj_formatado = this.cnpj_input.match(padrao).join('');
                console.log(`https://www.receitaws.com.br/v1/cnpj/${cnpj_formatado}`);
                if (cnpj_formatado != '') {
                    try {
                        fetch(`https://www.receitaws.com.br/v1/cnpj/${cnpj_formatado}`)
                        .then(response => {
                            console.log(response.status)
                            if (!response.status != 200) {
                                throw new Error('Erro ao consultar CNPJ na Receita Federal: ' + response.status);
                            }
                            return response.json();
                        })
                        .then(data => {
                            this.dados_receita = data;
                        })
                        .catch(error => {
                            console.log(error.message);
                            alert(error.message);
                        });
                    } catch (error) {
                        console.log(error.message);
                        alert(error.message);
                    }
                } else {
                    alert('CNPJ não foi informado');
                }
            },
            cadastrarCliente() {
                let cnpj_formatado = this.cnpj_input.trim().replace('/', '').replace('.', '').replace('-', '')
                if (cnpj_formatado != '') {
                    fetch(`http://localhost:8000/api/clientes/register`, {
                        method: 'POST',
                        headers: {
                            'Content-type': 'application/json'
                        },
                        body: JSON.stringify({"cnpj": cnpj_formatado})
                    })
                    .then(response => {
                        if(response.status != 201) {
                            throw new Error('Não foi possível cadastrar o cliente. Verifique o CNPJ informado.')
                        } else {
                            console.log('Cliente cadastrado com sucesso!')
                            this.$router.push({ path: `/clientes`})
                        }
                    })
                    .catch(error => {
                        alert(error.message);
                    })
                } else {
                    alert('CNPJ não foi informado');
                }
            }
        }
    }
</script>

<style></style>