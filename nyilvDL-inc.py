import requests
import re
import os
import shutil
from datetime import datetime

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

karik = [4443,5421]

mikortol = '2018-11-25'
targetdate = datetime.strptime(mikortol, '%Y-%m-%d')

for kari in karik:
    headers = {'User-Agent': 'Nyilvanos fordulo letolto 1.0',
    'From': 'rpotor@gmail.com',
    'X-Comment': 'Szoljatok plíz mielott bannoltok, ha ez nagyon floodol vagy ilyesmi :-)'
    }
    r = requests.get('http://beholder.hu/?m=tf&in=karakter.php&karakter=TF' + str(kari), headers=headers)
    
    forcsik = re.findall('(\d*\..forduló).{8}(\d{4}\-\d{2}\-\d{2})', r.text)
    reinforcsik = re.findall('Reinkarnálás előtti fordulók', r.text)
	
    if len(forcsik) > 0:
        createFolder('c:/nyilvDL/' + str(kari) + '/')    
        forcsik = [[s[0].replace('. forduló', ''), s[1]] for s in forcsik]
        szamlalo = 0
		
        for forcsi in forcsik:
            forcsidate = datetime.strptime(forcsi[1], '%Y-%m-%d')
            if forcsidate > targetdate:
                szamlalo = szamlalo + 1			
                r = requests.get('http://www.beholder.hu/?m=tf&in=fordulo20.php&karakter=TF' + str(kari) + '&fordulo=' + forcsi[0], headers=headers)
                file = open('c:/nyilvDL/' + str(kari) + '/' + str(kari) + '-' + forcsi[0] + '.html', "wb")
                file.write(r.content)
                file.close()
    
        print(str(kari) + ' karakter ' + mikortol + ' utáni nyilvános fordulói letöltve (' + str(szamlalo) + ' forduló)')
    
    if len(reinforcsik) > 0:
        rein = requests.get('http://beholder.hu/?m=tf&in=karakter.php&karakter=TF' + str(kari) + '&reinkarnalt=1', headers=headers)
        reinforcsik = re.findall('(\d*\..forduló).{8}(\d{4}\-\d{2}\-\d{2})', rein.text)
        if len(reinforcsik) > 0:
            createFolder('c:/nyilvDL/' + str(kari) + 'reink/')
            reinforcsik = [[s[0].replace('. forduló', ''), s[1]] for s in reinforcsik]
            szamlalo = 0
            	
            for forcsi in reinforcsik:
                forcsidate = datetime.strptime(forcsi[1], '%Y-%m-%d')
                if forcsidate > targetdate:
                    szamlalo = szamlalo + 1				
                    r = requests.get('http://www.beholder.hu/?m=tf&in=fordulo20.php&karakter=TF' + str(kari) + '&fordulo=' + forcsi[0] + '&reinkarnalt=1', headers=headers)
                    file = open('c:/nyilvDL/' + str(kari) + 'reink/' + str(kari) + '-' + forcsi[0] + '.html', "wb")
                    file.write(r.content)
                    file.close()
            if szamlalo == 0:
                shutil.rmtree('c:/nyilvDL/' + str(kari) + 'reink/')			
            else:
                print(str(kari) + ' karakter ' + mikortol + ' utáni, reinkarnálás előtti nyilvános fordulói letöltve (' + str(szamlalo) + ' forduló)')