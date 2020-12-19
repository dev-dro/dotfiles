source $HOME/.bashrc

export GTK_IM_MODULE="ibus"
export XMODIFIERS=@im="ibus"
export QT_IM_MODULE="ibus"

export HISTCONTROL="erasedups"
export HISTSIZE="100000"

export TERMINAL="alacritty"
export PAGER="less"
export EDITOR="nvim"
export VISUAL="nvim"
export BROWSER="firefox-developer-edition"

export CM_LAUNCHER="rofi"

export QT_STYLE_OVERRIDE="kvantum-dark"

export SCRIPTS_HOME="${HOME}/.scripts"
export THEMES_HOME="${HOME}/.themes"
export SDK_HOME="${HOME}/Development/sdk"

export NPM_CONFIG_PREFIX="${HOME}/.node_modules"

export ANDROID_SDK_ROOT="${SDK_HOME}/android"
export ANDROID_HOME="${ANDROID_SDK_ROOT}"

export PATH="${PATH}:${HOME}/.local/bin"
export PATH="${PATH}:${NPM_CONFIG_PREFIX}/bin"
export PATH="${PATH}:${ANDROID_SDK_ROOT}/tools"
export PATH="${PATH}:${ANDROID_SDK_ROOT}/tools/bin"
export PATH="${PATH}:${ANDROID_SDK_ROOT}/platform-tools"

if type rg &> /dev/null; then
  export FZF_DEFAULT_COMMAND="rg --files"
  export FZF_DEFAULT_OPTS="-m --height 50% --border"
fi

if systemctl -q is-active graphical.target && [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
  exec startx
fi
