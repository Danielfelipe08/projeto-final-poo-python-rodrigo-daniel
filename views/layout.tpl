% rebase('base', title=title, session=session)

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{title or "Sistema"}}</title>

    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/style.css">
</head>

<body>

<header class="navbar">
    <div class="container nav-container">
        <h1 class="logo">Biblioteca</h1>

        <nav>
            <ul class="nav-links">
                <li><a href="/">Início</a></li>
                <li><a href="/livros">Livros</a></li>
                <li><a href="/emprestimos">Empréstimos</a></li>

                % if session and session.get('user_id'):
                    <li><a href="/logout" class="logout-btn">Sair</a></li>
                % else:
                    <li><a href="/login">Login</a></li>
                    <li><a href="/register">Registrar</a></li>
                % end
            </ul>
        </nav>
    </div>
</header>

% include("partials/messages.tpl")

<main class="container content">
    {{!base}}   
</main>

</body>
</html>
