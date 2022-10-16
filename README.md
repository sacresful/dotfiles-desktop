# dotfiles
Font: <a href=https://github.com/source-foundry/Hack/releases/download/v3.003/Hack-v3.003-ttf.zip> Hack</a></br>
imageviewer: pqiv</br>
filemanager: vifm</br>
texteditor: vim</br>
terminal: urxvt</br>


remember:</br>
config add (file, after editing)</br>
config commit -a -m "comment"</br>
config push</br>

1. su
   apt install sudo
2. sudo apt install vim
3. add "contrib", "non-free" to /etc/apt/sources.list
   deb http://deb.debian.org/debian/ bullseye main contrib non-free
4. apt update
   apt install nvidia-driver firmware-misc-nonfree
   sudo reboot
5. sudo apt install xserver-xorg-video-nvidia xserver-xorg-core xinit(try this first)
6. sudo apt install lightdm(for now)
   reboot
7. sudo apt install git
8. run install-apps.sh
9. sudo dpkg --add-architecture i386
qtile installation
pip install xcffib 
pip install --no-cache-dir cairocffi
pip install qtile
10. /usr/share/xsessions add .qtile desktop
