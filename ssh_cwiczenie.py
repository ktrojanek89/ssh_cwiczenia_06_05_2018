#!USR/BIN/PYTHON
import paramiko
print "Ala"
zmienna=paramiko.SSHClient()
type(zmienna)
zmienna.set_missing_host_key_policy(paramiko.AutoAddPolicy())
zmienna.connect("localhost", username='tester02', password='karolina')
wejscie,wyjscie,bledy=zmienna.exec_command("cat /etc/passwd")
print wyjscie.read()
