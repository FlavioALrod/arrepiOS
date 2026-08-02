import xml.etree.ElementTree as ET
from objeto import Dispositivo as d
 

def montagem():
    dados = ET.parse("rede.xml")
    raiz = dados.getroot()
    dispositivos = []
    for host in raiz.findall("host"):
        endereco = host.find("address")
        ip = endereco.attrib["addr"]
        hostname = host.find("hostnames/hostname")
        if hostname is None:
            nome = "Desconhecido"
        else:
            nome = hostname.attrib["name"]
        dispositivos.append(d(nome,ip))
    return dispositivos