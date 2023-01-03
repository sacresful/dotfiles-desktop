dbus-update-activation-environment --all & DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY
gnome-keyring-daemon --start --components=secrets
xrdb -merge ~/.Xresources
xbindkeys &
setxkbmap pl
exec qtile start
dunst -print
