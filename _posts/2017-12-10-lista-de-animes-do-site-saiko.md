---
layout: post
title: Lista de Animes do Site Saiko
date: '2017-12-10 00:00:00 -0300'
img: category-python.png
categories: [python]
tags: [jupyter notebook, data scraping, beautifulsoup, python]

---

## Objetivos

Esse foi um projeto bem simples que possuiu dois objetivos:

* Auxiliar na aprendizagem da técnica de raspagem de dados utilizando Python;
* Criar um formato de lista que o site Saiko não possui e disponibilizá-lo na web.

## O Alvo

O site de animes Saiko. URL: https://saikoanimes.com/legendados/

## O Desafio

Como o site Saiko possui apenas listas de animes com figuras, *o que demanda um pouco a mais de tempo e dados de conexão para o processamento das páginas*, o desafio foi de recuperar dados desses animes e criar uma lista com apenas o nome, link para download e nota dos animes. Apenas os animes legendados foram escolhidos devido a sua maior quantidade.

## O Algoritmo

O algoritmo inicia com a captura da url que possui 9 páginas, sendo que todas elas possuem um total de 42 animes (com exceção da última página que possui 41 animes). A url padrão das páginas dos animes legendados é: https://saikoanimes.com/legendados/?fwp_paged= . Para cada página, cada anime é capturado de acordo com a tag "\<div class='anime'\>". E para cada anime é capturado dados referentes ao nome (\<div class='listtittle'\>), link para download (\<a href...\>) e nota (\<div class='rwp-users-score-value'\>).

Para a visualização desses dados é criado uma estrutura html, onde dentro de uma tabela são adicionados dados dos animes referentes a uma página. Dessa forma, cada página possui a sua tabela. A estrutura em html é salvo no arquivo list_anime.html.

## Resultado

É possível visualizar o arquivo list_anime.html em um navegador. Para melhorar a visualização do resultado, o bootstrap framework foi utilizado para estilizar o arquivo, que pode ser visto em: http://edsonlead.com/list_anime

![Lista de animes 1]({{site.url}}/assets/img/post008/figure_1.png)

## Considerações

Embora seja uma brincadeira, a ideia partiu de um pequeno comentário que me fizeram sobre a lista de animes do site Saiko *"Eu não gosto de lista assim porque demora muito pra carregar a página"*. E de fato, o site é muito bom, mas tem esse detalhe.

No momento, não se tem melhorias para aplicar ao código-fonte a não ser a refatoração do mesmo. Caso, tenha alguma sugestão fique a vontade para comentar este post. Uma descrição e código-fonte pode ser encontrado em: https://github.com/edsonlead/data_scraping/tree/master/004.
