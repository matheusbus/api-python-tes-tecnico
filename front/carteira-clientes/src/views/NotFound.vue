<template>
    <div class="container my-5 border border-3 rounded p-5 bg-secondary text-white">
        <h3>Ooops!</h3>
        <p>A página que você solicitou não foi encontrada.</p>
        <button class="btn btn-warning" @click="voltar">Voltar para página Inicial</button>
    </div>
</template>

<script>
    export default {
        methods: {
            voltar() {
                this.$router.push({ path: '/clientes' })
            }
        }
    }
</script>

<style>
</style>