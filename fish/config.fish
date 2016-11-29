# added by Miniconda3 4.0.5 installer
set -x PATH /home/pol/miniconda3/bin $PATH
set -x LD_LIBRARY_PATH ./ $LD_LIBRARY_PATH
set -x PYTHONPATH . src build $PYTHONPATH
set -x MYPYPATH /home/pol/.config/mypy/
set -x EDITOR nvim
set -x QT_QPA_PLATFORMTHEME
set -x JULIA_LOAD_PATH  ./ $JULIA_LOAD_PATH 
source (conda info --root)/bin/conda.fish

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