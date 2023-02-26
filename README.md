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

##Current version
1.1.0
