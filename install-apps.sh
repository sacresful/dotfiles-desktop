#!/bin/bash
apt_install () {
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
	sudo apt-get update 
	sudo apt install libgl1-mesa-dri:i386 libgl1:i386
	sudo apt install nvidia-driver-libs:i386
	sudo apt-get update
	sudo apt install gnupg2 software-properties-common apt-transport-https curl
	curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
	sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
	sudo apt-get update
	sudo apt install code
}
apt_install
