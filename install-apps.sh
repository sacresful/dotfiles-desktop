#!/bin/bash
apt_install () {
	sudo apt-get install \
		neofetch \
		vifm \
		rxvt-unicode \
		sxiv \
		firefox-esr \
		obs-studio \
		zip \
		unzip \
		alsa-utils \
		pulseaudio \
		mpv \
		htop \
		python3-pip \
		libpangocairo-1.0-0 \
		ffmpeg x264 x265 
		fonts-noto \
		xinput \
		cmus \
		ncal \
		network-manager \
		steam \
	sudo apt-get update 
	sudo dpkg --add-architecture i386
	sudo apt-get update
	sudo apt install libgl1-mesa-dri:i386 libgl1:i386
	sudo apt-get upgrade steam -f
	sudo apt install nvidia-driver-libs:i386
	sudo apt-get update
}
apt_install
