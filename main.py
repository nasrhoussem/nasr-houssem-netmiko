from netmiko import ConnectHandler

def acces_netmiko():
    # Paramètres de connexion au routeur Cisco C8000V
    cisco_router = {
        "device_type": "cisco_xr",       # type adapté pour IOS XR
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
    }

    print("[*] Connexion au routeur...")
    net_connect = ConnectHandler(**cisco_router)

    # 1) Affiche la date côté routeur
    print("\n[+] Affichage de la date (show clock)")
    clock_output = net_connect.send_command("show clock")
    print(clock_output)

    # 2) Enregistre les interfaces dans le fichier interfaces.txt
    print("\n[+] Récupération des interfaces (show interfaces)")
    interfaces_output = net_connect.send_command("show interfaces")

    with open("interfaces.txt", "w") as f:
        f.write(interfaces_output)

    print("[✓] Interfaces sauvegardées dans interfaces.txt")

    net_connect.disconnect()
    print("[*] Déconnexion terminée.\n")


def dire_bonjour():
    print("Hello, Git!")


if __name__ == "__main__":
    dire_bonjour()
    acces_netmiko()










print("Hello,Git!")
