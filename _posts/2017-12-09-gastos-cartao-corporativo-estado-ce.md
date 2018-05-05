---
layout: post
title: Gastos do Cartão Corporativo do Estado do Ceará
date: '2017-12-09 00:00:00 -0300'
img: category-python.png
categories: [python]
tags: [jupyter notebook, data scraping, beautifulsoup, python]

---
[UPDATE]:05/05/2018

## Objetivo

Auxiliar na aprendizagem da técnica de raspagem de dados utilizando Python.

## O Alvo

Portal da Transparência do Governo do Estado do Ceará. URL: http://transparencia.ce.gov.br/content/planejamento-e-execucao-orcamentaria/despesas/cartao-corporativo

## O Desafio

Recuperar dados do Portal da Transparência do Governo do Estado do Ceará sobre gastos do cartão corporativo de responsabilidade do Chefe do Poder Executivo, no período de 2015 a 2018. Calcular a média de gastos e desvio padrão anual e plotar os gastos do cartão corporativo.

## O Algoritmo

O algoritmo inicia com a captura da url que possui as quatro tabelas anuais dos gastos com o cartão corporativo. Onde, primeiramente, são capturados os cabeçalhos de cada tabela. Logo em seguida, os valores de cada mês são tratados.

Cálculos de média e desvio padrão são realizados utilizando a biblioteca numpy e os gráficos são gerados com o pyplot.

## Resultado

É possível gerar as médias e os desvios padrão para os gastos anuais com o cartão corporativo para cada ano (2015, 2016, 2017 e 2018).

```

	Gastos com Cartão Corporativo 2018
	Média de gastos ->   R$   2513.30
	Desvio padrão   -> ± R$   1723.37

	Gastos com Cartão Corporativo 2017
	Média de gastos ->   R$   2524.33
	Desvio padrão   -> ± R$   1865.36

	Gastos com Cartão Corporativo 2016
	Média de gastos ->   R$   1016.25
	Desvio padrão   -> ± R$   979.13

	Gastos com Cartão Corporativo 2015
	Média de gastos ->   R$   786.42
	Desvio padrão   -> ± R$   598.68


```

É possível, também, gerar os gráficos para cada ano em Valor(R$) x Mês e um único gráfico mostrando os gastos dos 4 anos. Abaixo são apresentados 5 gráficos, onde: a) corresponde aos 4 anos; b) corresponde ao ano de 2018; c) corresponde ao ano de 2017; d) corresponde ao ano de 2016; e) corresponde ao ano de 2015.

a) ![Gastos 2015-2018](https://raw.githubusercontent.com/edsonlead/data_scraping/master/003/images/mulplot.png)

b) ![Gastos 2018](https://raw.githubusercontent.com/edsonlead/data_scraping/master/003/images/sinplot-2018.png)

c) ![Gastos 2017](https://raw.githubusercontent.com/edsonlead/data_scraping/master/003/images/sinplot-2017.png)

d) ![Gastos 2016](https://raw.githubusercontent.com/edsonlead/data_scraping/master/003/images/sinplot-2016.png)

e) ![Gastos 2015](https://raw.githubusercontent.com/edsonlead/data_scraping/master/003/images/sinplot-2015.png)

## Considerações

A intenção deste pequeno projeto foi somente a de praticar raspagem de dados utilizando Python. Com isso em mente, melhorias serão aplicadas à ele no decorrer do tempo. Essas melhorias estão descritas em: https://github.com/edsonlead/data_scraping/tree/master/003.

Seria interessante se fosse disponibilizado com o que foi utilizado o cartão corporativo do Estado. Porém, *"Nessa página são disponibilizados os gastos com cartão corporativo que está sob responsabilidade do Chefe do Poder Executivo, cujas informações são disponibilizadas com valores sintéticos a fim de não comprometer a segurança almejada, conforme art. 22º, VII, da Lei 15.175/2012"*. Dessa forma, não há como apresentar aqui os motivos do aumento do gasto em comparação com os anos tratados.
