from django.shortcuts import render

elenco = {
    'atletas': [
        {'foto': 'images/rafael.jpg', 'nome': 'Rafael', 'idade': 36, 'posicao': 'Goleiro', 'nascimento': 'Brasil'},
        {'foto': 'images/arboleda.jpg', 'nome': 'Robert Arboleda', 'idade': 33, 'posicao': 'Zagueiro', 'nascimento': 'Equador'},
        {'foto': 'images/alan_franco.png', 'nome': 'Alan Franco', 'idade': 28, 'posicao': 'Zagueiro', 'nascimento': 'Argentina'},
        {'foto': 'images/wendell.jpg', 'nome': 'Wendell', 'idade': 32, 'posicao': 'Lateral Esquerdo', 'nascimento': 'Brasil'},
        {'foto': 'images/cedric.webp', 'nome': 'Cédric Soares', 'idade': 33, 'posicao': 'Lateral Direito', 'nascimento': 'Portugal'},
        {'foto': 'images/luiz_gustavo.webp', 'nome': 'Luiz Gustavo', 'idade': 37, 'posicao': 'Volante', 'nascimento': 'Brasil'},
        {'foto': 'images/damian_bobadilla.webp', 'nome': 'Damián Bobadilla', 'idade': 24, 'posicao': 'Volante', 'nascimento': 'Paraguai'},
        {'foto': 'images/lucas_moura.webp', 'nome': 'Lucas Moura', 'idade': 33, 'posicao': 'Meia Atacante', 'nascimento': 'Brasil'},
        {'foto': 'images/ferrerinha.jpg', 'nome': 'Ferreirinha', 'idade': 27, 'posicao': 'Ponta Esquerda', 'nascimento': 'Brasil'},
        {'foto': 'images/lucas_ferreira.jpg', 'nome': 'Lucas Ferreira', 'idade': 19, 'posicao': 'Ponta Direita', 'nascimento': 'Brasil'},
        {'foto': 'images/andre_silva.webp', 'nome': 'André Silva', 'idade': 26, 'posicao': 'Centroavante', 'nascimento': 'Brasil'}
    ]
}

info_site = {
    'titulo': 'São Paulo Futebol Clube',
    'historia': 'O São Paulo Futebol Clube foi fundado em 25 de janeiro de 1930, fruto da união de dissidentes do Club Athletico Paulistano e da Associação Athlética das Palmeiras. A ata de fundação foi assinada na madrugada do dia seguinte (26 de janeiro), mas oficialmente o clube considera como data magna o dia 25, em homenagem ao aniversário da cidade de São Paulo.',
    'autores': ['João Victor e Elias Renner']
}

def inicio(request):
    return render(request, 'website/inicio.html', {'info': info_site})

def equipe(request):
    return render(request, 'website/equipe.html', elenco)

def sobre(request):
    return render(request, 'website/sobre.html', {'info': info_site})