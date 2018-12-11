import requests
import re
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

karik = [2669,4660,4998,5752,3913,3584,2822,1776,1244,4118,5109,1762,2735,3735,3351,4991,4304,1699,2857,2647,5003,2868,1299,3983,3524,3889,2043,2526,2253,3448,5226,3870,3321,3185,4615,4476,4542,5510,4314,5257,4250,1544,4160,1283,2861,1606,4437,3885,2543,1317,5692,3642,4758,5705,2679,4575,3633,2281,2116,1105,5024,4651,1676,2939,2754,2263,4414,4810,3204,1410,3436,4375,4977,4379,3918,1783,3198,3893,3594,2569,4770,4389,2431,1940,1675,5627,3130,5852,5729,5338,3096,4835,4315,3311,4415,5599,2130,1141,3805,2414,5925,3842,5348,3715,2981,1441,2983,4685,4056,2643,5971,5885,2238,3762,1726,2089,1879,1421,5032,3822,5709,1839,1765,2827,4577,3465,5941,4694,3271,1909,4456,5339,1315,5119,5491,3382,2479,1440,3989,3938,1321,4607,1193,2668,1455]

for kari in karik:
    headers = {'User-Agent': 'Nyilvanos fordulo letolto 1.0',
    'From': 'rpotor@gmail.com',
    'X-Comment': 'Szoljatok plíz mielott bannoltok, ha ez nagyon floodol vagy ilyesmi :-)'
    }
    r = requests.get('http://beholder.hu/?m=tf&in=karakter.php&karakter=TF' + str(kari), headers=headers)
    
    forcsik = re.findall('(\d*\..forduló)', r.text)
    reinforcsik = re.findall('Reinkarnálás előtti fordulók', r.text)
	
    if len(forcsik) > 0:
        createFolder('c:/nyilvDL/' + str(kari) + '/')    
        forcsik = [s.replace('. forduló', '') for s in forcsik]
    
        for forcsi in forcsik:
            r = requests.get('http://www.beholder.hu/?m=tf&in=fordulo20.php&karakter=TF' + str(kari) + '&fordulo=' + forcsi, headers=headers)
            file = open('c:/nyilvDL/' + str(kari) + '/' + str(kari) + '-' + forcsi + '.html', "wb")
            file.write(r.content)
            file.close()
    
        print(str(kari) + ' karakter nyilvános fordulói letöltve (' + str(len(forcsik)) + ' forduló)')
    
    if len(reinforcsik) > 0:
        rein = requests.get('http://beholder.hu/?m=tf&in=karakter.php&karakter=TF' + str(kari) + '&reinkarnalt=1', headers=headers)
        reinforcsik = re.findall('(\d*\..forduló)', rein.text)
        if len(reinforcsik) > 0:
            createFolder('c:/nyilvDL/' + str(kari) + 'reink/')
            reinforcsik = [s.replace('. forduló', '') for s in reinforcsik]
            	
            for forcsi in reinforcsik:
                r = requests.get('http://www.beholder.hu/?m=tf&in=fordulo20.php&karakter=TF' + str(kari) + '&fordulo=' + forcsi + '&reinkarnalt=1', headers=headers)
                file = open('c:/nyilvDL/' + str(kari) + 'reink/' + str(kari) + '-' + forcsi + '.html', "wb")
                file.write(r.content)
                file.close()
    
            print(str(kari) + ' reinkarnált karakter nyilvános fordulói letöltve (' + str(len(reinforcsik)) + ' forduló)')