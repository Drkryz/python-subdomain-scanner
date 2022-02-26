import sys
import socket


args = sys.argv

if len(args) == 1:
    print("Usage: python main.py [domain] -w [wordlist]")
    sys.exit(1)


if args[2] == '-w' or args[2] == '-wordlist':

    subdmain_word_list = args[3]

    founds = []

    try:
        filePath = open(subdmain_word_list, 'r')
    except FileNotFoundError:
        print('File not found')
        sys.exit()

    for line in filePath:
        website_uri = line.strip() + "." + args[1]
       
        try:
            website_response = socket.gethostbyname(website_uri)

            strfounds = "[+] " + website_uri + ": " + website_response
            founds.append(strfounds)

            print("[+] " + website_uri + " " + website_response)
        except socket.gaierror:
            print("[-] " + website_uri + " " + "No response")

    filePath.close()

    if len(founds) == 0:
        print("No results found")

    else:
        print("\n[+] Found " + str(len(founds)) + " results")
        print("[=] Results:" + "\n" + "\n".join(founds))