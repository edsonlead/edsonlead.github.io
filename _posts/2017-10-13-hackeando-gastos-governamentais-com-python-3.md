---
layout: post
title: Hackeando Gastos Governamentais com Python 3
date: '2017-10-13 23:42:33 -0300'
img: category-python.png
categories: [python]
tags: [jupyter notebook, beautifulsoup, python]

---

\[UPDATE\]: 09/11/2017

Ontem, 12 de outubro, aproveitei para publicar um pequeno projeto que desenvolvi em alguns dias. Postei nos grupos do Facebook Python Brasil e A.P.D.A., al&eacute;m da minha timeline. Obtive um feedback bem legal e maior do que eu esperava. E neste post iremos tratar sobre esse projeto.

&Eacute; de conhecimento comum que d&aacute; pra fazer v&aacute;rias coisas com uma linguagem de programa&ccedil;&atilde;o. Aprender tudo sobre uma &eacute; praticamente imposs&iacute;vel, para meros mortais. Por isso, &eacute; importante encontrar um foco. Em tese, deve ser algo desafiador e que desperte o interesse de quem est&aacute; escrevendo os c&oacute;digos. Eu fui atr&aacute;s do meu foco, se encontrei eu n&atilde;o sei. Mas estou gostando de raspagem de dados.

J&aacute; acompanho h&aacute; um tempo o trabalho do Professor Fernando Ashikaga. Ele ministra cursos e palestras sobre raspagem de dados. Acompanhei pelo YouTube uma dessas palestras realizada pela Roadsec SP.

<iframe width="100%"  src="https://www.youtube.com/embed/pM68J2JA72U" frameborder="0" ></iframe>

A partir dessa palestra eu fiquei ainda mais interessado em raspagem de dados e pensei em me desafiar. E como atualmente se fala bastante em gastos e or&ccedil;amento do governo, resolvi utilizar o <a href="http://portaltransparencia.gov.br/" target="_blank">Portal da Transpar&ecirc;ncia do Governo Federal</a> como objeto de estudo.

## As Ferramentas

Comecei meus estudos pela documenta&ccedil;&atilde;o do Beautiful Soup<sup>[1]</sup>. Tinha que ser com Python. E nisso fui passando algumas noites aprendendo coisas novas, inclusive o Jupyter Notebook<sup>[2]</sup>. Eu utilizava mais o vim e o iPython. O Pyplot<sup>[3]</sup> foi utilizado para a plotagem dos gr&aacute;ficos.

Uma defini&ccedil;&atilde;o r&aacute;pida sobre o Beautiful Soup:

<blockquote>"Beautiful Soup &eacute; uma biblioteca Python para extrair dados de arquivos HTML e XML. Ele funciona com o seu analisador favorito para fornecer maneiras idiom&aacute;ticas de navegar, pesquisar e modificar a &aacute;rvore de an&aacute;lise. Geralmente economiza horas ou dias de trabalho do programador."<sup>[1]</sup></blockquote>

Agora, uma defini&ccedil;&atilde;o r&aacute;pida sobre o Jupyter Notebook:

<blockquote>"O notebook amplia a abordagem baseada em console para a computa&ccedil;&atilde;o interativa em uma dire&ccedil;&atilde;o qualitativamente nova, fornecendo uma aplica&ccedil;&atilde;o baseada na web adequada para capturar todo o processo de computa&ccedil;&atilde;o: desenvolvimento, documenta&ccedil;&atilde;o e execu&ccedil;&atilde;o de c&oacute;digo, al&eacute;m de comunicar os resultados."<sup>[2]</sup></blockquote>

E sobre o Pyplot:

<blockquote>"Matplotlib.pyplot &eacute; uma cole&ccedil;&atilde;o de fun&ccedil;&otilde;es de estilo de comando que fazem Matplotlib funcionar como MATLAB. Cada fun&ccedil;&atilde;o pyplot faz alguma altera&ccedil;&atilde;o em uma figura: por exemplo, cria uma figura, cria uma &aacute;rea de tra&ccedil;ado em uma figura, tra&ccedil;a algumas linhas em uma &aacute;rea de tra&ccedil;ado, decora o gr&aacute;fico com r&oacute;tulos, etc."<sup>[3]</sup></blockquote>

## O Desafio

O desafio teve como objetivo auxiliar na aprendizagem da t&eacute;cnica de raspagem de dados. Ele foi: realizar raspagem de dados no Portal da Transpar&ecirc;ncia e apresentar graficamente os gastos diretos de alguns &oacute;rg&atilde;os superiores, desde o in&iacute;cio da inser&ccedil;&atilde;o dos dados no portal at&eacute; o ano atual. Os &oacute;rg&atilde;os escolhidos foram: Presid&ecirc;ncia da Rep&uacute;blica; Minist&eacute;rio da Ci&ecirc;ncia, Tecnologia, Inova&ccedil;&atilde;o e Comunica&ccedil;&otilde;es; Minist&eacute;rio da Educa&ccedil;&atilde;o; Minist&eacute;rio da Previd&ecirc;ncia Social; Minist&eacute;rio da Sa&uacute;de; Minist&eacute;rio do Meio Ambiente; e Minist&eacute;rio do Esporte. Nenhum motivo especial foi utilizado na escolha desses &oacute;rg&atilde;os.

Para isso, o primeiro passo foi verificar os padr&otilde;es tanto das urls quanto do html das p&aacute;ginas, al&eacute;m de identificar os dados que devem ser extra&iacute;dos. O html da p&aacute;gina &eacute; igual para todos os anos e &oacute;rg&atilde;os superiores, e os dados se encontram exatamente dentro das mesmas posi&ccedil;&otilde;es e marca&ccedil;&otilde;es html. Depois de anotar esses padr&otilde;es, passamos para o algoritmo.

![Portal Transparencia]({{site.baseurl}}/assets/img/post006/post06-portal.png)


![Portal Transparencia Fonte]({{site.baseurl}}/assets/img/post006/post06-portal-fonte.png)

## O Algoritmo

Basicamente, o algorimto inicia com a captura da url referente a cada &oacute;rg&atilde;o superior, captura os dois valores de "class=colunaValor" pertencente a marca&ccedil;&atilde;o "
\<td>", sendo o de interesse o segundo que &eacute; refente ao valor destinado ao &oacute;rg&atilde;o. Ap&oacute;s isso, temos um tratamento para retirar o que n&atilde;o for de interesse, deixando apenas o valor do segundo&nbsp; "class=colunaValor". O valor de cada ano, ap&oacute;s passar por esse tratamento, &eacute; adicionado dentro de uma lista. Essa string deve ser convertida em float para colocar todos os valores em uma &uacute;nica unidade, pois, como os gr&aacute;ficos devem representar esses dados, nada melhor do que deix&aacute;-los da forma mais amig&aacute;vel poss&iacute;vel. A unidade escolhida foi bilh&atilde;o de reais com base em todos os dados.

Dessa forma, temos para cada &oacute;rg&atilde;o superior uma lista de valores em bilh&otilde;es de reais desde o ano de 2004 at&eacute; o ano de 2017. Com isso, junto com uma lista contendo os anos (2004, 2005..., 2017), os gr&aacute;ficos foram plotados da forma Em bilh&otilde;es de R$ (eixo y) X Ano (eixo x) para cada um deles. O c&oacute;digo tamb&eacute;m possui uma fun&ccedil;&atilde;o para plotar todos os &oacute;rg&atilde;os em um &uacute;nico gr&aacute;fico ou escolher quais queremos comparar.

## Resultados

&Eacute; poss&iacute;vel gerar os gr&aacute;ficos por &oacute;rg&atilde;o superior, isso totaliza 7 gr&aacute;ficos. Somado a isso, o c&oacute;digo permite plotar gr&aacute;ficos com mais de um &oacute;rg&atilde;o superior, o que &eacute; ideal quando se quer comparar gr&aacute;ficos. Abaixo s&atilde;o apresentados 4 gr&aacute;ficos, onde: a) compara os gastos entre todos os órgãos superiores já citados; b) mostra os gastos com a educação; c) mostra os gastos com a saúde; d) mostra os gastos com a previdência privada; e e) mostra os gastos com a presidência da república.

a) ![Gráfico 01]({{site.baseurl}}/assets/img/post006/post06-graf01.png)

b) ![Gráfico 02]({{site.baseurl}}/assets/img/post006/post06-graf02.png)

c) ![Gráfico 03]({{site.baseurl}}/assets/img/post006/post06-graf03.png)

d) ![Gráfico 04]({{site.baseurl}}/assets/img/post006/post06-graf04.png)

e) ![Gráfico 04]({{site.baseurl}}/assets/img/post006/post06-graf05.png)

A inten&ccedil;&atilde;o deste pequeno projeto foi somente a de aprender e praticar raspagem de dados utilizando Python. Em rela&ccedil;&atilde;o as an&aacute;lises acerca do momento econ&ocirc;mico e pol&iacute;tico no qual o Pa&iacute;s vive(u) fica por conta do leitor. Vale ressaltar que esses valores s&atilde;o os divulgados pelo pr&oacute;prio Governo.

O c&oacute;digo completo pode ser encontrado no meu GitHub: <a href="https://github.com/edsonlead/data_scraping/blob/master/001/" target="_blank" rel="noopener">https://github.com/edsonlead/data_scraping/blob/master/001/</a>. Ainda irei aplicar algumas melhorias e quem sabe outras fun&ccedil;&otilde;es. Caso tenha alguma sugest&atilde;o ou coment&aacute;rio, fa&ccedil;a bom uso das issues: <a href="https://github.com/edsonlead/data_scraping/issues" target="_blank" rel="noopener">https://github.com/edsonlead/data_scraping/issues</a> ou no espa&ccedil;o para coment&aacute;rios aqui neste post.

<blockquote>Agrade&ccedil;o ao Juliano Garcia, Anderson Rezende e Roberto Sousa pela ajuda na representa&ccedil;&atilde;o gr&aacute;fica dos dados, ao Prof Fernando Ashikaga pela inspira&ccedil;&atilde;o e divulga&ccedil;&atilde;o dos seus conhecimentos. E a todos que deram um feedback nas publica&ccedil;&otilde;es que postei. Voc&ecirc;s me motivaram ainda mais.</blockquote>

Obrigado por ler at&eacute; aqui. :)

## Refer&ecirc;ncias

1 <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank" rel="noopener">https://www.crummy.com/software/BeautifulSoup/bs4/doc/</a>

2 <a href="http://jupyter-notebook.readthedocs.io/en/latest/notebook.html" target="_blank" rel="noopener">http://jupyter-notebook.readthedocs.io/en/latest/notebook.html</a>

3 <a href="https://matplotlib.org/users/pyplot_tutorial.html" target="_blank" rel="noopener">https://matplotlib.org/users/pyplot_tutorial.html</a>
