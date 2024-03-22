from django.db.models import Max
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.views import APIView
import requests

class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class NovoClienteAPIView(APIView):
    def post(self, request):
        cnpj = request.data.get('cnpj')
        cnpj = self.formata_cnpj(cnpj)

        proximo_id = Cliente.objects.aggregate(Max('id'))['id__max'] + 1

        if not cnpj or cnpj == '':
            return Response(data='O CNPJ não foi fornecido.', status=status.HTTP_400_BAD_REQUEST)

        dados_receita = self.buscar_dados_receita(cnpj)

        if dados_receita and dados_receita['status'] != 'ERROR':
            cliente = Cliente(
                id=proximo_id,
                cnpj=cnpj,
                situacao=dados_receita['situacao'],
                tipo=dados_receita['tipo'],
                razao_social=dados_receita['nome'],
                nome_fantasia=dados_receita['fantasia'],
                estado=dados_receita['uf'],
                municipio=dados_receita['municipio'],
                logradouro=dados_receita['logradouro'],
                bairro=dados_receita['bairro'],
                numero=dados_receita['numero'],
                complemento=dados_receita['complemento'],
                natureza_juridica=dados_receita['natureza_juridica'],
                porte=dados_receita['porte'],
                atividade_principal=dados_receita['atividade_principal'][0]['text'],
                telefone=dados_receita['telefone'],
                numero_funcionarios=0,
                faturamento_anual_estimado=0,
                vendedor_responsavel=''
            )

            dados_cliente = {
                'id': proximo_id,
                'cnpj': cliente.cnpj,
                'situacao': cliente.situacao,
                'tipo': cliente.tipo,
                'razao_social': cliente.razao_social,
                'nome_fantasia': cliente.nome_fantasia,
                'estado': cliente.estado,
                'municipio': cliente.municipio,
                'logradouro': cliente.logradouro,
                'bairro': cliente.bairro,
                'numero': cliente.numero,
                'complemento': cliente.complemento,
                'natureza_juridica': cliente.natureza_juridica,
                'porte': cliente.porte,
                'atividade_principal': cliente.atividade_principal,
                'telefone': cliente.telefone,
                'numero_funcionarios': 0,
                'faturamento_anual_estimado' : 0,
                'vendedor_responsavel' : 'Não cadastrado',
            }

            serializer = ClienteSerializer(data=dados_cliente)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=dados_receita['message'], status=status.HTTP_400_BAD_REQUEST)


    def buscar_dados_receita(self, cnpj):
        consulta = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')

        if consulta.status_code == 200:
            return consulta.json()
        else:
            print(f'Erro ao consultar dados na Receita Federal: {consulta.status_code}')
            return None

    def formata_cnpj(self, cnpj):
        formatado = cnpj.replace('.', '').replace('/', '').replace('-', '')
        return formatado    
    
class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(data="Cliente deletado com sucesso.", status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
    
class AllClienteListView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class ClienteUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer    
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        
        if not serializer.is_valid(raise_exception=True):
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)