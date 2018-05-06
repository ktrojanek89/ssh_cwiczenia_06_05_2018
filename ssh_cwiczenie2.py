#funkcja podsumowujaca ssh_cwiczenie.py
#!USR/BIN/PYTHON
import paramiko
zmienna=paramiko.SSHClient()
type(zmienna)
zmienna.set_missing_host_key_policy(paramiko.AutoAddPolicy())
zmienna.connect("localhost", username='tester02', password='karolina')
wejscie,wyjscie,bledy=zmienna.exec_command("cat /etc/passwd")
rezultat=wyjscie.read()

def nazwauzytkownika(arg):
    lista_linii=rezultat.split("\n")
    uzytkownik_istnieje=False

    for el in lista_linii:
        if el.find(arg)+1:
            uzytkownik_istnieje=True
            #print(el)
            break

    if uzytkownik_istnieje:
        print("istnieje")
    else:
        print("nie istnieje")

nazwauzytkownika("tester02")
nazwauzytkownika("tester00")
