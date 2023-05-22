import time 
import colorama 
import os 
import nmap
import hashlib
import whois

def banner():
	print("""
████████████████████████████████████████
█─▄─▄─█─▄▄─█─▄▄─█▄─▄███▄─▄─▀█─▄▄─█▄─▀─▄█
███─███─██─█─██─██─██▀██─▄─▀█─██─██▀─▀██
▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄█▄▄▀

1]port scan \t 2]whois_lookup \t 3]calculate_hash
""")
	

# scaning
def scan():
    Myip = input("ip : ")
    nm = nmap.PortScanner()
    nm.scan(Myip, arguments=f'-p 1-1000') 

    for host in nm.all_hosts():
        print('Device: %s' % host)
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                print(f'Port: {colorama.Fore.BLUE}[{colorama.Fore.RESET}%s{colorama.Fore.BLUE}]{colorama.Fore.RESET}\tState: {colorama.Fore.BLUE}[{colorama.Fore.RESET}{colorama.Fore.GREEN}%s{colorama.Fore.RESET}{colorama.Fore.BLUE}]{colorama.Fore.RESET}' % (port, nm[host][proto][port]['state']))

# whois 
def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return str(e)


# hash
def calculate_hash(string):
    byte_string = string.encode('utf-8')

    hasher = hashlib.sha256()

    hasher.update(byte_string)

    hashed_string = hasher.hexdigest()

    return hashed_string


os.system("clear")

banner()

val = input("=> ")

if val == "1":
	scan()
elif val =="2":
	domain_name = input("domain name: ")
	result = whois_lookup(domain_name)
	print(result)
elif val =="3":
	input_string = input("string : ")
	hashed_result = calculate_hash(input_string)
	print("hash: ", hashed_result)

