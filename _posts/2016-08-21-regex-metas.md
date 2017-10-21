---
layout: post
title:	"Regex - Metas"
date:	2016-08-12 21:00:00
description: Aqui demos continuidade ao assunto sobre expressões regulares.
categories:
- regex
tags:
- regex
img: category-others.png
---

## Introdução

Neste post iremos tratar sobre os metacaracteres, aquela sopa de letrinhas utilizadas em expressões regulares. Basicamente, são símbolos com poderes especiais, onde cada um possui uma função diferente e que veremos no decorrer dos *posts* sobre *regex*. Esses símbolos, embora possuam cada um uma simples função, quando unidos podem gerar expressões bem complexas.

## Objetivo

O objetivo deste post é alcançar uma didática que facilite a aprendizagem sobre expressões regulares, simplificando este processo principalmente para quem for iniciante.

## Metacaractere

### O que é?

> Lembra dos meta-humanos lá do *Static Shock*?

![](http://static.comicvine.com/uploads/original/0/7604/914960-2cgzoyu.jpg)
**Figura 1<sup>[1]</sup>.**

Na nossa introdução já definimos o que são os metacaracteres, *"são símbolos com poderes especiais, onde cada um possui uma função diferente"*. Lembrando que estamos tratando do significado de metacaractere dentro do contexto de expressões regulares.

Podemos, também, definir metacaractere como um caractere ou uma sequência dele com algum significado especial em aplicações computacionais. Ou ainda, um caractere especial em um programa ou dados que fornece informações sobre outros caracteres, podendo expressar uma ideia sobre como processar os caracteres que seguem o metacaractere.

Em suma, precisamos de metacaractere para construirmos nossas expressões regulares.

### Quais são?

> São vários

Em geral, os metacaracteres utilizados para a construção de expressões regulares são os seguintes: <code>. ? * + ^ $ | [] {} () \</code>.

Veremos agora uma lista com os metacaracteres que farão parte dos nossos estudos.

**Tabela 1.** Alguns metacaracteres utilizados em expressões regulares.  

Metacaractere | Nome       | Função
:----------: | ----------- | -----------
.            | Ponto       | Um caracter qualquer
?            | Opcional    | Zero ou um
*            | Asteristico | Zero, um ou mais
+            | Mais        | Um ou mais
^            | Circunflexo | Início da linha
$            | Cifrão      | Fim da linha
\\|          | Ou          | Ou um ou outro
\            | Escape      | Torna literal algum caractere
\b           | Borda       | Início ou fim de palavra
\1           | Retrovisor  | Texto casado no grupo 1
()           | Grupo       | Delimita um grupo
[]           | Lista       | Lista de caracteres permitidos
[^]          | Lista negada| Lista de caracteres proibidos
{n,m}        | Chaves      | De *n* até *m*

Existem outros, eles dependem da aplicação a qual estamos utilizando, no momento focaremos nesses. :)

### E as categorias?

> Hmm...

Já sobre as categorias dos metacaracteres, podemos encontrar materiais que os separam em 4 ou 5 categorias. Particularmente, já encontrei materiais mais completos que abordam uma classificação de até 8 categorias. Mas isso depende da ferramenta que estamos utilizando e no nosso caso focamos em Shell. Então, trataremos das seguintes categorias:

* Especificadores

* Quantificadores

* Âncoras

* Agrupamento

O nome dessas categorias podem variar, o importante é ter a noção da similiaridade que alguns metacaracteres possuem entre si. E essa classificação irá nos ajudar no entendimento do tema. No ponto de vista de quem vos escreve, é interessante conhecermos essa classificação mais por questão de didática, pois, fica mais fácil de aprender agrupando os semelhantes e os detalhando.

## Conclusão

Neste post demos continuidade ao tema tratando um pouco sobre os metacaracteres que nada mais são do que símbolos com poderes especiais. Apresentamos quais são os metacaracteres que iremos focar. Reforçando, existem outros dependendo da aplicação computacional que estaremos utilizando. E por fim, conhecemos uma classificação em 4 grupos ou categorias nos quais podemos separar os metacaracteres de acordo com as suas funções.

## Próximo episódio

No próximo *post* iremos dar continuidade conhecendo os metacaracteres que pertencem a categoria Especificadores, o por que dessa denominação e alguns exemplos práticos para a nossa fixação.

## Referências

[1] - [Google Images](https://www.google.com.br/search?q=meta+humano&biw=1356&bih=614&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiupoK-hL3OAhWGDpAKHfN0CYYQ_AUIBigB#tbm=isch&q=Static+Shock)

>
