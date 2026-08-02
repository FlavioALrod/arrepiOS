import subprocess

def scanear():
    resultado = subprocess.run(
        ["nmap", "-sn", "-oX", "rede.xml", "192.168.18.0/24"],
        #["nmap", "-sn", "192.168.18.0/24"],
        capture_output=True,
        text=True
    
    )

#print(resultado.stdout)