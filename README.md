# Tars-OpenFinance
<p align="center"></p>

## Descrição
<h1>TARS - IA contra fraudes de pagamento instantâneo</h1>
<p>
Somos uma feature de um Bank as a Service. para instituições que trabalham com PIX ou FedNow.
O TARS irá diminuir os riscos de seus clientes caírem em uma fraude de pagamentos instantâneos.
O cliente não precisará aprender ou se adaptar a nenhuma nova plataforma financeira ou fintech. O TARS atuará no próprio aplicativo do banco.
</p>

## Tecnologias utilizadas

## Integrantes:
- <a href="https://www.linkedin.com/in/raduanmuarrek/">Raduan Muarrek</a>
- <a href="https://www.linkedin.com/in/rodrigo-campos-8b70191ab/">Raphael Lisboa</a>
- <a href="https://www.linkedin.com/in/raphael-lisboa-antunes-a41919231/">Rodrigo Campos</a>
- <a href="https://www.linkedin.com/in/vitor-moura-de-oliveira/">Vitor Moura</a>

## Estrutura de pastas


## Documentos

##Modo de uso da solução.

1. Faça o clone deste repositório

2. No seu terminal ou vscode, intale os seguintes algoritimos:
.Flask 
.Skelearn
.Pandas

3. rode o seguinte comando: python api.py

4. No postman, você precisará passar um json contendo as seguintes atributos:

{'availableAmount': 4213.0, 'amount': 12210.0, 'schedules': 11110.0, 'incomePerMonth': 11430.0, 'patrimony': 200.0, 'standardDeviation': 320.0, 'transactionDay': 230.0, 'transactionMonth': 430.0}

Os atributos numéricos podem ser alterados, você utilizará esse json para realizar as requisições no postman, poís são com esses atributos que nosso modelo foi treinado

5. No postman, com seu servidor no ar, insirá o endereço de ip https://0.0.0.0:5000/predict

6.Altere o tipo de texto para json e insirá seu json, clique para enviar a requisição e veja que você recebeu um atributo chamado "outlier", que indica 1 ou 0. 1 significa que a transação é fraudulenta e 0 que a transação é comum


## Referências

