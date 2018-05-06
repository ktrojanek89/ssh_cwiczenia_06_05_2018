#!USR/BIN/PYTHON

#niezmienna czesc 1
import paramiko
#print "Ala"
zmienna=paramiko.SSHClient()
type(zmienna)
zmienna.set_missing_host_key_policy(paramiko.AutoAddPolicy())
zmienna.connect("localhost", username='tester02', password='karolina')
wejscie,wyjscie,bledy=zmienna.exec_command("cat /etc/passwd")
rezultat=wyjscie.read()

#czesc 2
lista_linii=rezultat.split("\n")
tester03_jest=False

for el in lista_linii:
    if el.find("tester02")+1:
        tester03_jest=True
        #print(el)
        break

if tester03_jest:
    print("istnieje")
else:
    print("nie istnieje")

#czesc 3

lista_linii=rezultat.split("\n")
innyuzytkownik=False

for el in lista_linii:
    if el.find("tester02")+1:
        #innyuzytkownik=True
        #print(el)
        break

if innyuzytkownik:
    print("istnieje")
else:
    print("nie istnieje")
