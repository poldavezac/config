if &shell =~# 'fish$'
    set shell=bash
endif
filetype off
set rtp+=~/.config/nvim/bundle/Vundle.vim
call vundle#rc("~/.config/nvim/bundle")
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'JuliaLang/julia-vim'
Plugin 'fugitive.vim'
Plugin 'Gundo'
"Plugin 'pyclewn'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'benekastah/neomake'
Plugin 'zyedidia/julialint.vim'
Plugin 'https://github.com/junegunn/vim-easy-align.git'
Plugin 'https://github.com/critiqjo/lldb.nvim.git'
Plugin 'https://github.com/dag/vim-fish.git'
call vundle#end()
filetype plugin indent on

set ruler
syntax enable
set hlsearch
set tabstop=4
set shiftwidth=4
set expandtab
set ignorecase
set smartcase
set notr
set wildmenu
set nobackup
set history=999
set number
set foldmethod=indent
set foldenable
set undodir=~/.config/nvim/undos,.,/tmp
set undofile

nmap <C-Space>  i<Space><Esc>
nmap <C-x><C-s> :w<Enter>
nmap <C-BS> db
imap <C-x><C-s> <Esc>:w<Enter>i
imap <C-BS> <Esc>dbi
imap <BS> <Esc>s
nnoremap <F5> :GundoToggle<CR>
nnoremap <S-Q>  <S-A>
nmap <silent> <F9> :execute "cd ".expand("%:h")<Enter>
nmap <Tab>  >>
nmap <S-Tab>  <<
tnoremap <Esc> <C-\><C-n>

set autoindent
set smartindent
set background=dark

set colorcolumn=81
let g:load_doxygen_syntax=1

if !exists("autocommands_pol_loaded")
  let autocommands_pol_loaded = 1
  augroup POL
  autocmd VimLeave *.* mksession! $HOME/.config/nvim/session.vim
  augroup END
endif

function! SourceGDB()
    source ~/.config/nvim/bundle/neovim_gdb/plugin/neovim_gdb.vim
endfunction

function! Incr()
  let a = line('.') - line("'<")
  let c = virtcol("'<")
  if a > 0
    execute 'normal! '.c.'|'.a."\<C-a>"
  endif
  normal `<
endfunction
vnoremap <C-a> :call Incr()<CR>

set makeprg=./waf
set errorformat=
set errorformat+=%f:%l:%c:%m
set errorformat+=%f:%l:%m
set errorformat+=%DWaf:\ Entering\ directory\ `%f'
set errorformat+=%XWaf:\ Leaving\ directory
set errorformat+=%XWaf:\ Leaving\ directory

let b:nm_inc = split(system("pkg-config --cflags gtk+-3.0 ".
                           \"glib-2.0 freetype2 gsl eigen3  libftdi opencv ".
                           \"python3"))
py3 << EOF
import vim
try:
    numpy.distutils.misc_util
    lst = ' -I'.join(['']+numpy.distutils.misc_util.get_numpy_include_dirs())
    vim.eval('extend(b:nm_inc, split("%s"))' % lst)
except: pass
EOF

call extend(b:nm_inc, ['-std=c++14', '-pthread', '-fms-extensions', '-Iinclude',
                      \'-Iinclude/xvin', '-Iinclude/generated',
                      \'-Ibuild/xvin/include', '-Isrc/menus/plot/treat'])

let g:neomake_c_clang_maker  = {'args' : b:nm_inc + ['-std=gnu11'] }
let g:neomake_c_gcc_maker    = {'args' : b:nm_inc + ['-std=gnu11'] }
let g:neomake_cpp_clang_maker= {'args' : b:nm_inc + ['-std=c++14'] }
let g:neomake_cpp_gcc_maker  = {'args' : b:nm_inc + ['-std=c++14'] }
let g:neomake_python_enabled_makers = ['pylint', 'mypy']
autocmd BufWritePost *.cc Neomake
autocmd BufWritePost *.c Neomake
autocmd BufWritePost *.h Neomake
autocmd BufWritePost *.hh Neomake
autocmd BufWritePost *.hpp Neomake
autocmd BufWritePost *.py Neomake
autocmd BufWritePost *.jl Neomake

if !exists('g:airline_symbols')
let g:airline_symbols = {}
endif

"enable/disable fugitive/lawrencium integration >
let g:airline#extensions#branch#enabled = 1
let g:airline#extensions#neomake#enabled = 1

" unicode symbols
let g:airline_left_sep = '▶'
let g:airline_right_sep = '◀'
let g:airline_left_sep = '»'
let g:airline_right_sep = '«'
let g:airline_symbols.crypt = '🔒'
let g:airline_symbols.linenr = '␤'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.linenr = '␊'
let g:airline_symbols.branch = '⎇'
let g:airline_symbols.paste = 'ρ'
let g:airline_symbols.paste = 'Þ'
let g:airline_symbols.paste = '∥'
let g:airline_symbols.spell = 'Ꞩ'
let g:airline_symbols.notexists = '∄'
let g:airline_symbols.whitespace = 'Ξ'

set bdir=/home/pol/.local/share/vim/backup
