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

## asdf-vm
. $HOME/.asdf/asdf.sh
. $HOME/.asdf/completions/asdf.bash

## aliases
alias vim='nvim'
alias vi='nvim'
alias svim='sudoedit'
alias diff='vimdiff'

alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

alias df='df -h'
alias du='du -c -h'

alias ping='ping -c 3'

alias ls='ls --human-readable --classify --color=auto --group-directories-first'
alias lr='ls --recursive'
alias ll='ls -l'
alias la='ll --almost-all'
alias lx='ll -X --ignore-backups' # sort by extension
alias lz='ll -S --reverse' # sort by size
alias lt='ll -t --reverse' # sort by time

alias mkdir='mkdir -p -v'
alias cp='cp -i -r'
alias mv='mv -i'
alias rm='rm --preserve-root --interactive=once -r'
alias ln='ln -i'

alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'
alias chgrp='chgrp --preserve-root'

alias :q='exit'
alias :x='exit'

alias pacman='pacman --color=auto'

# tabtab source for jhipster package
# uninstall by removing these lines or running `tabtab uninstall jhipster`
[ -f /home/dev-dro/Code/invoice-ti/finpesweb-desenvolvimento/node_modules/tabtab/.completions/jhipster.bash ] && . /home/dev-dro/Code/invoice-ti/finpesweb-desenvolvimento/node_modules/tabtab/.completions/jhipster.bash
