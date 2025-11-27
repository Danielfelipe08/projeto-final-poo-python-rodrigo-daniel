% rebase('layout.tpl', title=title)

<div style="max-width: 500px; margin: 50px auto; padding: 25px; background: #fff; border-radius: 8px; box-shadow: 0 0 10px #ddd;">

    <h2 style="text-align: center; margin-bottom: 20px;">Cadastro de Usuário</h2>

    % if error:
        <div style="background:#ffdddd; padding:10px; border:1px solid #ff8888; border-radius:5px; margin-bottom:20px;">
            {{error}}
        </div>
    % end

    <form action="/register" method="post">

        <label for="name">Nome completo:</label>
        <input type="text" id="name" name="name" required style="width:100%; padding:8px; margin-bottom:12px;">

        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required style="width:100%; padding:8px; margin-bottom:12px;">

        <label for="birthdate">Data de nascimento:</label>
        <input type="date" id="birthdate" name="birthdate" required style="width:100%; padding:8px; margin-bottom:20px;">

        <button type="submit" style="width:100%; padding:10px; background:#4a68ff; color:white; border:none; border-radius:6px; cursor:pointer;">
            Cadastrar
        </button>
    </form>

    <p style="text-align:center; margin-top:15px;">
        Já possui login?
        <a href="/login">Entrar</a>
    </p>

</div>
