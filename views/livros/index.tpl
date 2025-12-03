% rebase('layout.tpl', title=title)

<h2>Livros</h2>

<form method="post" action="/livros">
    <input type="text" name="titulo" placeholder="Título" required>
    <input type="text" name="autor" placeholder="Autor" required>
    <input type="number" name="ano" placeholder="Ano" required>
    <button type="submit">Adicionar</button>
</form>

<hr>

<ul>
% for l in livros:
    <li>
        <b>{{l.titulo}}</b> — {{l.autor}} ({{l.ano}})
    </li>
% end
</ul>
