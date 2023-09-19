## QTILE CONFIG ##

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"

# Autostart
import os
import subprocess

from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


keys = [
    # Key Binding
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Run Rofi"),
    Key([mod], "b", lazy.spawn("firefox"), desc='Brave Browser'),
    Key([mod], "f", lazy.spawn("thunar"), desc='Thunar'),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Window Focus
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Moving Windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Growing Windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
]

# Groups
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

layout_theme = {"border_width": 3,
                "margin": 5,
                "border_focus": "#a89984",
                "border_normal": "#282828"
                }


# Layouts
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(),
]

# Colors For The Bar
def init_colors():
    return [["#ebdbb2", "#ebdbb2"], # color 0
            ["#282828", "#282828"], # color 1
            ["#cc241d", "#cc241d"], # color 2
            ["#d65d0e", "#d65d0e"], # color 3
            ["#d79921", "#d79921"], # color 4
            ["#98971a", "#98971a"], # color 5
            ["#83a598", "#83a598"], # color 6
            ["#458588", "#458588"], # color 7
            ["#b16286", "#b16286"], # color 8
            ["#a89984", "#a89984"]] # color 9


colors = init_colors()

# Widgets
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Bar
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                        padding = 0,
                        scale = 0.7,
                        foreground = colors[0],
                        background = colors[9],
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[1]
                        ),        
                widget.GroupBox(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        margin_y = 2,
                        margin_x = 3,
                        padding_y = 2,
                        padding_x = 3,
                        borderwidth = 0,
                        disable_drag = True,
                        focused = colors [0],
                        active = colors[4],
                        inactive = colors[9],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[0],
                        foreground = colors[4],
                        background = colors[1]
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[1]
                        ),
                widget.WindowName(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        foreground = colors[1],
                        background = colors[9],
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[1]
                        ),        
                #widget.StatusNotifier(),
                #widget.Systray(),
                #widget.DF(),
                #widget.Memory(),
                #widget.CPU(),
                #widget.Bluetooth(),
                #widget.BatteryIcon(),
                #widget.Battery(),
                widget.Clock(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        foreground = colors[9],
                        background = colors[1],
                        format='%d/%m/%y %H:%M:%S'
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[1]
                        ),
                #widget.QuickExit(),
            ],
            30,
            # background=["#000000", "#000000"],
            margin=[5,5,5,5],
            # opacity=1.0,
            # border_width=[3, 3, 3, 3],
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]
        ),
    ),
]

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

# WM Name
wmname = "LG3D"
