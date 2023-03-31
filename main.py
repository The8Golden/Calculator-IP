import os
import colorama



global ip



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


#Vérifie si l'information est bien un cidr ou non
def iscidr(ip):
    if len(iplist) == 1:
        return True
    else:
        return False


#verifie si l'ip ou le masque est valide et si elle est pas trop longue

def isIpValid(ip: list):
    iplist = ip.split(".")
    if len(iplist) == 4:
        for ips in iplist:
            if int(ips) < 0 or int(ips) > 255:
                    print("L'ip ou le masque n'est pas valide")
                    input()
                    exit()
        return True
    else:
        return False


#Convertir le cidr en masque
def cidrToMask(cidr: int):
    mask = [0, 0, 0, 0]
    for i in range(cidr):
        try :
            mask[i // 8] = mask[i // 8] + (1 << (7 - i % 8))
        except IndexError:
            print("Le cidr n'est pas valide")
            input()
            exit()
    return ".".join(map(str, mask))

#masque en cidr
def maskToCidr(mask: str):
    if isIpValid(mask):
        print
    else:
        print("Le masque n'est pas valide")
        input()
        exit()
    cidr = 0
    for octet in mask.split("."):
        binary = bin(int(octet))
        cidr += binary.count("1")
    return cidr


#Afficher la classe de l'ip
def classe(ip: int):
    if int(ip[0]) >= 1 and int(ip[0]) <= 126:
        return "A"
    elif int(ip[0]) >= 128 and int(ip[0]) <= 191:
        return "B"
    elif int(ip[0]) >= 192 and int(ip[0]) <= 223:
        return "C"
    elif int(ip[0]) >= 224 and int(ip[0]) <= 239:
        return "D"
    elif int(ip[0]) >= 240 and int(ip[0]) <= 255:
        return "E"
    else:
        return "Inconnue"
    
#Definir si c'est public ou privée 
def public(ip: int):
    if int(ip[0]) == 10:
        return "Privée"
    elif int(ip[0]) == 172 and int(ip[1]) >= 16 and int(ip[1]) <= 31:
        return "Privée"
    elif int(ip[0]) == 192 and int(ip[1]) == 168:
        return "Privée"
    else:
        return "Publique"

    

#Savoir si l'utilisateur met un masque ou une ip
question = input("""Voulez vous convertir un masque en cidr ou une ip en cidr ? 
1 - Masque en cidr
2 - Ip en cidr ou cidr en masque
 """)


if question == "1":
    clear()
    masque = input("Entrer votre masque : ")
    print("Le cidr est : " + colorama.Fore.GREEN  + str(maskToCidr(masque)) + colorama.Fore.RESET)
    input()
    exit()
elif question == "2":
    clear()
    ip = input("Entrer votre ip ou le cidr : ")


try : 
    iplist = ip.split(".")
except:
    pass




if iscidr(ip):
    print(cidrToMask(int(ip)))
    input()
else:
    if isIpValid(ip):
        pass
    else:
        print("L'ip n'est pas valide")
        exit()
    print(f"L'ip {ip} est de classe : " + colorama.Fore.GREEN + classe(iplist) + colorama.Fore.RESET)

    print(f"L'ip {ip} est : " + colorama.Fore.GREEN + public(iplist) + colorama.Fore.RESET)


    for number in iplist:
        if number.isdigit():
            if int(number) < 0 or int(number) > 255:
                print(colorama.Fore.YELLOW + "L'ip n'est pas valide" + colorama.Fore.RESET)
                input()
                exit()
        
        else:
            print("L'ip n'est pas valide")
            input()
            exit()


    print(colorama.Fore.YELLOW + "Nombre en binaire" + colorama.Fore.RESET)
    for number in iplist:
        print(f"{number} : "   + colorama.Fore.GREEN + bin(int(number)) + colorama.Fore.RESET)

    print("\n")
    print(colorama.Fore.YELLOW + "Nombre en hexadécimal" + colorama.Fore.RESET)
    for number in iplist:
        print(f"{number} : " + colorama.Fore.GREEN + hex(int(number)) + colorama.Fore.RESET)
    input()


