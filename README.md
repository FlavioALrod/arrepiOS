<p align="center">
  <img src="https://static.wikia.nocookie.net/discoelysium_gamepedia_en/images/2/2d/Portrait_shivers.png/revision/latest?cb=20190719153914" alt="Logo do ARREPIOS" width="500"/>
</p>

<h1 align="center">🕵️‍♂️ ARREPIOS</h1>

# 🕵️‍♂️ ARREPIOS - Advanced Radar for Reconnaissance, Enumeration, and Protocol Inspection & Operational Security

*"Porque escanear rede dá arrepios... ou seria ARREPIOS?"*

## 🚧 EM DESENVOLVIMENTO ATIVO - VERSÃO ALPHA 🚧

> *"Por que usar nmap se você pode passar raiva com seu próprio script?"*

---

## 📡 O que é o ARREPIOS?

**ARREPIOS** é um framework de escaneamento de rede que veio para provar que:
- Sim, você pode reinventar a roda em Python
- Não, você não deveria, mas é mais divertido
- Sim, o nome é um acrônimo forçado (e eu estou orgulhoso disso)

---

## 🎯 O que isso faz (por enquanto)?

Este é um **escaneador de rede "profissional"** que:

- 🔍 Descobre dispositivos na sua rede (como se você já não soubesse)
- 🚪 Lista portas abertas (para você se sentir o Neo do Matrix)
- 📝 Gera XML (porque em 2026 a gente ainda sofre com isso)
- 📊 Mostra informações bonitinhas no terminal (UI/UX nota 10, segundo minha mãe)

---

## 🚀 Novidades em Desenvolvimento (Leia-se: "Coisas que eu prometo que vou fazer... eventualmente")

### 🔮 ARP Deep Dive
- **Análise ARP Avançada**: Vamos descobrir quem está mentindo na sua rede
- **Detecção de Spoofing**: Porque você nunca sabe se seu vizinho está se passando pelo roteador
- **Mapeamento ARP**: Descobrindo quem responde a quem (drama de novela das 8)

### 🎨 Interface do Usuário
- **Modo CLI Sarcástico**: Porque respostas sérias são superestimadas
- **Interface Gráfica**: Para os fracos que têm medo do terminal
- **Modo "Hacker dos Anos 90"**: Tela verde com texto caindo (opcional)

### 🔬 Análise de Protocolos
- **TCP/UDP Deep Scan**: Porque você precisa saber se é TCP ou UDP (spoiler: é sempre TCP)
- **ICMP Analysis**: Vamos ver quem está respondendo ping (e quem está ignorando você)
- **Protocol Fingerprinting**: Identificando serviços como um detetive de rede

### ⚡ Funcionalidades Avançadas
- **Comandos Remotos**: Porque dar comandos em dispositivos alheios é mais legal
- **Escaneamento Inteligente**: Apenas dispositivos que você realmente se importa
- **Modo Furtivo**: Para quando você quer se sentir um espião (use com responsabilidade)

### 📊 Extras
- **Exportação Múltipla**: XML, JSON, CSV, e talvez PDF (por que não?)
- **Relatórios Automáticos**: Para você mostrar ao chefe que está trabalhando
- **Histórico de Escaneamentos**: Para ver como sua rede evoluiu (ou não)

---

## ⏰ Previsão de Lançamento

**"Quando estiver pronto"™** - Ou seja, quando eu:
- Tiver tempo livre (hahaha)
- Não estiver procrastinando no YouTube
- Lembrar que esse projeto existe

---

## 🛠️ Tecnologias Envolvidas

| Tecnologia | Motivo |
|------------|--------|
| **Python 3.8+** | Porque sim |
| **Nmap** | O verdadeiro herói dessa história |
| **Scapy** | Futuro (talvez)  -- Para análise de pacotes como um verdadeiro nerd |
| **XML Parser** | Masoquismo puro |
| **Subprocess** | Porque chamar o nmap é mais fácil que implementar tudo |
| **Tkinter/PyQt** | Futuro (talvez) |
| **Café** | Combustível principal |

---
🗺️ Roadmap (Sonhos Molhados)
v0.1.0 - MVP (já foi)
├── Escaneamento básico
├── Exportação XML
└── Classes de dispositivos

v0.2.0 - Em desenvolvimento
├── Análise ARP
├── Mais opções de escaneamento
└── Interface melhorada

v0.3.0 - Futuro próximo (talvez)
├── Interface gráfica
├── Análise de protocolos
└── Comandos remotos

v1.0.0 - Lançamento oficial
├── Todas as features prometidas
├── Documentação completa
└── Café incluso (mentira)

🤝 Como Contribuir
Contribuições são MUITO bem-vindas! Siga estes passos:

    Faça um fork (é de graça, aproveite)

    Crie uma branch (git checkout -b feature/algo-incrivel)

    Faça suas alterações (e reze para não quebrar nada)

    Commit (git commit -m "Adicionei algo incrível")

    Push (git push origin feature/algo-incrivel)

    Abra um Pull Request (e espere eu lembrar de olhar)

Regras para contribuição:

    ✅ Código limpo é bom

    ✅ Comentários são melhores

    ✅ Sarcasmo nos comentários é OBRIGATÓRIO

    ❌ Nada de JSON (brincadeira... ou não)
⚠️ Avisos Importantes
🚨 Legal

    SÓ USE EM REDES QUE VOCÊ POSSUI AUTORIZAÇÃO

    Não seja o cara que vai parar no xkcd #838

    Sua mãe não vai te visitar na cadeia

🛡️ Segurança

    Pode disparar alertas em firewalls (culpe o nmap)

    Não execute em redes corporativas (a menos que queira uma conversa com o RH)

    Use com responsabilidade (ou não, eu não sou seu pai)

🐛 Bugs

    Se encontrar um bug, é uma "feature não documentada"

    Se não encontrar bugs, você não testou direito

    Se o programa explodir, reinicie o computador

P: Por que XML?
R: Porque:

    Todo mundo diz que XML está morto

    Eu quero provar que estão errados

    Na verdade, só queria usar o xml.etree.ElementTree uma vez

P: Isso funciona no Windows?
R: Teoricamente sim. Na prática... talvez. Me avise se funcionar.

P: Posso usar em produção?
R: Pode. Mas eu não recomendaria. Mas você pode. Mas não deveria. Mas se quiser...

## 📦 Como Instalar (se você realmente quiser)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/arrepiOS.git
cd arrepiOS

# Crie um ambiente virtual (porque somos profissionais)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
nmap "https://nmap.org/"

# Reze para funcionar
python3 main.py


