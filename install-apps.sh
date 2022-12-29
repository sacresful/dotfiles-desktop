#!/bin/bash
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install \
#basic
	neofetch \
	zip \
	unzip \
	vifm \
	rxvt-unicode \
	sxiv \
	firefox-esr \
	alsa-utils \
	pulseaudio \
	htop \
	fonts-noto \
	xinput \
	network-manager \
	net-tools \
	ufw \
	rofi \
	wget \
#utility
	obs-studio \
	mpv \
	python3-pip \
	libpangocairo-1.0-0 \
	ffmpeg \
	x264 \
	x265 \
	cmus \
	ncal \
	steam \
	gnome-keyring \
	pass \
sudo apt-get update 
sudo apt install libgl1-mesa-dri:i386 libgl1:i386
sudo apt install nvidia-driver-libs:i386
sudo apt-get update
wget https://az764295.vo.msecnd.net/stable/e8a3071ea4344d9d48ef8a4df2c097372b0c5161/code_1.74.2-1671533413_amd64.deb
sudo apt install ./code_1.74.2-1671533413_amd64.deb
