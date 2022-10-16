#!/bin/bash
apt_install () {
	sudo apt-get install neofetch vifm rxvt-unicode pqiv firefox-esr obs-studio zip unzip alsa-utils pulseaudio htop python3-pip libpangocairo-1.0-0 clementine ffmpeg x264 x265
	sudo apt-get update
	sudo dpkg --add-architecture i386
	sudo apt-get update
}
apt_install
