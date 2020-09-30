if !has('python3')
  echo "Error: Required vim compiled with +python3"
  finish
endif

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

function! ToggleTaskRunner()
  py3file plugin_root_dir . "/../src/taskrunner.py"
endfunction

command! -nargs=0 ToggleTaskRunner call ToggleTaskRunner()
