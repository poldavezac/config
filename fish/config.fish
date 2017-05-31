# added by Miniconda3 4.0.5 installer
set -x PATH $HOME/.local/bin $HOME/miniconda3/bin $PATH
set -x LD_LIBRARY_PATH ./ $LD_LIBRARY_PATH
set -x PYTHONPATH "./:../:./src/:./build/"
set -x MYPYPATH ./linting/:../linting/
set -x EDITOR nvim
set -x QT_QPA_PLATFORMTHEME
set -x JULIA_LOAD_PATH  ./ $JULIA_LOAD_PATH 
source $HOME/.config/fish/conda.fish

set normal (set_color normal)
set magenta (set_color magenta)
set yellow (set_color yellow)
set green (set_color green)
set red (set_color red)
set gray (set_color -o black)

# Fish git prompt
set __fish_git_prompt_showdirtystate 'yes'
set __fish_git_prompt_showstashstate 'yes'
set __fish_git_prompt_showuntrackedfiles 'yes'
set __fish_git_prompt_showupstream 'yes'
set __fish_git_prompt_color_branch yellow
set __fish_git_prompt_color_upstream_ahead green
set __fish_git_prompt_color_upstream_behind red

# Status Chars
set __fish_git_prompt_char_dirtystate '⚡ '
set __fish_git_prompt_char_stagedstate '→ '
set __fish_git_prompt_char_untrackedfiles '☡ '
set __fish_git_prompt_char_stashstate '↩ '
set __fish_git_prompt_char_upstream_ahead '+'
set __fish_git_prompt_char_upstream_behind '-'

alias win10 "rdesktop -u DEVS -g 95% -PKD 192.168.1.53"
alias win07 "rdesktop -u devtest -g 95% -PKD 192.168.1.66"
