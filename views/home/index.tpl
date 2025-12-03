% rebase('layout.tpl', title=title, session=session)

<div class="home-container">

    <div class="home-card">

        <h2>Bem-vindo ao Sistema de Biblioteca 📚</h2>

        <p class="home-subtitle">
            Gerencie livros, usuários e empréstimos de forma simples e rápida.
        </p>

        <div class="home-actions">
            <a href="/livros" class="home-btn">📘 Livros</a>
            <a href="/emprestimos" class="home-btn">📄 Empréstimos</a>
            <a href="/users" class="home-btn">👤 Usuários</a>
        </div>

        <a href="/logout" class="logout-link">Sair</a>

    </div>

</div>
