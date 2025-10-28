# Ritmos-do-Coracao-Chat

Este é um chatbot desenvolvido com Rasa para auxiliar usuários com informações sobre doações para a ONG Projeto Ritmos do Coração.

## Funcionalidades
- Fornece informações sobre diferentes métodos de doação (Nota Fiscal Paulista, Pix, transferências bancárias, cartões, doações de itens, entregas presenciais).
- Respostas em português.
- Fluxo conversacional guiado por regras.

## Como executar
1. Certifique-se de que o Python 3.8+ está instalado e um ambiente virtual está ativado.
2. Instale as dependências: `pip install rasa`
3. Treine o modelo: `rasa train`
4. Execute o chatbot: `rasa run`
5. Para ações customizadas: `rasa run actions` (em outro terminal)
6. Teste no shell: `rasa shell`

## Teste via API
Para integrar com um frontend personalizado:
1. Treine o modelo: `rasa train`
2. Execute as ações: `rasa run actions` (terminal 1)
3. Execute o servidor: `rasa run --cors "*"` (terminal 2)
4. Faça requisições POST para `http://localhost:5005/webhooks/rest/webhook`

## Estrutura do Projeto
- `config.yml`: Configuração do pipeline e políticas.
- `domain.yml`: Definições de intenções, ações e respostas.
- `data/`: Dados de treinamento (NLU, regras e stories).
- `actions/`: Ações customizadas em Python.
- `models/`: Modelos treinados (gerados automaticamente).
- `tests/`: Testes de conversas.

## Contribuição
Para contribuir, edite os arquivos de dados e treine novamente o modelo.

