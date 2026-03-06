# =====================================================
# ~/.bashrc - Custom Clean Version
# =====================================================


# 1. Only run for interactive shells
case $- in
    *i*) ;;
      *) return;;
esac


# 2. History Configuration
HISTCONTROL=ignoreboth
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s histappend
shopt -s checkwinsize


# 3. Environment Variables
export ANDROID_HOME="$HOME/Android/Sdk"
export PATH="$PATH:$ANDROID_HOME/cmdline-tools/latest/bin"
export PATH="$PATH:$ANDROID_HOME/platform-tools"
export PATH="$HOME/security-tools/bin:$PATH"


# 4. Prompt Configuration
if [[ "$TERM" == *"-256color" ]] || [[ "$TERM" == "xterm-color" ]]; then
    color_prompt=yes
fi

if [ "$color_prompt" = yes ]; then
    PS1='\[\033[01;34m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='\u@\h:\w\$ '
fi
unset color_prompt

# Set terminal title
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;\u@\h: \w\a\]$PS1"
    ;;
esac


# 5. Aliases
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# LAMP shortcuts
alias startLAMP='sudo systemctl start apache2 && sudo systemctl start mariadb'
alias stopLAMP='sudo systemctl stop apache2 && sudo systemctl stop mariadb'
alias statusLAMP='sudo systemctl status apache2 && sudo systemctl status mariadb'
alias restartLAMP='sudo systemctl restart apache2 && sudo systemctl restart mariadb'


# 6. Bash Completion
if ! shopt -oq posix; then
  [ -f /usr/share/bash-completion/bash_completion ] && \
    . /usr/share/bash-completion/bash_completion
fi


# 7. Terminal UI (Banner + Neofetch)

banner() {
    echo -e "\e[96m$(figlet -f slant "Ubuntu System")\e[0m"
}

terminal_header() {
    banner
    neofetch
}

clear() {
    command clear
    terminal_header
}

# Run when terminal starts
terminal_header


export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
