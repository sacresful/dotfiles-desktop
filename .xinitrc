exec dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
xrdb -merge ~/.Xresources
xbindkeys &
setxkbmap pl
exec qtile start
