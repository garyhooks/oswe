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
