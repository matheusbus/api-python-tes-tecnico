<template>
    <div class="container my-5">
        <h1>Detalhes do Cliente #{{ cliente.id }}</h1>
    </div>

    <div class="container my-5">
        <form class="form-group">
            <div class="row">
                <div class="col-md-6">
                    <label for="cnpj">Cadastro Nacional de Pessoas Jurídicas</label>
                    <input type="text" class="form-control mb-2" id="cnpj" aria-describedby="cnpjHelp" readonly :value="cliente.cnpj">
                </div>
                <div class="col-md-6">
                    <label for="situacao">Situação Cadastral</label>
                    <input type="text" class="form-control mb-2" id="situacao" readonly :value="cliente.situacao">
                </div>
            </div>

            <div class="row">
                <div class="col md-6">
                    <label for="tipo">Tipo</label>
                    <input type="text" class="form-control mb-2" id="tipo" readonly  :value="cliente.tipo">
                </div>
                <div class="col md-6">
                    <label for="razao_social">Razão Social</label>
                    <input type="text" class="form-control mb-2" id="razao_social" readonly  :value="cliente.razao_social">
                </div>
            </div>


            <label for="nome_fantasia">Nome Fantasia</label>
            <input type="text" class="form-control mb-2" id="nome_fantasia" readonly  :value="cliente.nome_fantasia">

            <div class="row">
                <div class="col">
                    <label for="estado">Estado</label>
                    <input type="text" class="form-control mb-2" id="estado" readonly  :value="cliente.estado">
                </div>

                <div class="col">
                    <label for="municipio">Município</label>
                    <input type="text" class="form-control mb-2" id="municipio" readonly  :value="cliente.municipio">
                </div>
            </div>

            <div class="row">
                <div class="col">
                    <label for="logradouro">Logradouro</label>
                    <input type="text" class="form-control mb-2" id="logradouro" readonly  :value="cliente.logradouro">
                </div>
                <div class="col">
                    <label for="bairro">Bairro</label>
                    <input type="text" class="form-control mb-2" id="bairro" readonly  :value="cliente.bairro">
                </div>
                <div class="col">
                    <label for="numero">Número</label>
                    <input type="text" class="form-control mb-2" id="numero" readonly  :value="cliente.numero">
                </div>
            </div>


            <label for="complemento">Complemento</label>
            <input type="text" class="form-control mb-2" id="complemento" readonly  :value="cliente.complemento">

            <div class="row">
                <div class="col">
                    <label for="natureza_juridica">Natureza Jurídica</label>
                    <input type="text" class="form-control mb-2" id="natureza_juridica" readonly :value="cliente.natureza_juridica">
                </div>
                <div class="col">
                    <label for="porte">Porte</label>
                    <input type="text" class="form-control mb-2" id="porte" readonly :value="cliente.porte">
                </div>
            </div>

            <label for="atividade_principal">Atividade Principal</label>
            <textarea class="form-control mb-2" name="atividade_principal" id="atividade_principal" cols="30" rows="10" readonly>{{ cliente.atividade_principal }}</textarea>

            <label for="telefone">Telefone</label>
            <input type="text" class="form-control mb-2" id="telefone" readonly :value="cliente.telefone">

            <div class="row">
                <div class="col">
                    <label for="numero_funcionarios">Número de funcionários</label>
                    <input type="text" class="form-control mb-2" id="numero_funcionarios" readonly :value="cliente.numero_funcionarios">
                </div>
                <div class="col">
                    <label for="faturamento_anual_estimado">Faturamento anual estimado</label>
                    <input type="text" class="form-control mb-2" id="faturamento_anual_estimado" readonly :value="cliente.faturamento_anual_estimado">
                </div>
                <div class="col">
                    <label for="vendedor_responsavel">Vendedor Responsável</label>
                    <input type="text" class="form-control mb-2" id="vendedor_responsavel" readonly :value="cliente.vendedor_responsavel"> 
                </div>
            </div>
        </form>
        <a class="btn btn-primary btn-block my-5" href="/clientes" role="button"><i class="fas fa-arrow-left"></i> Voltar para Clientes</a>
    </div> 
</template>

<script>
    import { mapState } from 'vuex';

    export default {
        computed: {
            ...mapState({
                cliente: state => state.clienteSelecionado
            })
        },
        mounted() {
        }
    };
</script>

<style></style>