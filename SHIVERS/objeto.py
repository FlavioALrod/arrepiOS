

class Dispositivo:

    def __init__(self,nome,ip,mac=None,fabricante=None):

        self.nome = nome
        self.ip = ip
        self.mac = mac
        self.fabricante = fabricante
        self.portas = []


    def __str__(self):

        return(
            f"Nome:         {self.nome}\n"
            f"IP:           {self.ip}\n"
            f"MAC           {self.mac}\n"
            f"Fabricante    {self.fabricante}\n"
            f"portas\n      {self.fabricante}"

        )

