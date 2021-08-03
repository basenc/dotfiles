set -a fish_user_paths $DOTFILES/misc/bin $DOTFILES/bin $HOME/.local/bin $HOME/.cargo/bin

export fish_greeting=
export TERM=__[term]__
export EDITOR=__[editor]__

alias "cp"='cp -rv'
alias "mv"='mv -v'
alias "ls"='ls --color=always'
alias "ln"='ln -v'
alias "rm"='rm -rv'
alias "tarpack"="tar -cvf"
alias "tarpeek"="tar -tvf"
alias "untar"="tar -xvf"
alias 'xdg-user-dirs-update'='env LC_ALL=c xdg-user-dirs-update --force'
alias "colortest"="fish -c 'msgcat --color=test'"
alias 'pacman'='yay'

export DOTFILES=/home/$USER/.local/share/dotfiles
