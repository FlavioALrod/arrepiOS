from leitor import montagem
from radar import scanear


print("analisando a rede......")

scanear()

print("\nDispositivos encontrdos")

print("-"*50)

dispositivos = montagem()

for disposito in dispositivos:
    print(disposito)
    print("-"*45)