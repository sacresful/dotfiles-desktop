exec dbus-launch
exec dbus-run-session
exec dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
dbus-update-activation-environment --all
gnome-keyring-daemon --start --components=secrets
xrdb -merge ~/.Xresources
xbindkeys &
setxkbmap pl
exec qtile start
