source $HOME/.bashrc

export HISTCONTROL="erasedups"
export HISTSIZE="100000"

export TERMINAL="alacritty"
export PAGER="less"
export EDITOR="nvim"
export VISUAL="nvim"
export BROWSER="firefox-developer-edition"

export NPM_CONFIG_PREFIX="${HOME}/.node_modules"

export SDK_HOME="${HOME}/Code"
export ANDROID_SDK_ROOT="${SDK_HOME}/android"
export ANDROID_HOME="${ANDROID_SDK_ROOT}"

export PATH="${PATH}:${HOME}/.local/bin"
export PATH="${PATH}:${NPM_CONFIG_PREFIX}/bin"
export PATH="${PATH}:${ANDROID_SDK_ROOT}/tools"
export PATH="${PATH}:${ANDROID_SDK_ROOT}/tools/bin"
export PATH="${PATH}:${ANDROID_SDK_ROOT}/platform-tools"

if systemctl -q is-active graphical.target && [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
  exec startx
fi
