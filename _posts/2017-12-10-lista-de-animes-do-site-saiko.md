---
layout: post
title: Lista de Animes do Site Saiko
date: '2017-12-10 00:00:00 -0300'
img: category-python.png
categories: [python]
tags: [jupyter notebook, data scraping, beautifulsoup, python]

---

Para treinar raspagem de dados foi utilizado como objeto de estudos um site que conheci recentemente. Ele tem um layout bem legal, o webdesigner deixou as marcações html em uma forma aceitável para o nosso estudo, ótimo para download de animes e seus colaboradores dispobilizam o calendário de lançamento dos episódios. Porém, não possui a tradicional lista de animes sem os pôsters e é recheado de propaganda com redirecionamento de páginas (isso me deixa louco kkk), o que é bom para começarmos a brincar. =D

## Objetivos

Esse foi um projeto bem simples que possuiu três objetivos:

* Auxiliar na aprendizagem da técnica de raspagem de dados utilizando Python;
* Criar um formato de lista que o site Saiko não possui;
* Facilitar o download dos episódios.

## O Alvo

O site de animes Saiko. URL: https://saikoanimes.com

## O Desafio

Como o site Saiko possui apenas listas de animes com figuras e muito redirecionamento de páginas, *o que demanda um pouco a mais de tempo e dados de conexão para o processamento das páginas (fora um pouco de dor de cabeça)*, o desafio foi de recuperar dados desses animes e criar uma lista com apenas pôster de anime, o nome, link para acesso no site Saiko, nota e episódios dos animes.

Basicamente, o desafio foi o de facilitar o download dos episódios de animes desse site. Apenas os animes legendados foram escolhidos devido a sua maior quantidade.

## O Algoritmo

O algoritmo inicia com a captura da url que possui 9 páginas, sendo que todas elas possuem um total de 42 animes (com exceção da última página que possui 41 animes). A url padrão das páginas dos animes legendados é: https://saikoanimes.com/legendados/?fwp_paged=. Para cada página, cada anime é capturado de acordo com a tag "\<div class="anime"\>". E para cada anime é capturado dados referentes ao pôster (\<img), ao nome (\<div class="listtittle"\>), link para acesso ao site (\<a href...\>), nota (\<div class="rwp-users-score-value"\>) e lista dos episódios para download (\<div class="list").

Para a visualização desses dados é criado uma estrutura html, onde dentro de uma tabela são adicionados dados dos animes referentes a uma página. Dessa forma, cada página possui a sua tabela que foi numerada devidamente. A estrutura em html é salva no arquivo list_anime.html.

## Resultado

É possível visualizar o arquivo list_anime.html em um navegador. O bootstrap framework foi utilizado para estilizar o arquivo, que pode ser visto em: http://edsonlead.com/list_anime

![Lista de animes 1]({{site.url}}/assets/img/post008/figure_1.png)
![Lista de animes 2]({{site.url}}/assets/img/post008/figure_2.png)
![Lista de animes 3]({{site.url}}/assets/img/post008/figure_3.png)

Com essa listagem de animes é possível verificar que alguns animes não possui lista de episódios, são eles: Brotherhood: Final Fantasy XV, Cowboy Bebop: Tengoku no Tobira, Darker than Black: Kuro no Keiyakusha Gaiden, Date A Live Movie: Mayuri Judgment, Fukumenkei Noise, Hellsing Ultimate, Isekai no Seikishi Monogatari e Z/X: Ignition.

De um total de 377 animes postados no site, cerca de 8 desses animes não possui lista de episódios disponíveis para download.

## Considerações

Embora seja uma brincadeira, a ideia partiu de dois pequenos comentários que me fizeram sobre o site Saiko *"Eu não gosto de lista assim porque demora muito pra carregar a página"* e ainda *"O meu adblock bloqueou o site"*. E de fato, o site é muito bom, mas têm esses detalhes que ajudaram nos estudos com raspagem de dados.

No momento, não se tem melhorias em mente para aplicar ao código-fonte a não ser a refatoração do mesmo. Caso, tenha alguma sugestão fique a vontade para comentar este post. Uma descrição e código-fonte pode ser encontrado em: https://github.com/edsonlead/data_scraping/tree/master/004.
