---
layout: post
title:	"Regex - Starting"
date:	2016-07-03 16:00:00
description: Aqui começamos o nosso primeiro post no qual trataremos sobre expressões regulares.
categories:
- regex
tags:
- regex
img: category-others.png
---

## Introdução

Neste post trataremos de um tema que tenho focado nos últimos meses. Caso você seja um usuário de derivados do Unix já deve ter se deparado com este tema pelo menos por *command line*. Sem dúvidas é bem legal de se trabalhar com expressões regulares, assim como é estudá-las. Dá pra se sentir um ser supremo diante dos seus amigos de TI que não conseguem entender essa sopa de (meta)?caracteres, que no final é algo bem simples de entender. A complexidade dessas expressões dependem da sua prática e do problema que você procura solucionar.

### Objetivo

O objetivo deste post: simplificar as coisas. Mostrar de forma fácil e objetiva que expressões regulares são divertidas e fáceis de aprender. Na verdade, é como a maioria das coisas em computação, você somente aprende praticando. Caso você seja um iniciante no assunto, iremos aqui definir um norte para os seus estudos. Caso o contrário, seja bem vindo para complementar este texto com seus comentários pertinentes ao tema com o intuito de ajudar o estagiário.

## Expressões regulares

> Tudo (in)?certo para começarmos(?\|!)

Neste item vamos conhecer um pouco da história das expressões regulares para entendermos as suas origens e os seus aspectos. Isso parece coisa de humanas, mas é interessante conhecermos um pouco da ferramenta que utilizaremos, o que de fato ela é e em que momentos ela nos poderá ser útil.

### A História

> Uma imagem vale mais do que mil palavras

![Vamos Simplificar](https://brainmoda.files.wordpress.com/2013/01/history.png "Resumo da ópera")

**Figura 1<sup>[1]</sup>.**

*Warren McCulloch* e *Walter Pitts*, em 1943, publicaram um trabalho, [*A logical calculus of the ideas immanent in nervous activity*](http://link.springer.com/article/10.1007/BF02478259), no qual foi desenvolvido uma teoria em relação ao funcionamento dos neurônios humanos. Em 1956, o matemático *Stephen Kleene* desenvolveu algebricamente esse modelo e apresentou em uma publicação, [*Representation of events in nerve nets and finite automata*](http://www.dlsi.ua.es/~mlf/nnafmc/papers/kleene56representation.pdf), neste estudo símbolos foram utilizados para representar seus *regular sets*<sup>[1]</sup>. A partir daí nasceram as expressões regulares.

Porém, apenas em 1968, *Ken Thompson*, o pioneiro do Unix, publicou o seu trabalho [*Regular expression search algorithm*](http://www.fing.edu.uy/inco/cursos/intropln/material/p419-thompson.pdf). Ele implementou seu algoritmo de busca no editor QED. Posteriormente, esse editor virou o editor padrão dos sistemas Unix, o Ed. Ele aceitava expressões regulares seguindo essa sintaxe:<code>g/< regular expression >/p</code>, onde, *g* de *Global* e *p* de *Print* (*Global Regular Expression Print*). Agora você sabe esse detalhe sobre o <code>grep</code> e a sua raiz com as expressões regulares. Em 1979, *Alfred Aho* o extendeu para o <code>egrep</code><sup>[1]</sup>.

O <code>sed</code> e <code>awk</code> foram desenvolvidos, mas o primeiro pacote de expressão regular surgiu na linguagem C, em 1986, e de forma gratuita. A partir de então o seu uso foi ampliado para diversos programas e linguagens.

### O que é?

> "MAZUQUEISSO? MAZUQUEISSO? MAZUQUEISSO?"

Basicamente, são caracteres com funções especiais que formam uma expressão que é interpretada como regra para "casar" alguma coisa ou, por muitas vezes, partes de textos. Por "casar" devemos entender como um *match* (sim, isso também me lembra o *Tinder*), encaixar, bateu, confere e etc... Pode-se dizer, também, que expressão regular é uma forma de procurar um texto, uma sequência de caracteres, ou trecho em determinadas posições de acordo com um padrão especificado. E por "padrão" devemos entender como aquilo que se quer encontrar com a ajuda da regex.

**Um detalhe:** será adotado a terminologia <code>regex</code> neste e nos próximos posts, caso queira utilizar o termo ER fique à vontade. Eu não utilizo esse termo porque ele me lembra de Entidade e Relacionamento lá de banco de dados.


### Para que serve?

> Para um monte de coisas

Serve para várias tarefas que envolvam busca, extrações, manipulações e validações de padrões em textos. Particularmente, a pessoa que vos escreve utiliza bastante para converter formatos de arquivos e para extrair informações específicas em arquivos de *output*.

Se você quiser uma lista, segue aí:

* Validação de campos de formulários

* Encontrar palavras reservadas

* Filtragem de informações em banco de dados

* Filtro de busca por campos (nome, idade, cpf, rg e etc.)

* Filtro de grep/egrep

* Substituição de caracteres

* Conversão de arquivos

* E etc.

### Exemplos

> O mais esperado

Veremos a seguir alguns exemplos para testarmos no Terminal. Caso você seja teimoso e não queira migrar do Windows para um sistema Unix ou derivado, utilize o [Cygwin](https://cygwin.com/install.html).

No item Expressões Regulares temos duas, vamos testar uma delas. Escreva um conteúdo como esse em um <code>arquivo.txt</code>:

<div class="highlight">
<pre class="kd">
correto<br />
certo<br />
erto<br />
incerto<br />
berto<br />
incorreto<br />
</pre>
</div>

Agora, utilize o *egrep* no arquivo da seguinte forma:

<div class="highlight">
<pre class="kd">
$ egrep '(in)?certo' arquivo.txt
</pre>
</div>

Seu resultado deve ser:

<div class="highlight">
<pre class="kd">
certo<br />
incerto
</pre>
</div>

O padrão especificado foi <code>(in)?certo</code>, que casou as palavras <code>certo</code> e <code>incerto</code> contidas no <code>arquivo.txt</code> e retornou as linhas onde o "casamento" ocorreu.

Outro exemplo, execute:

<div class="highlight">
<pre class="kd">
$ fgrep 'root' /etc/passwd
</pre>
</div>

Será casado e apresentado as linhas que contém o padrão especificado <code>root</code>. Divirta-se dando *match* no arquivo <code>/etc/passwd</code>.

## Conclusão

Neste post demos início a um tema que a primeira vista parece ser complexo, mas que ao decorrer dos estudos iremos simplificar o nosso entendimento. Foi visto um pouco da história das expressões regulares onde podemos observar a nobreza de sua origem, do que se trata e para o que serve. No item de exemplos podemos entender o que seria "casar" e "padrão" de regex. E se você prestou atenção, nos exemplos, embora semelhantes, utilizamos o *egrep* e o *fgrep*. Teremos um post tratando melhor sobre esses utilitários.

### Próximo episódio

No próximo artigo sobre regex iremos começar a tratar sobre os metacaracteres, onde abordaremos a sua divisão em categorias.

## Referências

[1] - [https://blog.staffannoteberg.com/2013/01/30/regular-expressions-a-brief-history/](https://blog.staffannoteberg.com/2013/01/30/regular-expressions-a-brief-history/)

> "You drive us wild" (Rock and Roll All Nite - Kiss)
