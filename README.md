# pyCheckMyFleet-pi

Configuração e Instalação

Sistema Operacional: 
Raspbian
----------------------------------------------------
Pré-requisitos:
Módulo bluetooth instalado
Módulo wi-fi instalado
----------------------------------------------------
Instalação do sistema:

Antes de começar a instalação execute os seguintes comandos:

$  sudo apt-get update
$  sudo apt-get upgrade
$  sudo apt-get autoremove
$  sudo reboot

Instale os componentes necessários utilizando os comandos:

$  sudo apt-get install python-serial
$  sudo apt-get install bluetooth bluez-utils blueman
$  sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n libwxgtk2.8-dev
$  sudo apt-get install git-core
$  sudo reboot 

Em seguida, clone o repositório na pasta raíz do seu Raspbian:

$  cd ~
$  git clone https://github.com/gabriel-augusto/pyCheckMyFleet-pi
----------------------------------------------------
Instalação dos módulos python:

$ sudo apt-get install python-pip
$ sudo apt-get install libbluetooth-dev
$ sudo pip install pybluez
$ sudo apt-get install python-mysqldb
$ sudo apt-get install build-essential python-dev libmysqlclient-dev
$ sudo pip install MySQL-python
----------------------------------------------------
Permitir saída de vídeo auxiliar no RPi:

Conecte seu teclado e sua TV no RPi.
Insira seu cartão SD.
Ligue a TV.
Ligue o RPi e pressione a tecla SHIFT até que o LED verde pare de Power up the Pi and hold down the SHIFT key, until the green LED pare de piscar. Isto irá forçar o RPi a entrar no modo de recuperação.
Se a tela continuar vazia, tente pressionar as teclas 1, 2, 3, 4, uma após a outra (uma dessas teclas irá direcionar a saída de vídeo para a saída auxiliar).
Edite o arquivo de configuração (há um link no menu do Noobs) para selecionar o tipo da sua TV. Procure por esta linha:
#sdtv_mode=0
Remova o símbolo # e altere o numero ao final para um dos seguintes baseado no tipo da sua TV:
sdtv_mode=0 # Normal NTSC
sdtv_mode=1 # Japanese version of NTSC – no pedestal
sdtv_mode=2 # Normal PAL
sdtv_mode=3 # Brazilian version of PAL – 525/60 rather than 625/50, different subcarrier
Adicione a seguinte linha ao arquivo:
hdmi_ignore_hotplug=1
Tenha certeza de que a seguinte linha:
hdmi_force_hotplug=1
está comentada (tem o símbolo # no início da linha).
Precione a tecla TAB.
Clique em OK
Pressione a tecla ESC e aguarde o RPi reiniciar.
----------------------------------------------------
Login automático:

Abra o terminal e edite o arquivo inittab:
$ sudo nano /etc/inittab

Navegue até a seguinte linha no arquivo inittab:
1:2345:respawn:/sbin/getty 115200 tty1

Adicione # no início da linha para comenta-la:
#1:2345:respawn:/sbin/getty 115200 tty1

Adicione a seguinte linha logo abaixo a linha comentada:
1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1

Isto irá executar o login com o usuário pi e sem nenhuma autenticação.
Pressione Ctrl+X para sair do editor nano seguido de Y para salvar o arquivo e então pressione Enter para confirmar o nome do arquivo.
----------------------------------------------------
conectar ao OBDII automaticamente:

Primeiramente, com o OBD ligado perto do seu Raspbarry-pi, descubra o endereço MAC do seu OBD com o comando:

$  hcitool scan

Para adicionar o OBDII à lista de dispositivos bluetooth do seu raspbarry, com o bluetooth ligado, o OBD conectado ao carro ligado e com os dois dispositovos próximo, abra o terminal e insira o seguinte comando:

$ sudo bluez-simple-agent hci0 00:0D:18:A0:4E:35

Em seguida, quando solicitado o PIN digite:
1234

Agora com o OBD adicionado a lista de dispositivos bluetooth, edite o arquivo rfcomm.conf:

$ sudo nano /etc/bluetooth/rfcomm.conf

E adicione o seguinte código ao final do arquivo:

rfcomm1 {
    bind yes;
    device 00:0D:18:A0:4E:35;
    channel 1;
    comment "Connection to Bluetooth serial module";
}

Este código ira permitir que ao utilizar o comando “sudo rfcomm bind all” o raspbarry se conecte automaticamente ao OBDII. Posteriormente iremos mostrar como colocar esse código para ser executado na inicialização do sistema.

----------------------------------------------------
Execução automática:

Para executar o sistema automaticamente após a inicialização do SO execute:

$ sudo nano /etc/profile

Então, ao final deste arquivo, insira o seguinte código:
cd pyobd-pi/
python run.py

Ao final digite “ctrl+X” para sair, pressione “Y” para salvar e por fim “Enter” para confirmar o nome do arquivo.
-----------------------------------------------------
