dunst -print
exec dbus-update-activation-environment --runit DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
dbus-update-activation-environment --all
gnome-keyring-daemon --start --components=secrets
xrdb -merge ~/.Xresources
xbindkeys &
setxkbmap pl
exec qtile start
