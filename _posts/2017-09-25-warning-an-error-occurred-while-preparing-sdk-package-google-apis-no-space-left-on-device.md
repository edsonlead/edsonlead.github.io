---
layout: post
title: 'Warning: An error occurred while preparing SDK package Google APIs : No space
  left on device'
date: '2017-09-25 08:00:06 -0300'
img: category-android.png
categories: [mobile, android]
tags: [fstab, android, no space left on device]
---
Aqui trataremos de solucionar um "erro" que poder&aacute; ocorrer durante a instala&ccedil;&atilde;o de pacotes necess&aacute;rios para o desenvolvimento m&oacute;vel para Android. Na ocasi&atilde;o, o mesmo acontecia na instala&ccedil;&atilde;o tanto atrav&eacute;s do ./sdkmanager via linha de comando quanto pelo Android Studio.
O problema &eacute; claro:
<blockquote>"No space left on device"</blockquote>

Mas como poderia ser poss&iacute;vel se o disco possu&iacute;a espa&ccedil;o o suficiente?

Pesquisando pela Internet, foi poss&iacute;vel verificar que os downloads realizados dos pacotes no SDK Manager s&atilde;o gravados no diret&oacute;rio /tmp. Ou seja, n&atilde;o havia espa&ccedil;o o suficiente para que o download fosse completado e que fosse poss&iacute;vel dar seguimento &agrave; instala&ccedil;&atilde;o do mesmo.

Como no momento da instala&ccedil;&atilde;o do meu SO eu n&atilde;o reservei uma parti&ccedil;&atilde;o para o /tmp, o mesmo recebia uma aloca&ccedil;&atilde;o autom&aacute;tica de disco com 50% do total de mem&oacute;ria RAM da m&aacute;quina sempre que o systemd inicializava.

Diante disso encontrei duas alternativas:

<ol>
<li>Reparticionar o disco (fora que quest&atilde;o)</li>
<li>Criar um link do /tmp para a home do meu usu&aacute;rio</li>
</ol>

O n&uacute;mero 2 funcionou no in&iacute;cio, mas logo n&atilde;o funcionou como o desejado. Mas, depois de voltar a reler sobre disco r&iacute;gido no <a href="http://www.guiafoca.org/cgs/guia/iniciante/ch-disc.html" target="_blank">Guia Foca GNU/Linux</a>, veio a sacada com o arquivo /etc/fstab.

Para quem n&atilde;o sabe, o arquivo /etc/fstab:

<blockquote>permite que as parti&ccedil;&otilde;es do sistema sejam montadas facilmente especificando somente o dispositivo ou o ponto de montagem<sub>1</sub></blockquote>

Traduzindo:

<blockquote>Basta especificar o diret&oacute;rio /tmp e alocar o espa&ccedil;o de disco necess&aacute;rio &agrave; ele</blockquote>

Com isso, no arquivo /etc/fstab foi inserido a seguinte linha:

{% highlight bash %}
tmpfs /tmp tmpfs defaults,size=8g 0 0
{% endhighlight %}

Basicamente, temos a parti&ccedil;&atilde;o que queremos montar (tmpfs), o ponto de montagem (/tmp), o tipo de sistemas de arquivos (tmpfs), as op&ccedil;&otilde;es (defaults, size=8g) onde inserimos o tamanho da aloca&ccedil;&atilde;o de disco para o diret&oacute;rio /tmp, o dump sem backup (0) e a ordem (0) para que n&atilde;o seja verificado na inicializa&ccedil;&atilde;o do sistema.

O arquivo /etc/fstab ficar&aacute; semelhante a isso:

![Fstab]({{site.baseurl}}/assets/img/post005/post05-fstab.png)

Dessa forma, basta realizar o reboot da m&aacute;quina, prosseguir com a instala&ccedil;&atilde;o dos pacotes para o desenvolvimento m&oacute;vel para Android e ser feliz HA-HA.

## Refer&ecirc;ncia

1.<a href="http://www.guiafoca.org/cgs/guia/iniciante/ch-disc.html" target="_blank"> http://www.guiafoca.org/cgs/guia/iniciante/ch-disc.html</a>
