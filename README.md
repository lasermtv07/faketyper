# FakeTyper
## Description
A CLI program that simulates keyboard input with an option to randomly generate a certain amount of errors in the output.
## Usage
`faketyper COMMAND options`
## Help
### Syntax
`[]` - switch  
`<>` - argument
### Commands
- `run [/k] [/d] [/b] [/w] <speed> <errors> <string> <error characters>` - types given string at given speed
   - `/k` - hides the onscreen keyboard
   - `/d` - disables the use of capital letters. Legacy function.
   - `/b` - writes out the typed string after typing finishes
   - `/w` - disables 3sec wait before typing starts
   - `<speed>` - typing speed, in characters per seconds
   - `<errors>` - probability of error appearing in the text, 0-100, 0 for no errors
   - `<string>` - the text that will be typed out
   - `<error characters>` - list of charcters that error characters will be repalced with. If u want all letters, write ' '
- `help [/s]` - displays this help
   - `/s` - show shorter version of this help
- `version [/c]` - prints the current version of the program
   - `/c` - prints more detailed version of version changelog

## Changelog
### Beta 0.3
#### MAJOR
- Added linux switch-writing support
- readded voluntary arguments
- added aliases
#### MINOR
- removed changelog command
- added v -c
### Beta 0.3.1 (newest)
#### MAJOR
none
#### MINOR
- fixed the broken help
- added syntax help if you type out command wrong
## Disclaimer
This is a beta and it is NOT SUPPOSED TO REPRESENT THE FULL PRODUCT! I only wanna backup it here as I'm gonna have to rewrite a big chunk of it, because the code is pretty bad. But if u use it anyway and find a bug, please report it using GitHub issues. Also don't look at it unless you wanna add it to your cringe compilation.

Your Laser =)
