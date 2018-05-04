---
layout: post
title: Preparando Meu Laboratório Virtual
date: '2018-05-01 00:00:00 -0300'
img: category-root.png
categories: [root]
tags: [virtualização, fedora, centos, virtualbox]

---

## Laboratório virtual?

Laboratório virtual é uma estratégia bastante utilizada para o ensino-aprendizagem de administração de redes, sistemas, pentests, análise de malware, etc. Basicamente, utiliza-se o conceito de virtualização. A virtualização é bastante utilizada em empresas para a gerência de recursos computacionais com maior eficiência.

Eis algumas tecnologias que são utilizadas para a criação de máquinas virtuais:

* <a href="https://www.virtualbox.org/" target="_blank">VirtualBox</a>

* <a href="https://www.vmware.com/br.html" target="_blank">VMware</a>

* <a href="https://www.linux-kvm.org/page/Main_Page" target="_blank">KVM</a>

* <a href="https://www.xenproject.org/" target="_blank">Xen</a>


## Instalando uma tecnologia de virtualização

Dentre as tecnologias citadas, o VirtualBox foi escolhido.

Um passo-a-passo para a sua instalação na distribuição Fedora pode ser encontrado <a href="https://www.itzgeek.com/how-tos/virtualization/install-virtualbox-4-3-on-fedora-22.html" target="_blank">neste link</a>.

<code>
$ sudo dnf install kernel-devel kernel-headers dkms
</code>

<code>
$ wget https://www.virtualbox.org/download/oracle_vbox.asc
</code>

<code>
$ sudo rpm --import oracle_vbox.asc
</code>

<code>
$ wget http://download.virtualbox.org/virtualbox/rpm/fedora/virtualbox.repo
-O /etc/yum.repos.d/virtualbox.repo
</code>

<code>
$ sudo dnf install VirtualBox-5.2
</code>

<code>
$ sudo service vboxdrv start
</code>

<code>
$ sudo usermod -a -G vboxusers nome_do_usuario
</code>

Um erro foi retornado ao executar o comando da linha 6:

```
Job for vboxdrv.service failed because the control process exited with error code.
See "systemctl status vboxdrv.service" and "journalctl -xe" for details.
```

E o seguinte erro era apresentado ao iniciar o VirtualBox pelo terminal:

```
WARNING: The vboxdrv kernel module is not loaded. Either there is no module
available for the current kernel (4.15.17-200.fc26.x86_64) or it failed to
load. Please recompile the kernel module and install it by

sudo /sbin/vboxconfig

You will not be able to start VMs until this problem is fixed.
```
Bastou reiniciar a máquina e executar o comando <code>sudo /sbin/vboxconfig</code>.

## As máquinas virtuais

Criar uma máquina virtual é bem simples e intuitivo no VirtualBox.
O mesmo acontece na instalação de sistemas operacionais.

Para esse momento, foi escolhido ter duas máquinas virtuais onde cada uma possui uma distribuição diferente. O objetivo é possuir uma máquina cliente e outra máquina servidora.

## As distribuições linux escolhidas

Duas distribuições Linux foram escolhidas: <a href="https://torrent.fedoraproject.org/torrents/Fedora-Xfce-Live-x86_64-28.torrent" target="_blank">Fedora Xfce 28</a> (máquina cliente) e <a href="http://mirror.ufscar.br/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1708.torrent" target="_blank">CentOS 7 Minimal</a> (máquina servidora).

A interface Xfce foi escolhida levando em consideração que se trata de um ambiente de desktop "leve". E com certeza irá evitar possíveis travamentos e lentidão na máquina principal comparado com a utilização do Gnome ou KDE. A escolha do CentOS Minimal é justamente para ampliar os estudos fazendo configurações do zero. A intenção é utilizar ao máximo o modo texto nessas duas distribuições Linux.

Outras distros como Debian ou SUSE podem ser adicionadas, mas por enquanto, apenas as duas escolhidas :D
