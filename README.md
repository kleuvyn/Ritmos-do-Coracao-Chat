# Chatbot "Ritmos do Coração"

## Descrição do Projeto

O Chatbot "Ritmos do Coração" é um assistente conversacional inteligente e **sustentável (Custo Zero)**, desenvolvido para otimizar o processo de Captação de Recursos (Doações) da ONG.

Construído com o **Rasa Open Source**, o *chatbot* atua como um ponto de contato 24/7, garantindo a conversão de doações ao:

* **Gerenciar Fluxos Complexos (Multi-Nível):** Lida com as 14 opções de doação e jornadas detalhadas (Ex: passo-a-passo da Nota Fiscal Paulista), assegurando que o doador não se perca.
* **Fornecer Dados Críticos com Precisão:** Entrega rápida e precisa de informações essenciais (CNPJs, dados bancários, links de pagamento e endereços).
* **Assegurar Sustentabilidade Financeira:** O uso do Rasa, auto-hospedado (*self-hosted*), elimina o risco de custos por alto volume de uso e permite o *deploy* em **Níveis Gratuitos de Cloud (*Free Tiers*)**.

## Tecnologias e Componentes

| Categoria | Tecnologia | Versão Mínima | Finalidade |
| :--- | :--- | :--- | :--- |
| **Framework Base** | Rasa Open Source | `rasa>=3.x` | Motor principal de IA Conversacional (NLU e Core). |
| **Linguagem** | Python | `3.8+` | Linguagem base para o *framework* e Ações Customizadas. |
| **Infraestrutura** | Docker / Docker Compose | `20.10.x` | Facilita a execução em produção (Deploy). |

## Pré-Requisitos

Para rodar o projeto localmente, você precisa ter as seguintes ferramentas instaladas:

1.  **Python** (`3.8+`) e **pip**
2.  **Git** (Para clonar o repositório)

Se optar por rodar via Docker (recomendado para simular o ambiente de produção):
3.  **Docker e Docker Compose**

---

## Instruções de Instalação e Execução

### Passo 1: Clone o Repositório

```bash
git clone [INSIRA_O_LINK_DO_SEU_REPOSITORIO]
cd chatbot-ritmos-do-coracao

Passo 2: Configuração e Instalação (Opção de Desenvolvimento)

Se você não for usar o Docker, siga estes passos para configurar o ambiente Python:

    Crie e Ative o Ambiente Virtual:
    Bash

python3 -m venv .venv
source .venv/bin/activate  # Para Linux/Mac
# No Windows: .venv\Scripts\activate

Instale o Rasa e as Dependências:
Bash

    pip install -r requirements.txt

Passo 3: Treinamento e Teste Rápido

Treine o modelo e comece a interagir com o chatbot no shell (terminal):
Bash

# 1. Treinar o modelo
rasa train

# 2. Iniciar a conversa interativa (apenas texto)
rasa shell 
# Digite '/stop' ou use Ctrl+C para sair

Passo 4: Execução Completa com Ações Customizadas (Via API)

Para testar a lógica complexa (que está no arquivo actions/actions.py) e simular o ambiente de produção, é necessário rodar dois serviços em terminais separados.

    Terminal 1 (Rasa Core - Gerenciamento de Diálogo):
    Bash

rasa run --enable-api --cors "*"

Terminal 2 (Servidor de Ações Customizadas):
Bash

    rasa run actions

    O Rasa Core estará disponível na porta 5005 e o Servidor de Ações na porta 5055.

Guia de Funcionalidades (Exemplos de Uso)

Mensagem do Usuário	Intenção Capturada (Rasa NLU)	Resultado (Rasa Core)
Queria saber como doar dinheiro	doar_dinheiro	Apresenta o menu de opções: PIX, TED ou Boleto.
Qual o CNPJ da Nota Fiscal Paulista?	informar_cnpj_nfp	Entrega a informação crítica e o link para adesão.
qual o endereço pra levar as doações	doar_itens	Solicita agendamento e apresenta o endereço.
Tenho dúvida sobre o Pix	duvida_pix	Esclarece o fluxo do PIX, chaves e confirmação.

Estrutura do Repositório

.
├── actions/             # Lógica de negócio e Ações Customizadas em Python
│   └── actions.py
├── data/
│   ├── nlu.yml          # Dados para o NLU (Intenções e Entidades)
│   ├── stories.yml      # Fluxos de conversação baseados em IA
│   └── rules.yml        # Regras estritas (Ex: saudações, fallbacks)
├── config.yml           # Configurações do modelo Rasa (NLU e Core)
├── domain.yml           # Define Intenções, Respostas, Entidades e Ações
└── requirements.txt     # Dependências Python do projeto

Contribuições

Contribuições são bem-vindas! Se você tiver sugestões, bugs para reportar ou melhorias a implementar, por favor, abra uma Issue ou submeta um Pull Request.
