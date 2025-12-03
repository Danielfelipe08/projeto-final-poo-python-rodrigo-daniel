

# 📚 Sistema de Biblioteca – Projeto Final de Orientação a Objetos (2025.2)

Aplicação Web desenvolvida em **Python + Bottle**, seguindo o padrão **MVC** e aplicando os **4 pilares da Orientação a Objetos**.
O sistema permite gerenciar **usuários, livros e empréstimos**, com persistência em arquivos JSON e autenticação de acesso.

---

## ✔️ **Funcionalidades Principais**

### 🔐 **Autenticação**

* Cadastro de usuário
* Login por e-mail e data de nascimento
* Sessão com Beaker
* Proteção de rotas (somente usuários autenticados acessam livros/emprestimos)

### 📘 **Gestão de Livros**

* Listar livros
* Adicionar novo livro

### 📄 **Gestão de Empréstimos**

* Registrar novo empréstimo
* Selecionar usuário e livro
* Listar empréstimos

### 👤 **Gestão de Usuários**

* Listar usuários
* Criar usuário
* Editar usuário
* Excluir usuário

### 🎨 **Interface Web**

* Layout customizado
* Páginas estilizadas com CSS moderno
* Layout responsivo
* Cartões de login/cadastro

---

# 🧱 **Estrutura do Projeto (MVC)**

```
projeto-final-poo-python-rodrigo-daniel/
│
├── app.py
├── main.py
├── config.py
├── Makefile
├── requirements.txt
├── README.md
│
├── controllers/
│   ├── __init__.py
│   ├── auth_controller.py
│   ├── base_controller.py
│   ├── emprestimos_controller.py
│   ├── home_controller.py
│   ├── livros_controller.py
│   ├── login_controller.py
│   └── user_controller.py
│
├── models/
│   ├── __init__.py
│   ├── emprestimo.py
│   ├── livro.py
│   ├── user.py
│   └── usuario_model.py
│
├── services/
│   ├── __init__.py
│   ├── emprestimo_service.py
│   ├── livro_service.py
│   ├── user_service.py
│   └── usuario_service.py
│
├── utils/
│   ├── __init__.py
│   └── auth_middleware.py
│
├── data/
│   ├── emprestimos.json
│   ├── livros.json
│   └── users.json
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   └── js/
│
└── views/
    ├── auth/
    │   ├── login.tpl
    │   └── register.tpl
    │
    ├── emprestimos/
    │   └── index.tpl
    │
    ├── home/
    │   └── index.tpl
    │
    ├── livros/
    │   └── index.tpl
    │
    ├── partials/
    │   ├── base.tpl
    │   ├── helper-final.tpl
    │   ├── layout.tpl
    │   ├── user_form.tpl
    │   └── users.tpl

```

---

# 🧠 **Pilares da Orientação a Objetos Aplicados**

## ✔️ **1. Abstração**

As classes **Livro**, **Emprestimo**, **User**, **Usuario**, **Admin**, **Leitor** abstraem conceitos do domínio real.

---

## ✔️ **2. Encapsulamento**

A classe `Usuario` protege a senha:

```python
self.__senha
def verificar_senha()
```

---

## ✔️ **3. Herança**

```python
class Admin(Usuario)
class Leitor(Usuario)
```

---

## ✔️ **4. Polimorfismo**

Método sobrescrito:

```python
def tem_permissao_admin()
```

Cada tipo de usuário retorna comportamentos diferentes.

---

# 🗂️ **Persistência de Dados**

O projeto usa **JSON** como forma de persistência:

* `users.json`
* `livros.json`
* `emprestimos.json`

Os *services* fazem leitura/escrita encapsulada:

```python
def _load()
def _save()
```

---

# 🚀 **Como Executar o Projeto**

## 1️⃣ Criar ambiente virtual

```sh
python -m venv venv
```

## 2️⃣ Ativar ambiente virtual

### Windows:

```sh
venv\Scripts\activate
```

### Mac/Linux:

```sh
source venv/bin/activate
```

## 3️⃣ Instalar dependências

```sh
pip install -r requirements.txt
```

## 4️⃣ Executar o servidor

```sh
python run.py
```

O sistema abrirá em:

👉 [http://localhost:8080](http://localhost:8080)

---

# 📦 **requirements.txt**

Use este arquivo:

```
bottle
beaker
```





# 🧩 **Diagrama de Classes (Descrição)**

```
Usuario (abstract)
 ├── Admin
 └── Leitor

Livro
Emprestimo

UsuarioService
LivroService
EmprestimoService
```


---

# 👥 **Autores**

| Nome         | GitHub                    |
| ------------ | ------------------------- |
| **Rodrigo Barbosa**  | github.com/RodrigoCBarbosa |
| **Daniel Felipe** | github.com/Danielfelipe08 |






