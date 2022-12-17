# FakeTyper
## Description
CLI program that simulates keyboard input with an option to randomly generate a certain amount of errors in the output.
## Usage
`faketyper COMMAND options`
## Version
Beta 0.2, the 'less if update'
## Help
### Syntax
`
[] - switches
<> - argument. All arguments are MANDATORY! *If you want to choose default settings, you have to use ' ',
even though it works only with run <error characters>.`
### Commands
-------------------------------------------------------------------
`run: run [/k] [/d] [/b] [/w] <speed> <errors> <string> <error characters*> - starts the typing
   -/k hides the onscreen keyboard
   -/d disables the use of capital letters. Legacy function.
   -/b writes out the typed string after typing finishes
   -/w disables 3sec wait before typing starts
   <speed> typing speed, in characters per seconds
   <errors> probability of error appearing in the text, 0-100, 100 for no errors
   <string> the text that will be typed out
   <error characters>* list of charcters that error characters will be repalced with. If u want all letters, write ' '
   help: help [/s] - displays this help
   -/s show shorter version of this help
   version: version [/c] - prints the current version of the program
   -/c prints more detailed version of version changelog`
   -----------------------------------------------------------------
`help: help [/s] - displays this help
    -/s show shorter version of this help`
`version: version [/c] - prints the current version of the program
       -/c prints more detailed version of version changelog`

## Changelog
### Beta 0.2
#### MAJOR:
-CLI system updated
-Command switches added
-Removed support for voluntary arguments and aliases
#### MINOR:
- changed the run command
-added switches /k /s /d /w
-removed the alias r
- changed the help command
-added the /s switch
-changed the version command
-added the /c switch
-removed changelog command
## Disclaimer
This is a beta and it is NOT SUPPOSED TO REPRESENT THE FULL PRODUCT! I only wanna backup it here as Im gonna have to rewrite a big chunk of it, because the code is pretty bad. But if u use it anyway and find a bug, please report it using GitHub issues. Also dont look at it unless you wanna add it. to your cringe compilation.

Your Laser =)
