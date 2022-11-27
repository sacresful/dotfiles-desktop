# dotfiles
Font: <a href=https://github.com/source-foundry/Hack/releases/download/v3.003/Hack-v3.003-ttf.zip> Hack</a></br>
imageviewer: pqiv</br>
filemanager: vifm</br>
texteditor: vim</br>
terminal: urxvt</br>


remember:</br>
config commit -a -m "comment"</br>
config push</br>

1. su</br>
   apt install sudo</br>
2. sudo apt install vim</br>
3. add "contrib", "non-free" to /etc/apt/sources.list</br>
   deb http://deb.debian.org/debian/ bullseye main contrib non-free</br>
4. apt update</br>
   apt install nvidia-driver firmware-misc-nonfree</br>
   sudo reboot</br>
5. sudo apt install xserver-xorg-video-nvidia xserver-xorg-core xinit(try this first)</br>
7. sudo apt install git</br>
8. run install-apps.sh</br>
9. qtile installation</br>
   pip install xcffib </br>
   pip install --no-cache-dir cairocffi</br>
   pip install qtile</br>
   pip install pytz</br>

useful sites:</br>
ps1generator(bashrc)</br>

try(maybe):</br>
pqiv -> sxiv</br>
maybe vlc -> mpv</br>

/etc/X11/xorg.conf.d/50-mouse-acceleration.conf</br>
Section "InputClass"</br>
	Identifier "My Mouse"</br>
	Driver "libinput"</br>
	MatchIsPointer "yes"</br>
	Option "AccelProfile" "flat"</br>
	Option "AccelSpeed" "0"</br>
EndSection</br>

