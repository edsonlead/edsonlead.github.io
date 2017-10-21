---
layout: post
title: 'Fedora 26: atualizando o F25...'
date: '2017-07-14 11:22:43 -0300'
img: category-fedora.png
categories: [fedora]
tags: [fedora, upgrading, mate]
---
No dia 11 de julho, ter&ccedil;a-feira, o <a href="https://fedoramagazine.org/fedora-26-is-here/" target="_blank">Fedora 26 foi lan&ccedil;ado </a>. V&aacute;rias novidades vieram nessa nova vers&atilde;o, uma delas foi o lan&ccedil;amento do <a href="https://labs.fedoraproject.org/python-classroom/" target="_blank">Python Classroom Labs</a>. E como um bom usu&aacute;rio do fedora, resolvi atualizar o Fedora 25 do meu notebook.

Sim! Atualizar a vers&atilde;o 25 para a 26 do Fedora sem que haja a necessidade de fazer download de .iso. Caso voc&ecirc; queira instalar o Fedora 26 do zero pode <a href="https://getfedora.org/pt/" target="_blank" rel="noopener noreferrer">realizar o download aqui</a>. Nesse caso, eu prefiro o <a href="https://torrent.fedoraproject.org/torrents/" target="_blank" rel="noopener noreferrer">download por torrent</a> devido a minha conex&atilde;o.

## Atualizando o sistema...

Para atualizar o Fedora 25 segui, basicamente, os mesmos passos que utilizei para o Fedora 24 no ano passado. Voc&ecirc; pode verificar o passo a passo no artigo do <a href="https://fedoramagazine.org/upgrading-fedora-25-fedora-26/" target="_blank" rel="noopener noreferrer">Fedora Magazine: Upgrading Fedora 25 to Fedora 26</a>. Os passos/comandos que utilizei s&atilde;o os mesmos que est&atilde;o presentes nesse artigo.

<strong>Atualizar para a &uacute;ltima vers&atilde;o do Fedora 25:</strong>

{% highlight bash %}
$ sudo dnf upgrade --refresh
{% endhighlight %}

Instalar o plugin DNF:

{% highlight bash %}
$ sudo dnf install dnf-plugin-system-upgrade
{% endhighlight %}

Iniciar a atualiza&ccedil;&atilde;o:

{% highlight bash %}
$ sudo dnf system-upgrade download --releasever=26 --allowerasing
{% endhighlight %}

Reboot e atualiza&ccedil;&atilde;o:

{% highlight bash %}
$ sudo dnf system-upgrade reboot
{% endhighlight %}

Particularmente, eu obtive um erro de conflito de arquivos (Error: Transaction check error:) o qual solucionei ap&oacute;s verificar do que se tratava o arquivo conflitante e o removi.

## P&oacute;s-atualiza&ccedil;&atilde;o...

Como a atualiza&ccedil;&atilde;o do Fedora n&atilde;o interfere nas configura&ccedil;&otilde;es dos programas que utilizo, n&atilde;o tive a necessidade de instalar e configurar pacotes que eu j&aacute; utilizava na vers&atilde;o anterior.

A tela de login ap&oacute;s a instala&ccedil;&atilde;o ficou bem legal com esse wallpaper padr&atilde;o do Fedora 26:

![Fedora 26]({{site.baseurl}}/assets/img/post004/post04-f26.jpg)

Mas o que mais chamou a minha aten&ccedil;&atilde;o foram o &iacute;cones Breeze:

![Breeze]({{site.baseurl}}/assets/img/post004/post04-breeze.png)

E essa &eacute; a minha &aacute;rea de trabalho. Utilizo o Mate como interface desktop:

![Desktop F26]({{site.baseurl}}/assets/img/post004/post04-desktop.png)

Caso voc&ecirc; deseja verificar as notas de lan&ccedil;amento do Fedora 26, elas est&atilde;o dispon&iacute;veis no <a href="https://docs.fedoraproject.org/en-US/Fedora/26/html/Release_Notes/index.html" target="_blank" rel="noopener noreferrer">Fedora Project</a>.

E voc&ecirc;, j&aacute; est&aacute; utilizando a nova vers&atilde;o do Fedora?
