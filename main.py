# excel export
from export_data import export_to_excel

from ExportDataGoogle import export_to_google

# empty lists
players = []
heartsgp = []
heartsw = []
heartsl = []
crownsgp = []
crownsw = []
crownsl = []
dicegp = []
dicew = []
dicel = []
dicenp = []
diceiw = []
olymgp = []
olymw = []
olymg = []
olyms = []
olymb = []

# player file
p = open("players", 'r')

# hearts files
hgp = open("hearts games played", 'r')
hw = open("hearts wins", 'r')
hl = open("hearts losses", 'r')

# 5 crowns files
cgp = open("5 crowns games played", 'r')
cw = open("5 crowns wins", 'r')
cl = open("5 crowns losses", 'r')

# dice files
dgp = open("dice games played", 'r')
dw = open("dice wins", 'r')
dl = open("dice losses", 'r')
dnp = open("dice no points", 'r')
diw = open("dice instant wins", 'r')

# olympic files
op = open("olympics participated", 'r')
ow = open("olympic wins", 'r')
og = open("olympic golds", 'r')
osi = open("olympic silvers", 'r')
ob = open("olympic bronzes", 'r')

# players list
for i in p:
    players.append(i.strip())

# hearts lists
for i in hgp:
    heartsgp.append(int(i))
for i in hw:
    heartsw.append(int(i))
for i in hl:
    heartsl.append(int(i))

# 5 crowns lists
for i in cgp:
    crownsgp.append(int(i))
for i in cw:
    crownsw.append(int(i))
for i in cl:
    crownsl.append(int(i))

# dice lists
for i in dgp:
    dicegp.append(int(i))
for i in dw:
    dicew.append(int(i))
for i in dl:
    dicel.append(int(i))
for i in diw:
    diceiw.append(int(i))
for i in dnp:
    dicenp.append(int(i))

# olympic lists
for i in op:
    olymgp.append(int(i))
for i in ow:
    olymw.append(int(i))
for i in og:
    olymg.append(int(i))
for i in osi:
    olyms.append(int(i))
for i in ob:
    olymb.append(int(i))

while True:
    if (
        len(players) == len(heartsgp) == len(heartsw) == len(heartsl) == len(crownsgp) == len(crownsw) == len(
            crownsl) == len(dicegp) == len(dicew) == len(dicel) == len(diceiw) == len(dicenp) == len(olymgp) == len(
            olymw) == len(olymg) == len(olyms) == len(olymb)
    ):
        break
    else:
        print("ERROR: Lengths of lists")
        quit()


# add new player function
def newplayer():
    players.append(name)
    heartsgp.append(0)
    heartsw.append(0)
    heartsl.append(0)
    crownsgp.append(0)
    crownsw.append(0)
    crownsl.append(0)
    dicegp.append(0)
    dicew.append(0)
    dicel.append(0)
    dicenp.append(0)
    diceiw.append(0)
    olymgp.append(0)
    olymw.append(0)
    olymg.append(0)
    olyms.append(0)
    olymb.append(0)


game = str(input("Game: ")).lower()

# hearts code
if game == "hearts":
    numplayers = int(input("Number of players: "))
    for i in range(numplayers):
        name = str(input("Player name: ")).lower()
        for j in range(len(players)):
            if name == players[j]:
                break
        else:
            newplayer()
        win = str(input("Winner?: ")).lower()
        if win == "yes":
            for j in range(len(players)):
                if name == players[j]:
                    heartsw[j] += 1
        loss = str(input("loser?: ")).lower()
        if loss == "yes":
            for j in range(len(players)):
                if name == players[j]:
                    heartsl[j] += 1
        for j in range(len(players)):
            if name == players[j]:
                heartsgp[j] += 1

# 5 crowns code
if game == "5 crowns":
    numplayers = int(input("Number of players: "))
    for i in range(numplayers):
        name = str(input("Player name: ")).lower()
        for j in range(len(players)):
            if name == players[j]:
                break
        else:
            newplayer()
        win = str(input("Winner?: ")).lower()
        if win == "yes":
            for j in range(len(players)):
                if name == players[j]:
                    crownsw[j] += 1
        loss = str(input("loser?: ")).lower()
        if loss == "yes":
            for j in range(len(players)):
                if name == players[j]:
                    crownsl[j] += 1
        for j in range(len(players)):
            if name == players[j]:
                crownsgp[j] += 1

# dice code
if game == "dice":
    numplayers = int(input("Number of players: "))
    for i in range(numplayers):
        name = str(input("Player name: ")).lower()
        for j in range(len(players)):
            if name == players[j]:
                break
        else:
            newplayer()
        win = str(input("Winner?: ")).lower()
        if win == "yes":
            iwin = str(input("Instant win?: ")).lower()
            if iwin == "yes":
                for j in range(len(players)):
                    if name == players[j]:
                        diceiw[j] += 1
            for j in range(len(players)):
                if name == players[j]:
                    dicew[j] += 1
        loss = str(input("loser?: ")).lower()
        if loss == "yes":
            np = str(input("On the board?: ")).lower()
            if np == "no":
                for k in range(len(players)):
                    if name == players[k]:
                        dicel[k] += 1
            for j in range(len(players)):
                if name == players[j]:
                    dicel[j] += 1
        for j in range(len(players)):
            if name == players[j]:
                dicegp[j] += 1

if game == "olympics":
    numteam = int(input("Number of teams: "))
    perteam = int(input("Number of players per team: "))
    for i in range(numteam):
        team = []
        for j in range(perteam):
            name = str(input("Player " + str(j) + " on team " + str(i) + " name: "))
            for k in range(len(players)):
                if name == players[k]:
                    break
            else:
                newplayer()
            team.append(name)
        for j in range(len(team)):
            for k in range(len(players)):
                if team[j] == players[k]:
                    olymgp[k] += 1
        win = str(input("Did team " + str(i) + " win? ")).lower()
        if win == "yes":
            for k in range(len(team)):
                for x in range(len(players)):
                    if team[k] == players[x]:
                        olymw[x] += 1
        golds = int(input("Team " + str(i) + " golds: "))
        silvers = int(input("Team " + str(i) + " silvers: "))
        bronzes = int(input("Team " + str(i) + " bronzes: "))
        for j in range(len(team)):
            for k in range(len(players)):
                if team[j] == players[k]:
                    olymg[k] += golds
                    olyms[k] += silvers
                    olymb[k] += bronzes

if game == "add":
    print("adding data to spreadsheet...")

# adding values back to files

# player file
p = open("players", 'w')
for i in players:
    p.write(i + "\n")

# hearts files
hgp = open("hearts games played", 'w')
for i in heartsgp:
    hgp.write(str(i) + "\n")
hw = open("hearts wins", 'w')
for i in heartsw:
    hw.write(str(i) + "\n")
hl = open("hearts losses", 'w')
for i in heartsl:
    hl.write(str(i) + "\n")

# 5 crowns files
cgp = open("5 crowns games played", 'w')
for i in crownsgp:
    cgp.write(str(i) + "\n")
cw = open("5 crowns wins", 'w')
for i in crownsw:
    cw.write(str(i) + "\n")
cl = open("5 crowns losses", 'w')
for i in crownsl:
    cl.write(str(i) + "\n")

# dice files
dgp = open("dice games played", 'w')
for i in dicegp:
    dgp.write(str(i) + "\n")
dw = open("dice wins", 'w')
for i in dicew:
    dw.write(str(i) + "\n")
dl = open("dice losses", 'w')
for i in dicel:
    dl.write(str(i) + "\n")
dnp = open("dice no points", 'w')
for i in dicenp:
    dnp.write(str(i) + "\n")
diw = open("dice instant wins", 'w')
for i in diceiw:
    diw.write(str(i) + "\n")

# olympic files
op = open("olympics participated", 'w')
for i in olymgp:
    op.write(str(i) + "\n")
ow = open("olympic wins", 'w')
for i in olymw:
    ow.write(str(i) + "\n")
og = open("olympic golds", 'w')
for i in olymg:
    og.write(str(i) + "\n")
osi = open("olympic silvers", 'w')
for i in olyms:
    osi.write(str(i) + "\n")
ob = open("olympic bronzes", 'w')
for i in olymb:
    ob.write(str(i) + "\n")

# close files
p.close()
hgp.close()
hw.close()
hl.close()
cgp.close()
cw.close()
cl.close()
dgp.close()
dw.close()
dl.close()
diw.close()
dnp.close()
op.close()
ow.close()
og.close()
osi.close()
ob.close()

print(players)

export_to_excel(players, heartsgp, heartsw, heartsl, crownsgp, crownsw, crownsl, dicegp, dicew, dicel, dicenp, diceiw,
                olymgp, olymw, olymg, olyms, olymb)

export_to_google(players, heartsgp, heartsw, heartsl, crownsgp, crownsw, crownsl, dicegp, dicew, dicel, dicenp, diceiw,
                 olymgp, olymw, olymg, olyms, olymb)
