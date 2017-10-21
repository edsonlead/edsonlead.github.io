---
layout: post
title: "Como instalar o turtle no Fedora 25"
date: '2017-07-07 19:35:22 -0300'
description:
img: category-fedora.png
categories: [python]
tags: [turtle, fedora]
---
O turtle é um módulo Python que possui funcionalidades que auxiliam na realização de desenhos com comandos bem simples. Teremos um post mais detalhado sobre esse assunto, este tratará somente da instalação do turtle no Fedora 25.

Para utilizar o módulo turtle é necessário que o pacote Tkinter esteja instalado. Então, seguimos no terminal com o comando:

{% highlight terminal %}
$ dnf search python3-tk
{% endhighlight %}

O comando acima serve para pesquisar pacotes. Após isso, instale de acordo com a sua arquiteura:

{% highlight terminal %}
$ sudo dnf install python3-tkinter.x86_64
{% endhighlight %}

Pronto! Vamos testar?

Acesse o Python interativo e utilize os comandos como apresentados abaixo:

{% highlight python %}
$ python3.5
Python 3.5.3 (default, May 10 2017, 15:05:55)
[GCC 6.3.1 20161221 (Red Hat 6.3.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import turtle
>>> bob = turtle.Turtle()
>>> for i in range(8):
...     bob.fd(100)
...     bob.lt(45)
...
>>>
{% endhighlight %}

O resultado será algo como:

![Resultado]({{site.baseurl}}/assets/img/post003/post03-turtle.png)

Muito bem! O módulo turtle já está funcionando. :)
