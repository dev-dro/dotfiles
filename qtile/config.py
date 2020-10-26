from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Screen, ScratchPad, DropDown, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder

mod = "mod4"
alt = "mod1"

extension_defaults = dict(
    background = "#3B4252",
    foreground = "#D8DEE9",
    selected_background = "#434C5E",
    selected_foreground = "#E5E9F0",
    dmenu_height = 24,
    fontsize = 9
)

keys = [
    # Switch focus
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.next()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),

    # Swap windows 
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "semicolon", lazy.layout.flip()),

    # Change windows sizes
    Key([mod], "equal", lazy.layout.grow()),
    Key([mod], "minus", lazy.layout.shrink()),
    Key([mod, "shift"], "equal", lazy.layout.normalize()),
    Key([mod, "shift"], "minus", lazy.layout.maximize()),

    Key([mod], "bracketleft", lazy.prev_screen()),
    Key([mod], "bracketright", lazy.next_screen()),

    # Toggle between different layouts as defined below
    Key([mod], "t", lazy.group.setlayout('monadtall')),
    Key([mod], "y", lazy.group.setlayout('monadwide')),
    Key([mod], "m", lazy.group.setlayout('max')),
    Key([mod], "s", lazy.window.toggle_floating(), desc = "Toggle floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc = "Toggle fullscreen"),
    Key([mod], "w", lazy.window.kill(), desc = "Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc = "Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc = "Shutdown qtile"),

    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5")),
    Key(["shift"], "XF86MonBrightnessUp", lazy.spawn("light -A 20")),
    Key(["shift"], "XF86MonBrightnessDown", lazy.spawn("light -U 20")),
    Key(["control"], "XF86MonBrightnessUp", lazy.spawn("light -S 75")),
    Key(["control"], "XF86MonBrightnessDown", lazy.spawn("light -S 25")),

    # volume
    Key([], "XF86AudioMute", lazy.spawn("mute-toggle")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("change-volume +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("change-volume -5%")),

    # media
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),

    # screeshots
    Key([], "Print", lazy.spawn('screenshot')),

    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "r", lazy.spawn("alacritty -e ranger")),
    Key([mod], "v", lazy.spawn("alacritty -e nvim")),
    Key([mod], "space", lazy.spawn("rofi -show drun")),
    Key([mod], "c", lazy.spawn("clipmenu")),
    Key([mod], "p", lazy.spawn("bwmenu")),
    Key([mod], "q", lazy.run_extension(extension.CommandSet(commands = {
        'lock': 'slock',
        'suspend': 'systemctl suspend',
        'logout': 'qtile-cmd -o cmd -f shutdown',
        'restart': 'systemctl reboot',
        'poweroff': 'systemctl poweroff -i',
    }))),
]

groups = [
    Group(" MAIN "),
    Group(" CODE ", matches=[Match(wm_class=["jetbrains-idea"])]),
    Group(" TOOL "),
    Group(" PLAY ", matches=[Match(wm_class=["spotify", "pocket-casts-linux"])]),
    Group(" GAME ", matches=[Match(wm_class=["Steam", "FantasyGrounds.x86_64"])]),
    Group(" VIRT "),
    Group(" FILE "),
    Group(" CONF "),
    Group(" CHAT "),
    Group(" WORK "),
]

dgroups_key_binder = simple_key_binder("mod4")
dgroups_app_rules = []

layout_defaults = dict(
        border_focus = "#434c5e",
        border_normal = "#2E3440",
        border_width = 1,
        margin = 5,
)

layouts = [
    layout.MonadTall(align = layout.MonadTall._left, **layout_defaults),
    layout.MonadWide(align = layout.MonadTall._left, **layout_defaults),
    layout.Max(**layout_defaults),
]

floating_layout = layout.Floating(**layout_defaults, float_rules = [
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])

widget_defaults = dict(
    font = 'DejaVuSansMono Nerd Font',
    fontsize = 12,
    background = "#3B4252",
    foreground = "#D8DEE9",
    padding = 5,
)

sep_defaults = dict(
    linewidth = 0,
    padding = 15,
)

extension_defaults = widget_defaults.copy()

bar_defaults = dict(
    background = "#3B4252",
)

bar_groups = [
    widget.Sep(**sep_defaults),
    widget.Image(**widget_defaults, filename = "~/.config/qtile/icon.png",
                 mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn("rofi -show drun")}),

    widget.Sep(**sep_defaults),
    widget.GroupBox(**widget_defaults, highlight_method = "block", borderwidth = 0, rounded = False, spacing = 0,
                    active = "#D8DEE9", inactive = "#D8DEE9", urgent_border = "#BF616A", urgent_text = "#D8DEE9",
                    this_current_screen_border = "#4C566A", this_screen_border = "#4C566A",
                    other_current_screen_border = "#4C566A", other_screen_boder = "#4C566A"),

    widget.Sep(**sep_defaults),
    widget.TextBox("", **widget_defaults),
    widget.WindowName(width = bar.STRETCH, **widget_defaults, for_current_screen = True),
]

bar_notification = [
    widget.Sep(**sep_defaults),
    widget.TextBox("墳", **widget_defaults),
    widget.Volume(**widget_defaults),

    widget.Sep(**sep_defaults),
    widget.TextBox("﬉", **widget_defaults),
    widget.Wlan(**widget_defaults, format = "{essid} - {percent:2.0%}", interface = "wlp3s0"),

    widget.Sep(**sep_defaults),
    widget.TextBox("襤", **widget_defaults),
    widget.Battery(**widget_defaults, format = "{percent:2.0%} - {hour:d}:{min:02d}",
                   update_interval = 15, notify_below = 0.1),
    widget.Sep(**sep_defaults),
    widget.TextBox("", **widget_defaults),
    widget.Clock(**widget_defaults, format = '%a %d %b %Y %H:%M:%S'),

    widget.Sep(**sep_defaults),
]

main_screen = Screen(top = bar.Bar(
    [*bar_groups, *bar_notification], 24, **bar_defaults
))

hdmi_screen = Screen(top = bar.Bar(
    [*bar_groups, *bar_notification], 24, **bar_defaults
))

if (True):
    screens = [main_screen, hdmi_screen]
else:
    screens = [main_screen]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start = lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start = lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

# for java apps to function
wmname = "LG3D"

import os, subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

@hook.subscribe.screen_change
def restart_on_randr(event):
    qtile.cmd_restart()

@hook.subscribe.client_new
def floating_size_hints(window):
    hints = window.window.get_wm_normal_hints()
    if hints and 0 < hints['max_width'] < 960:
        window.floating = True
