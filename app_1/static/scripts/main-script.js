
document.addEventListener('DOMContentLoaded', function() {
    const botoesRegiao = document.querySelectorAll('.region-option');

    botoesRegiao.forEach(function(botao) {
        botao.addEventListener('click', function() {
            const nomeRegiao = botao.getAttribute('data-name');
            const imgRegiao = botao.getAttribute('data-img');
            const descricaoRegiao = botao.getAttribute('data-description');
            const listaPokemon = botao.getAttribute('data-lista-pokemon')

            const contentMenu = document.getElementById('content-menu');
            contentMenu.innerHTML = `
                <h1 id='content-title'>Essa é a Região de ${nomeRegiao}</h1>
                <img id='content-img' src='${imgRegiao}' alt='region-img'>
                <p id='content-description'>${descricaoRegiao}</p>
                <div class="search-container">
                    <button class="search-button">Search Pokemon </button>
                    <input type="text" class="search-input" placeholder="Enter the National ID Pokemon">
                </div>
                <p class = 'text'>${listaPokemon} </p>
                `;
            });
        });
    });
