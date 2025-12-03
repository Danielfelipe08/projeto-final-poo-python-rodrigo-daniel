% rebase('layout.tpl', title=title)

<h2>Empréstimos</h2>

<form method="post" action="/emprestimos">
    <select name="usuario_id" required>
        % for id, nome in usuarios.items():
            <option value="{{id}}">{{nome}}</option>
        % end
    </select>

    <select name="livro_id" required>
        % for id, titulo in livros.items():
            <option value="{{id}}">{{titulo}}</option>
        % end
    </select>

    <input type="date" name="data" required>

    <button type="submit">Registrar Empréstimo</button>
</form>

<hr>

<ul>
% for e in emprestimos:
    <li>
        {{usuarios[e.usuario_id]}} pegou "{{livros[e.livro_id]}}" em {{e.data}}
    </li>
% end
</ul>
