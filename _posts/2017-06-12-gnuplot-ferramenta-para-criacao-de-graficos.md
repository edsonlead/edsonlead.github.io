---
layout: post
title: "Gnuplot: ferramenta para criação de gráficos"
date: '2017-06-12 09:15:54 -0300'
img: category-others.png
categories: [plot]
tags: [gnuplot, gráficos, plot]
---
Embora receba em seu nome o termo GNU, essa ferramenta não possui uma licença ligada a GPL e muito menos possui relação com o projeto GNU. O <a href="http://gnuplot.info" target="_blank">Gnuplot</a> trata-se de uma freeware, ou seja, você não precisa pagar para utilizá-lo mas também não possui permissão para modificar o seu código fonte<sup>1</sup>.

O gnuplot &eacute; uma ferramenta multiplataforma de linha de comando para cria&ccedil;&atilde;o de gr&aacute;ficos. Foi criado para auxiliar estudantes e cientistas a visualizar de forma interativa dados e fun&ccedil;&otilde;es matem&aacute;ticas. Outras aplica&ccedil;&otilde;es como o Octave<sup>2</sup>, por exemplo, utiliza o gnuplot como engine para plotar gr&aacute;ficos.

Ele d&aacute; suporte a plotagem de gr&aacute;ficos 2D, 3D e gif, e scripts podem ser utilizados. Scripts? Sim, scripts. O legal de trabalhar com essa ferramenta por linha de comando &eacute; a possibilidade de plotar gr&aacute;ficos tanto de forma interativa quanto por meio de scripts. E &eacute; isso o que veremos neste post.

## Instalação do gnuplot

O download do gnuplot pode ser realizado em seu reposit&oacute;rio no sourceforget (<a href="https://sourceforge.net/projects/gnuplot/files/" target="_blank">repositório gnuplot</a>). Em sistemas Linux &eacute; comum que o gnuplot esteja em seus reposit&oacute;rios. Ent&atilde;o, para instal&aacute;-lo basta seguir um dos seguintes comandos:

Para dpkg (exemplo: Debian):
{% highlight terminal %}
$ sudo apt-get install gnuplot
{% endhighlight %}

Para rpm (exemplo: Fedora):
{% highlight terminal %}
$ sudo dnf install gnuplot
{% endhighlight %}

## Executando o gnuplot

Ap&oacute;s a instala&ccedil;&atilde;o, no terminal, podemos executar o gnuplot da seguinte maneira: $ gnuplot. Na forma interativa podemos inserir alguns comandos e o gr&aacute;fico s&oacute; ser&aacute; plotado ao inserir o comando plot.

![Gnuplot]({{site.baseurl}}/assets/img/post002/post02-gnuplot.png)

Uma outra forma de utiliz&aacute;-lo &eacute; atrav&eacute;s de scripts com extens&atilde;o .plt e que segue o seguinte formato de execu&ccedil;&atilde;o $ gnuplot arquivo.plt.

## Exemplos Práticos

Aqui &eacute; apresentado tr&ecirc;s exemplos de utiliza&ccedil;&atilde;o do gnuplot. N&atilde;o &eacute; a inten&ccedil;&atilde;o decifrar linha por linha dos escripts, mas sim, dar no&ccedil;&atilde;o de funcionamento da ferramenta e plotagem dos gr&aacute;ficos. O primeiro exemplo ir&aacute; abordar o uso do gnuplot via linha de comando e os dois &uacute;ltimos via scripts.

<em><strong>Gr&aacute;fico da fun&ccedil;&atilde;o seno</strong></em>

Esse primeiro exemplo &eacute; algo bem b&aacute;sico, apenas para familiariza&ccedil;&atilde;o, que podemos trabalhar direto no terminal. Acessando o gnuplot realizamos a plotagem da fun&ccedil;&atilde;o seno que abrir&aacute; uma janela apresentando o gr&aacute;fico dessa fun&ccedil;&atilde;o. Logo ap&oacute;s, temos a inser&ccedil;&atilde;o de dois comandos respons&aacute;veis por setar os intervalos em valores para os eixos x e y. Para que essas altera&ccedil;&otilde;es possam ser visualizadas faz-se necess&aacute;rio um replot.

{% highlight bash %}
$ gnuplot
gnuplot> plot sin(x)
gnuplot> set xrange [0:10]
gnuplot> set yrange [-2:2]
gnuplot> replot
{% endhighlight %}

Atrav&eacute;s da janela do gnuplot existe a possibilidade de salvar o gr&aacute;fico em formato PDF, SVG e imagem. O resultado:

![Gnuplot]({{site.baseurl}}/assets/img/post002/post02-dados1.png)

<em><strong>Utilizando dados de arquivo</strong></em>

Neste exemplo trabalhamos com dados de um arquivo externo, que foi denominado de dados.txt, e o seu conte&uacute;do &eacute; mostrado a seguir:

{% highlight terminal %}
    10.835    32.394
    18.714    31.073
    26.593    29.393
    34.472    27.467
    42.352    25.353
    50.231    23.227
    58.110    21.067
    65.989    19.013
    73.868    17.078
    81.748    15.070
    89.627    13.188
    97.506    11.401
   105.385     9.723
   113.264     8.132
   121.144     6.581
   129.023     5.268
   136.902     3.964
   144.781     2.781
   152.660     1.627
   160.540     0.621
   168.419    -0.317
   176.298    -1.153
   184.177    -1.925
   192.056    -2.820
   199.936    -3.599
   207.815    -4.235
   215.694    -4.780
   223.573    -5.211
   231.452    -5.484
   239.332    -5.752
   247.211    -6.004
   255.090    -6.185
   262.969    -6.490
   270.848    -6.566
   278.728    -6.783
   286.607    -6.702
   294.486    -6.634
   302.365    -6.554
   310.244    -6.436
   318.124    -6.213
   326.003    -6.103
   333.882    -5.890
   341.761    -5.789
   349.640    -5.545
   357.520    -5.442
   365.399    -5.113
{% endhighlight %}

As colunas representam os eixos cartesianos x e y, respectivamente. O script para a constru&ccedil;&atilde;o do gr&aacute;fico foi denominado de dados.plt, onde a fonte escolhida para o gr&aacute;fico foi Verdana em negrito de tamanho 9. Diferente do exemplo anterior, este salva o gr&aacute;fico em imagem com o nome de dados.png e possui um enconding que pode ser necess&aacute;rio para mostrar palavras acentuadas e o "&ccedil;". Nele tamb&eacute;m foi configurado para que os valores do eixo x sejam mostrados de 100 em 100 e os do eixo y de 10 em 10. Por fim, &eacute; inserido o arquivo que possui os dados a serem apresentados graficamente, assim como o nome da linha e a sua cor.

{% highlight bash %}
set terminal pngcairo enhanced font 'Verdana-Bold,9'
set output 'dados.png'
set encoding iso_8859_1
set title "Gráfico utilizando dados de arquivo"
set xlabel "Eixo X"
set ylabel "Eixo y"
set xtics 100
set ytics 10
plot "dados.txt" title "Linha verde" lc rgb "green" with lines
{% endhighlight %}

O resultado:

![Gnuplot]({{site.baseurl}}/assets/img/post002/post02-dados.png)

<em><strong>Utilizando dados de mais de um arquivo</strong></em>

Aqui o arquivo dados.txt foi dividido em outros dois, onde um possui somente a primeira coluna e outro somente a segunda coluna. O script anterior tamb&eacute;m foi alterado setando intervalos para os eixos cartesianos iniciando-os pelo valor zero. E a legenda do gr&aacute;fico recebeu estilo de box e espa&ccedil;amento. Observe que os arquivos foram inseridos dentro do mesmo plot.

{% highlight bash %}
set terminal pngcairo enhanced font 'Verdana-Bold,9'
set output 'dados2.png'
set encoding iso_8859_1
set title "Gráfico utilizando dados de arquivo"
set xlabel "Eixo X"
set ylabel "Eixo y"
set xrange [0:20]
set yrange [0:50]
set key top font "2" box 3 spacing 3
plot "dados1.txt" title "Linha vermelha" lc rgb "red" with lines,\
"dados2.txt" title "Linha azul" lc rgb "blue" with lines
{% endhighlight %}

O resultado:

![Gnuplot]({{site.baseurl}}/assets/img/post002/post02-dados2.png)

## Mais informações

Para maiores informa&ccedil;&otilde;es acerca de software &eacute; sempre importante verificar a sua man page, no caso: $ man gnuplot

E, logicamente, a documenta&ccedil;&atilde;o (<a href="http://gnuplot.info/docs_5.0/gnuplot.pdf" target="_blank">gnuplot.pdf</a>) presente no seu site oficial, onde al&eacute;m da documenta&ccedil;&atilde;o consta alguns exemplos (<a href="http://gnuplot.sourceforge.net/demo_5.0/" target="_blank">demo gnuplot</a>) para testes e aprendizagem.

Para quem prefere livros, duas recomenda&ccedil;&otilde;es s&atilde;o feitas pelo site oficial do gnuplot. S&atilde;o eles: <a href="https://www.packtpub.com/big-data-and-business-intelligence/gnuplot-cookbook" target="_blank"> Phillips, L. gnuplot Cookbook. Packt Publishing, 2012</a> <a href="https://www.manning.com/books/gnuplot-in-action-second-edition" target="_blank"> Janert, P. K. Gnuplot in Action - Understanding Data with Graphs. Manning Publications, 2&ordf; Ed., 2016</a><sup>3</sup>.

## Finalizando...

Aqui tratamos de forma breve sobre uma ferramenta desenvolvida para o meio acad&ecirc;mico, mas que sem d&uacute;vidas pode ser utilizada em outros contextos. Como apresentado, a sua instala&ccedil;&atilde;o &eacute; simples e a sua aprendizagem pode demadar algum tempo dependendo dos estilos que voc&ecirc; deseja aplicar em seus gr&aacute;ficos.

E a&iacute;? Voc&ecirc; j&aacute; conhecia o Gnuplot? J&aacute; o utilizou? Conhece alguma outra ferramenta alternativa? Pois conte para gente&nbsp;a sua experi&ecirc;ncia e&#47;ou opini&atilde;o nos coment&aacute;rios. O seu feedback &eacute; sempre bem-vindo.

## Referências

1 <a href="http://www.gnuplot.info/faq/faq.html#x1-120001.7" target="_blank">http://www.gnuplot.info/faq/faq.html#x1-120001.7</a>

2 <a href="https://www.gnu.org/software/octave/" target="_blank">https://www.gnu.org/software/octave/</a>

3 <a href="http://gnuplot.info/books.html" target="_blank">http://gnuplot.info/books.html</a>
