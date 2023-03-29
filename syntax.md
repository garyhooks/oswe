
### PowerShell

Get content from file
Wait and check every one second
Tail one line only
|
Select-String matching pattern only (to avoid all the other junk)

``
PS C:\log> Get-Content .\blah.log -wait -tail 1 | Select-String -Pattern "select version"
```


### Grep

-r = recursive
-n = provide line number
-w = match whole words only
^ = from the beginning of the line

> grep -rnw /var/www/whatever -e "^.*user_location.*public.*" --color

### Find

Find writable directory
> find /var/www/html/ -type d -perm -o+w

Find a file
> find / -name "moo.txt"
