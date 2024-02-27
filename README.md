
> ***NOTE:***<br>
> This project is unlikely to be  maintained as of the last release v1.1.1, unless I am bothered to use it again, which I doubt

<h1 align=center>FakeTyper</h1>

<div align=center>
<img src="https://img.shields.io/badge/Language-Python-yellow" />
<img src="https://img.shields.io/badge/Editor-Vim-green" />
<img src="https://img.shields.io/badge/Library-pynput-red" />
<img src="https://img.shields.io/badge/Library-getkey-red" />
</div>

## Dependencies
- python3
- pynput
- getkey
## GNU style --help
```
Usage: ft run [OPTIONS]   SPEED ERR_COUNT STRING ERR_CHARACTERS*
ft help [OPTIONS]
ft version [OPTIONS]
ft tip [OPTIONS]
Fakes typing STRING on keyboard with SPEED and voluntary ERRORS configured with ERR_COUNT and ERR_CHARACTERS
Options:
run -k    hides onscreen keyboard
    -d    Dont use, legacy feature
    -b    writes out the typed string after typing finishes
    -w    stops 3s wait before typing
    -t    read STRING from a .txt file
    -s    disable keyboard aliases (¦.. backspace; ^.. space; ¬.. newline)
    -l    wrotes in endless Loop
    -e    newlines with every space
    -c    use Czech kb layout
    -f    use Finnish kb layout
    -r    use Russian kb layour
help -s   shortened
version -c    show changelog
tip -a    write all
---
(c) lasermtv07, 2023
```
## Current version
1.1.1
