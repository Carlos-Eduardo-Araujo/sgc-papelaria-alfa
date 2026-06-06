# 📚 SGC - Papelaria Alfa

O Sistema de Gestão Comercial (SGC) - Papelaria Alfa é uma aplicação web Full-Stack desenvolvida por Carlos Eduardo Araújo e João Vitor Carneiro para o gerenciamento de vendas, controle de estoque, carteira de clientes e emissão de relatórios. O sistema possui uma API RESTful robusta protegida por autenticação JWT e uma interface gráfica amigável e responsiva.

---

## ✨ Funcionalidades em Destaque

### 💻 Interface Gráfica (Frontend)
* **Dashboard Interativo:** Tela inicial com atalhos rápidos para todos os módulos do sistema.
* **Gestão de Clientes:** Cadastro, listagem e exclusão de clientes, incluindo dados de contato (telefone/e-mail).
* **Gestão de Produtos:** Controle de estoque detalhado. Possui funcionalidade de **Edição Rápida de Estoque** com 1 clique (consumindo rota PATCH da API) e exclusão de produtos.
* **Frente de Caixa (PDV/Vendas):** Interface de vendas com sistema de **Carrinho de Compras**, permitindo adicionar múltiplos itens e quantidades diferentes antes de finalizar a compra.
* **Relatórios e Histórico:** Listagem completa de vendas com filtro por cliente. Conta com cálculo de faturamento em tempo real e um **Gráfico de Barras** dinâmico gerado com `Chart.js`.
* **Identidade Visual:** Design responsivo com as cores exclusivas da Papelaria Alfa (Azul Marinho e Laranja).

### ⚙️ Motor e Regras de Negócio (Backend / API)
* **Autenticação Segura:** Proteção total das rotas usando Tokens JWT.
* **Recuperação de Senha:** Fluxo de recuperação de senha por e-mail nativo do Django.
* **Validações Estritas:** A API bloqueia vendas sem itens e impede a venda se o produto não tiver estoque suficiente.
* **Automatização:** O valor total da venda é calculado automaticamente pelo backend e o estoque dos produtos é descontado imediatamente após o registro da venda.
* **Documentação Viva:** Documentação automática e interativa de todos os endpoints da API utilizando o **Swagger**.

---

## 🛠️ Tecnologias Utilizadas

**Backend:**
* [Python 3.x](https://www.python.org/)
* [Django](https://www.djangoproject.com/) (Framework web principal)
* [Django REST Framework (DRF)](https://www.django-rest-framework.org/) (Construção da API)
* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/) (Autenticação por Token)
* [drf-yasg](https://drf-yasg.readthedocs.io/) (Geração do Swagger)
* SQLite3 (Banco de Dados relacional)

**Frontend:**
* HTML5, CSS3 e JavaScript (Vanilla / Fetch API)
* [Bootstrap 5](https://getbootstrap.com/) (Estilização e Responsividade)
* [Chart.js](https://www.chartjs.org/) (Renderização de gráficos)

---

## 🏛️ Arquitetura e Padrões de Projeto
O projeto foi estruturado utilizando o padrão arquitetural **MVT (Model-View-Template)**, que é a variação do Django para o MVC. A aplicação foi dividida em camadas lógicas:
* **Models:** Representação das entidades do banco de dados (`Cliente`, `Produto`, `Venda`, `ItemVenda`).
* **Serializers:** Regras de negócio e transformação de dados complexos em JSON.
* **Views/ViewSets:** Controladores da API REST e renderizadores das telas HTML.
* **Templates:** Interface do usuário consumindo a API nativamente via JavaScript assíncrono (`async/await`).

---

## 🚀 Como Executar o Projeto Localmente

Siga o passo a passo abaixo para rodar a aplicação na sua máquina:

### 1. Clonar o Repositório
```bash

git clone [https://github.com/SEU_USUARIO/sgc-papelaria-alfa.git](https://github.com/SEU_USUARIO/sgc-papelaria-alfa.git)
cd sgc-papelaria-alfa

2. Criar e Ativar o Ambiente Virtual
Bash
python -m venv .venv

# No Windows:
.venv\Scripts\activate

# No Linux/Mac:
source .venv/bin/activate

3. Instalar as Dependências

pip install django djangorestframework djangorestframework-simplejwt drf-yasg

(Se você gerou um arquivo requirements.txt, pode usar: pip install -r requirements.txt)

4. Configurar o Banco de Dados (Migrações)

python manage.py makemigrations
python manage.py migrate

5. Criar o Usuário Administrador (Funcionário)
Este usuário será utilizado para fazer o login no sistema.


python manage.py createsuperuser

(Siga os passos na tela digitando usuário, e-mail e senha).

6. Iniciar o Servidor

python manage.py runserver

7. Acessar o Sistema
Interface Web (Login): Abra o navegador e acesse http://127.0.0.1:8000/app/login/

Documentação da API (Swagger): Acesse http://127.0.0.1:8000/swagger/

⚠️ Nota sobre a Recuperação de Senha: Como o sistema está rodando em ambiente de desenvolvimento local, ao testar a funcionalidade de "Esqueci minha senha", o e-mail com o link de recuperação não será enviado para a sua caixa de entrada, mas sim impresso no terminal/console onde o servidor (runserver) está sendo executado.

📂 Documentação Técnica
Os diagramas referentes à modelagem do sistema (Diagrama de Classes, Diagrama Lógico de Banco de Dados e Diagrama de Domínio) encontram-se na pasta docs/ deste repositório (Nota: lembre-se de criar essa pasta e colocar as imagens da Entrega 1 lá).

Desenvolvido para a disciplina de Engenharia de Requisitos / Desenvolvimento Web por Carlos Eduardo Araújo e João Vitor Carneiro.