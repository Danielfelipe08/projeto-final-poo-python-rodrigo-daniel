% rebase('layout.tpl', title=title)

<div class="auth-card">

    <h2>Cadastro de Usuário</h2>

    % if error:
        <div class="alert alert-error">
            {{error}}
        </div>
    % end

    <form action="/register" method="post">

        <label for="name">Nome completo:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required>

        <label for="birthdate">Data de nascimento:</label>
        <input type="date" id="birthdate" name="birthdate" required>

        <button type="submit">
            Cadastrar
        </button>
    </form>

    <p class="auth-footer">
        Já possui login?
        <a href="/login">Entrar</a>
    </p>

</div>
