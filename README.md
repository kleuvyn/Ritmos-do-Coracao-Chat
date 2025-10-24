# Chatbot "Ritmos do Coração"

## Descrição do Projeto

O **Chatbot “Ritmos do Coração”** é um assistente conversacional **inteligente e sustentável (Custo Zero)**, criado para otimizar o processo de **Captação de Recursos (Doações)** da ONG **Ritmos do Coração**.

Desenvolvido com o **Rasa Open Source**, o chatbot atua como um ponto de contato **24 horas por dia, 7 dias por semana**, garantindo uma comunicação empática, organizada e eficiente.

### Objetivos Principais

- **Gerenciar Fluxos Complexos (Multi-Nível)**  
  Administra as **14 opções de doação** com jornadas detalhadas (exemplo: passo a passo da **Nota Fiscal Paulista**), evitando que o doador se perca.

- **Fornecer Dados Críticos com Precisão**  
  Entrega rápida e segura de informações essenciais (CNPJs, dados bancários, links de pagamento e endereços).

- **Assegurar Sustentabilidade Financeira**  
  O uso do **Rasa self-hosted** elimina custos por alto volume de mensagens, permitindo deploy em **Free Tiers** de nuvem (sem custo).

---

## Tecnologias Utilizadas

| Categoria | Tecnologia | Versão Mínima | Finalidade |
|:--|:--|:--|:--|
| **Framework Base** | [Rasa Open Source](https://rasa.com/open-source/) | `rasa>=3.x` | Motor de IA Conversacional (NLU e Core) |
| **Linguagem** | Python | `3.8+` | Base para o framework e ações customizadas |
| **Infraestrutura** | Docker / Docker Compose | `20.10.x` | Facilita execução e deploy em produção |

---

## Pré-Requisitos

Antes de iniciar, certifique-se de ter instalados:

1. **Python** `3.8+` e **pip**  
2. **Git** (para clonar o repositório)  
3. *(Opcional, recomendado para produção)* **Docker** e **Docker Compose**

---

## Instalação e Execução

### Passo 1 — Clonar o Repositório

```bash
git clone [INSIRA_O_LINK_DO_SEU_REPOSITORIO]
cd chatbot-ritmos-do-coracao
````

---

### Passo 2 — Configuração e Instalação (Ambiente Local)

Se não for usar Docker, siga os passos abaixo:

**1. Criar e ativar o ambiente virtual**

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# Windows: .venv\Scripts\activate
```

**2. Instalar as dependências**

```bash
pip install -r requirements.txt
```

---

### Passo 3 — Treinar e Testar o Chatbot

**Treinar o modelo**

```bash
rasa train
```

**Iniciar conversa no terminal**

```bash
rasa shell
```

> Digite `/stop` ou use `Ctrl + C` para encerrar a conversa.

---

### Passo 4 — Execução Completa (Com Ações Customizadas)

Para testar fluxos complexos e lógicas personalizadas do arquivo `actions/actions.py`, abra **dois terminais**:

**Terminal 1 — Rasa Core (Gerenciamento de Diálogo):**

```bash
rasa run --enable-api --cors "*"
```

**Terminal 2 — Servidor de Ações Customizadas:**

```bash
rasa run actions
```

> O **Rasa Core** roda na porta `5005`
> O **Servidor de Ações** roda na porta `5055`

---

## Exemplos de Uso

| Mensagem do Usuário                      | Intenção Capturada  | Resposta Esperada                         |
| :--------------------------------------- | :------------------ | :---------------------------------------- |
| “Queria saber como doar dinheiro”        | `doar_dinheiro`     | Mostra menu: PIX, TED ou Boleto           |
| “Qual o CNPJ da Nota Fiscal Paulista?”   | `informar_cnpj_nfp` | Exibe o CNPJ e o link para adesão         |
| “Qual o endereço para levar as doações?” | `doar_itens`        | Informa o endereço e solicita agendamento |
| “Tenho dúvida sobre o Pix”               | `duvida_pix`        | Explica chaves PIX e confirmações         |

---

## Estrutura do Projeto

```
.
├── actions/             # Ações customizadas (Python)
│   └── actions.py
├── data/                # Dados de treinamento
│   ├── nlu.yml          # Intenções e entidades (NLU)
│   ├── stories.yml      # Histórias de conversação (Core)
│   └── rules.yml        # Regras diretas (fallbacks, saudações)
├── config.yml           # Configuração do pipeline e políticas do Rasa
├── domain.yml           # Intenções, respostas e ações registradas
└── requirements.txt     # Dependências Python
```

---

## Execução com Docker (Opcional)

Se preferir usar Docker, crie um arquivo **`docker-compose.yml`** com o seguinte conteúdo:

```yaml
version: '3.0'
services:
  rasa:
    image: rasa/rasa:3.6.20
    ports:
      - "5005:5005"
    volumes:
      - ./:/app
    command: ["run", "--enable-api", "--cors", "*"]

  actions:
    image: rasa/rasa-sdk:3.6.2
    ports:
      - "5055:5055"
    volumes:
      - ./actions:/app/actions
```

**Iniciar os serviços:**

```bash
docker-compose up
```

---

## Contribuições

Contribuições são **muito bem-vindas!** 
Se você quiser sugerir melhorias, reportar bugs ou adicionar novas funcionalidades:

* Abra uma **Issue** descrevendo sua ideia ou problema.
* Envie um **Pull Request** com suas alterações.

