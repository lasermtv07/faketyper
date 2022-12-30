# FakeTyper
## Description
A CLI program that simulates keyboard input with an option to randomly generate a certain amount of errors in the output.
## Usage
`faketyper COMMAND switches arguments`
## Help
### Syntax
`[]` - switches, typed either `/x` or `-x`
`{}` - language switches, used to set keyboard layout (added beta v0.4)
`<>` - mandatory argument
`| |` - optional arguments
`@` - Alternative name (first letter of the command - can also be used as keyboard shortcut)
### Commands
- `run @r [/k] [/d] [/b] [/w] {/c} {/f} {/r} <speed> <errors> <string> |error characters|` - types given string at given speed
   - `[/k]` hides the onscreen keyboard
   - `[/d]` disables the use of capital letters. Legacy function, /doesnt work anymore change of library/
   - `[/b]` writes out the typed string after typing finishes
   - `[/w]` disables 3sec wait before typing starts
   - `[/t]` makes the program read input string from a .txt file instead of the string typed into command
   - `[/s]` disables the use of keyboard aliases; List here:
      - .`■` or `¦`.. Backspace 
   - `{/c}` sets the keyboard layout to Czech
   - `{/f}` sets the keyboard layout to Finnish
   - `{/r}` sets the keyboard layout to Russian
   - `<speed>` typing speed, in characters per seconds
   - `<errors>` amount of errors appearing in the text, 0-100, 100 for no errors
   - `<string>` the text that will be typed out
   - `|error characters|` list of characters to be replaced by - optional
- `help @h [/s]` - displays this help
   - `[/s]` show shorter version of this help
- `version @v [/c]` - prints the current version of the program
   - `[/c]` prints more detailed `version` with the version changelog
- `tip @t [/a]` - prints a random tip
   - `[/a]` prints all tips

## Changelog
### Beta 0.4* - You'll love it! (newest)
#### MAJOR
- Ability to import .txt files (using the /t switch)
- Ability to use multiple keyboard layouts with the /c /f /r switches
   - Added Czech layout to the keyboard visualiser
   - Added Finnish keyboard the keyboard visualizer
   - Added Russian keyboard to the keyboard visualiser
   - (leave empty if you want to keep the english keyboard)
- Error generator algorithmus updated; if you want to know how, open source code and look
- Added keyboard aliases; "■" or "¦" now symbolize backspace
   - Can be disabled with the /s switch
#### MINOR
- Writing out text when typing out the text now works as intended
- Added the /a switch to tip command; via help
- Edited and improved the help
- Unspecified bugfixes
## Disclaimer
This is still a beta version, so it's still a *bit* rough around the edges. If you find a bug or have asuggestion, make sure to write it into the issues :)
<br/>
<br/>
**Application doesn't use sematic versioning (MAJOR.MINOR.PATCH), it uses my own instead (RELEASE_STAGE.MAJOR.MINOR)*
s
