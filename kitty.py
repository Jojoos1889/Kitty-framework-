#kitty framework 0.1
import os 
open("banner.sh")
print("KITTY FRAMEWORK")
input0 = input('attacco:')
if (input0 == 'xss'):
    input0B = input('target:')
    esecuzione = os.popen("xsser -u http://")+(input0B)
risultato = esecuzione.read()
if (input0 == 'nmap'):
    input0C = input('target:')
    esecuzione = os.popen("nmap -Pn")+(input0C)
risultato = esecuzione.read()
if (input0 == 'commix'):
    input0D = input("target")
    esecuzione = os.popen("commix -u")+(input0D)+(" --level=3")
risultato = esecuzione.read()
if (input0 == 'sqlmap'):
    input0E = input("comando sqlmap:")
    esecuzione = os.popen(input0E)
risultato = esecuzione.read()