# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger
from pytz import datetime

class ChangeTimezone(widget.Clock):
    defaults = [
        (
            "UTC",
            "datetime.timezone.utc",
            "Timezone to show when mouse is over widget.",
        ),
        (
            "NZT",
            "datetime.timezone.nzt",
            "Timezone to show when clicked two times.",
        ),
        (
            "CDT",
            "datetime.timezone.cdt",
            "Timezone to show when clicked three times.",
        ),
    ]

    # somehow find out how to make it dynamic, and change it through the list

    def __init__(self, **config):
        widget.Clock.__init__(self, **config)
        self.add_defaults(ChangeTimezone.defaults)
        self.eu_timezone = self.timezone

    def mouse_enter(self, *args, **kwargs):
        self.timezone = datetime.timezone.utc 
        self.bar.draw()

    def mouse_leave(self, *args, **kwargs):
        self.timezone = self.eu_timezone
        self.bar.draw()

mod = "mod4"
terminal = guess_terminal()
myTerminal = guess_terminal()
myBrowser = "firefox-esr"
myTextEditor = myTerminal + "vi"
myFileManager = myTerminal + "vifm"
myRecorder = "obs"
myImageViewer = "pqiv"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "e", lazy.spawn(myTerminal + ' -e vifm'), desc="Open file explorer"),
    Key([mod], "s", lazy.spawn(myTerminal + ' -e scrot -u'), desc="Screenshot"),
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'),
]
#groups = [Group("1", matches=[Match(wm_class=["firefox"])]),
#          Group("2"),
#          Group("3"),
#          Group("4"),
#          Group("5"),
#          Group("6"),
#          Group("7"),
#          Group("8"),
#          Group("9")]
groups = [Group(i) for i in "123456789"]


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus=["#dfad27"], border_width=1),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Hack",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/.config/qtile/background.png",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    rounded=False,
                    highlight_method="block",
                    borderwidth=5,
                    disable_drag=True,
                    highlight_color="#dfad27",
                    inactive="#808080",
                    hide_unused=False,
                    other_current_screen_border="000000",
                    other_screen_border="000000",
                    this_current_screen_border="#dfad27",
                    this_screen_border="#dfad27"
                    ),
                widget.Prompt(),
                widget.WindowName(
                    background="dfad27",
                    ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.StatusNotifier(),
                widget.Systray(),
                    widget.TextBox(
                        text="|"
                    ),
                widget.Net(
                    format="{up} {down}",
                    mouse_callbacks={"Button1": lazy.spawn(myTerminal + " -e nmtui")},
                    update_interval=4,
                    ),
                    widget.TextBox(
                        text="|"
                    ),
                widget.CPU(
                    format="{load_percent}%",
                    mouse_callbacks={"Button1": lazy.spawn(myTerminal + " -e htop")}
                    ),
                    widget.TextBox(
                        text="|"
                    ),
                widget.Memory(
                    format="{MemPercent:.0f}%",
                    mouse_callbacks={"Button1": lazy.spawn(myTerminal + " -e htop")}
                    ),
                    widget.TextBox(
                            text="|"
                        ),
                widget.DF(
                    visible_on_warn=False,
                    format="({uf}{m}|{r:.0f}%)",
                        ),
                    widget.TextBox(
                            text="|"
                        ),
                ChangeTimezone(
                    format="%I:%M %p %a, %d/%m/%Y",
                    timezone="Europe/Warsaw",
                    mouse_callbacks={"Button1": lazy.spawn(myTerminal + ' --hold -e cal -y')},
                    ),
                    widget.TextBox(
                            text="|"
                    ),
                widget.Volume(
                    mouse_callbacks={"Button1": lazy.spawn(myTerminal + ' -e alsamixer')}
                    ),
                    widget.TextBox(
                            text="|"
                    ),
                widget.CheckUpdates(
                    distro="Debian",
                    display_format="Updates: {updates}",
                    ),
                    widget.TextBox(
                            text="|"
                    ),                   
                widget.CurrentLayoutIcon(
                    scale=0.75   
                    ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        wallpaper="~/.config/qtile/background2.png",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Clock(
                    format="%I:%M %p",
                    ),
                widget.TextBox(
                    text="remapper",
                    mouse_callbacks={"Button1": lazy.spawn(myTerminal + ' -e sudo input-remapper-gtk')},
                    ),
            ],
            24,
        ),
    ),

]

logger.debug("Callback function triggered")

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Steam"), # Steam
        Match(title="Origin"), # Origin
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
