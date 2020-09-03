## external sources
source "/usr/share/bash-completion/bash_completion"
source "/usr/share/doc/pkgfile/command-not-found.bash"
source "/usr/share/git/completion/git-completion.bash"
source "/usr/share/git/completion/git-prompt.sh"

## prompts
normal_text="\[$(tput sgr0)\]"
prompt_text="\[$(tput bold ; tput setaf 4)\]"
git_text="\[$(tput bold ; tput setaf 2)\]"

PS1="${prompt_text} \n \u @ \h \w${git_text}\$(__git_ps1 ' (%s)')
${prompt_text} \$ ${normal_text}"
PS2="${prompt_text} > ${normal_text}"

unset normal_text prompt_text git_text

## aliases
alias vi='vim'
alias svim='sudoedit'
alias diff='vimdiff'

alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

alias df='df -h'
alias du='du -c -h'

alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'

alias ls='ls --human-readable --classify --color=auto --group-directories-first'
alias lr='ls --recursive'
alias ll='ls -l --almost-all'
alias lx='ll -X --ignore-backups' # sort by extension
alias lz='ll -S --reverse' # sort by size
alias lt='ll -t --reverse' # sort by time

alias mkdir='mkdir -p -v'
alias cp='cp -i -r'
alias mv='mv -i'
alias rm='rm -I -r'
alias ln='ln -i'

alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'
alias chgrp='chgrp --preserve-root'

alias :q='exit'
alias :x='exit'

alias pacman='sudo pacman --color=auto'
alias pacsyu='sudo pacman --sync --refresh --sysupgrade'
alias pacrns='sudo pacman --remove --nosave --recursive --recursive'
alias pacss='sudo pacman --sync --search'
alias pacqe='sudo pacman --query --explicit'

alias ex='atool -x'
alias calc='qalc'

