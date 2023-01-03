#!/bin/bash
install="sudo apt install"
sudo dpkg --add-architecture i386
sudo apt install libc6-i386
sudo apt-get update
#basic
$install neofetch 
$install zip 
$install unzip 
$install vifm 
$install rxvt-unicode 
$install sxiv 
$install firefox-esr 
$install alsa-utils 
$install pulseaudio 
$install htop 
$install fonts-noto 
$install xinput 
$install network-manager 
$install net-tools 
$install ufw 
$install rofi 
$install wget 
#utility
$install obs-studio 
$install mpv 
$install python3-pip 
$install libpangocairo-1.0-0 
$install ffmpeg 
$install x264
$install x265 
$install cmus 
$install ncal 
$install steam 
$install gnome-keyring 
$install pass 
$install texlive-full
$install ntfs-3g
$install dunst
$install libnotify-bin
$install apt-transport-https
$install seahorse
sudo apt-get update 
sudo apt install libgl1-mesa-dri:i386 libgl1:i386
sudo apt install nvidia-driver-libs:i386
sudo apt-get update
wget https://az764295.vo.msecnd.net/stable/e8a3071ea4344d9d48ef8a4df2c097372b0c5161/code_1.74.2-1671533413_amd64.deb
sudo apt install ./code_1.74.2-1671533413_amd64.deb
sudo mv 50-mouseacceleration.conf /etc/X11/xorg.conf.d
