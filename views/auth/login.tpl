% rebase('layout.tpl', title=title, session=session)

<div class="auth-card">

    <h2>Login</h2>

    % if error:
        <div class="alert alert-error">
            {{error}}
        </div>
    % end

    <form action="/login" method="post">

        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required>

        <label for="birthdate">Data de nascimento:</label>
        <input type="date" id="birthdate" name="birthdate" required>

        <button type="submit">
            Entrar
        </button>
    </form>

    <p class="auth-footer">
        Não possui conta?
        <a href="/register">Cadastre-se</a>
    </p>

</div>
