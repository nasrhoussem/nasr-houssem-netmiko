Mon Projet Netmiko

mkdir prenom-nom-netmiko

cd prenom-nom-netmiko

git init

echo 'print("Hello, Git!")' > main.py

git add main.py

git commit -m "Ajout du script Python principal"

git add main.py

git  checkout -b feature/netmiko

git commit -m "Ajout du script Python principal"

git log

git checkout -b feature/netmiko

vim main.py

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

   
    print("\n[+] Affichage de la date (show clock)")
    clock_output = net_connect.send_command("show clock")
    print(clock_output)

 
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

git add main.py
git commit -m "Ajout de la fonction acces_netmiko avec Netmiko"
git log --oneline
git checkout main
git merge feature/netmiko
git log --oneline
git remote add origin https://github.com/nasrhoussem/nasr-houssem-netmiko.git
git push -u origin main
git fetch origin
git checkout -b feature/salut origin/feature/salut

 vim main.py
 
def dire_salut():
    print("Salut, Git!")


if __name__ == "__main__":
    dire_salut()
git add main.py
git commit -m "Ajout de la fonction dire_salut"
git push origin feature/salut
git checkout main
git pull origin main









