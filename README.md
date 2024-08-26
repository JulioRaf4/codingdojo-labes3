# Coding Dojo Banese Labes

## Contextualização

Bem-vindo à Banese Labes Eventos! Você foi recentemente contratado como parte da equipe de desenvolvimento para criar um novo sistema de gerenciamento de eventos. Este sistema permitirá que os organizadores de eventos gerenciem palestrantes, participantes, locais, agenda, feedbacks e administradores. Seu trabalho é implementar as APIs que comporão esse sistema.

### Nova Posição

Você faz parte da equipe de desenvolvimento da Banese Labes Eventos, responsável por criar funcionalidades que serão utilizadas por milhares de organizadores de eventos em todo o mundo. A qualidade e eficiência do seu código irão diretamente impactar a experiência dos nossos clientes e usuários. Prepare-se para desenvolver soluções robustas e eficientes!

## Features a Serem Implementadas

Durante este coding dojo, você e seu grupo serão responsáveis por implementar uma das seguintes features:

1. **Gestão de Palestrantes**
   - Criar novos palestrantes.
   - Listar palestrantes.
   - Buscar palestrantes por CPF.
   - Deletar palestrantes.

   1.1. **Modelo palestrante**  
      - Nome
      - Assunto da palesta
      - CPF

---

2. **Gestão de Participantes**
   - Registrar novos participantes.
   - Listar todos os participantes.
   - Buscar participantes por CPF.
   - Deletar participantes por CPF.

   2.1. **Modelo Participante**  
      - Nome
      - Data de nascimento
      - CPF

---

3. **Gestão de Locais**
   - Cadastrar novos locais para eventos.
   - Listar todos os locais cadastrados.
   - Buscar local por nome.
   - Deletar local por nome.

   3.1. **Modelo do local**  
      - Nome
      - Cidade
      - Estado

---

4. **Gestão da Agenda**
   - Criar novos itens na agenda do evento.
   - Listar todos os itens da agenda.
   - Buscar itens por nome do gestor.
   - Deletar itens da agenda por nome do gestor.

   4.1. **Modelo Agenda**  
      - Nome do gestor que marcou
      - Data e hora
      - Repetiçãp [Diaria, semanal, mensal ...]

---

5. **Gestão de Feedback**
   - Registrar feedbacks dos participantes.
   - Listar todos os feedbacks recebidos.
   - Buscar feedbacks por ID.
   - Deletar feedbacks.
     
   5.1. **Modelo FeedBack**  
      - Avaliação entre 0-10
      - Descricao do feedback
      - Data o feedback foi dado

---

## Instruções para Rodar o Código

Para facilitar o desenvolvimento, este projeto foi configurado para ser executado com o gerenciador de dependências **Poetry**. Siga os passos abaixo para configurar e rodar o código de exemplo:

### 1. Fazer Fork do Repositório

1. Vá para o repositório original no GitHub.
2. Clique no botão "Fork" no canto superior direito da página.
3. Isso criará uma cópia do repositório em sua conta do GitHub.

### 2. Clonar o Repositório

Depois de fazer o fork, você precisa clonar o repositório para sua máquina local.

1. Abra o terminal ou o Git Bash.
2. Navegue até o diretório onde deseja clonar o repositório.
3. Execute o seguinte comando, substituindo `<seu-usuario>` pelo seu nome de usuário no GitHub:

```bash
git clone https://github.com/<seu-usuario>/codingdojo-labes3.git
```

### 3. Instalar Dependências

Com o Poetry instalado, navegue até o diretório raiz do projeto e execute o comando abaixo para instalar todas as dependências necessárias:

```bash
poetry install
```

### 4. Inicie a máquina virtual com as dependências 

Com o Poetry instalado, navegue até o diretório raiz do projeto e execute o comando abaixo para instalar todas as dependências necessárias:

```bash
poetry shell
```