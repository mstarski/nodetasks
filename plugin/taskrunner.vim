if !has('python3')
  echo "Error: Required vim compiled with +python3"
  finish
endif

function! ToggleTaskRunner()
  py3file "../src/taskrunner.py"
endfunction

command! -nargs=0 ToggleTaskRunner call ToggleTaskRunner()
