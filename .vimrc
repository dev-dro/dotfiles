if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin('~/.vim/plugged')

Plug 'arcticicestudio/nord-vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'sheerun/vim-polyglot'
Plug 'tpope/vim-sensible',
Plug 'tpope/vim-repeat',
Plug 'tpope/vim-commentary',
Plug 'tpope/vim-surround'

call plug#end()

set colorcolumn=120
set incsearch smartcase
set hidden
set listchars=tab:▸\ ,eol:¬
set nobackup nowritebackup
set noerrorbells
set noswapfile
set nowrap
set number relativenumber
set smartindent expandtab tabstop=4 softtabstop=4 shiftwidth=4
set undodir=~/.vim/undodir
set undofile

colorscheme nord

" CoC
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"

nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

autocmd! CompleteDone * if pumvisible() == 0 | pclose | endif
