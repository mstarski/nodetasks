if !has('python3')
  echo "Error: Required vim compiled with +python3"
  finish
endif

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF

import sys, vim
from os.path import normpath, join
plugin_root_dir = vim.eval('s:plugin_root_dir')
source_dir = normpath(join(plugin_root_dir, '..', 'src'))
sys.path.insert(0, source_dir)

import taskrunner

EOF

function! ToggleTaskRunner()
  python3 main()
endfunction

command! -nargs=0 ToggleTaskRunner call ToggleTaskRunner()
