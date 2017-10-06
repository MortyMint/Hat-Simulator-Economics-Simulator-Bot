#import os
import random as r
import time

namelist = []
pricelist = []
curlist = []
dif = []
raw = ''
lines = 0

def fix(p):
    q = str(p)
    if q[len(q)-2] != '.':
        q = q[:-1]
        q += q[len(q)-1]
    else:
        q += q[len(q) - 1]
    upd = float(q)
    return upd

def readlines(ls):
    with open('itemlist.txt', 'r') as file:
        ls = 0
        for line in file:
            ls += 1
    for i in range(ls):
        dif.append(0.0)
    file.close()
    return ls

def readtext():
    file = open('itemlist.txt', 'r')
    file.seek(0)
    for i in range(lines):
        raw = file.readline()
        if i != lines-1:
            raw = raw[0:-1]
        Qname = ''
        j = 0
        while raw[j] != ' ':
            Qname += raw[j]
            j += 1
        namelist.append(Qname)
        Qname = ''
        j += 1
        while raw[j] != ' ':
            Qname += raw[j]
            j += 1
        pricelist.append(float(Qname))
        Qname = ''
        j += 1
        while j != len(raw):
            Qname += raw[j]
            j += 1
        curlist.append(Qname)
    #CLOSE
    file.close()

def prandom(q,x,y,d):  #0 - DECREASE | 1 - INCREASE
    s = r.randint(x,y)
    res = q
    if d == 0:
        for i in range(s):
            res -= 0.11
    else:
        for i in range(s):
            res += 0.11
    return res

def decide():
    for i in range(lines):
        dif[i] = pricelist[i]
        if i == 0: #key
            if pricelist[i] > 35:  #keys price peak -- 35 ref (CAN WE PLEASE STAHP? PLEASE? PLEEEEEEEASE? (c)Morty )
                pricelist[i] -= prandom(pricelist[i], 2, 6, 0)
            elif pricelist[i] < 5: #(ME LITERALLY CRYING ABOUT TF2 KEY PRICE IN REF)
                pricelist[i] -= prandom(pricelist[i], 2, 3, 1)
            else:
                a = r.randint(0, 15)
                if a <= 3:
                    pricelist[i] = prandom(pricelist[i], 1, 3, 0)
                elif a >= 13:
                    pricelist[i] = prandom(pricelist[i], 1, 3, 1)
            pricelist[i] = round(pricelist[i], 2)
            pricelist[i] = fix(pricelist[i])
            if pricelist[i] + 0.01 == round(pricelist[i]):
                pricelist[i] += 0.01
            dif[i] -= pricelist[i]
            dif[i] = -round(dif[i],2)
        else:
            if curlist[i] == 'ref': #refined items
                if pricelist[i] % 10 == 0:
                    pricelist[i]-=0.01
                if pricelist[i] <= 1.33:
                    a = r.randint(0, 3)
                    if a == 1:
                        pricelist[i] += 0.11
                elif pricelist[i] <= 3:
                    a = r.randint(0, 15)
                    if a <= 5:
                        pricelist[i] = prandom(pricelist[i], 1, 3, 0)
                    elif a > 10:
                        pricelist[i] = prandom(pricelist[i], 1, 3, 1)
                elif pricelist[i] > 3:
                    a = r.randint(0, 15)
                    if a <= 5:
                        pricelist[i] = prandom(pricelist[i], 1, 4, 0)
                    elif a > 10:
                        pricelist[i] = prandom(pricelist[i], 1, 6, 1)
                pricelist[i] = round(pricelist[i],2)
                pricelist[i] = fix(pricelist[i])
                if pricelist[i] + 0.01 == round(pricelist[i]):
                    pricelist[i]+=0.01
                dif[i] -= pricelist[i]
                dif[i] = -round(dif[i],2)
            if curlist[i] == 'keys': #key items
                if pricelist[i] > 10 and pricelist[i] < 30:
                    pricelist[i] = round(pricelist[i])
                    a = r.randint(0, 15)
                    if a <= 4:
                        pricelist[i] += r.randint(1, 3)
                    elif a > 11:
                        pricelist[i] -= r.randint(1, 2)
                    dif[i] -= pricelist[i]
                    dif[i] = -round(dif[i])
                elif pricelist[i] > 30:
                    pricelist[i] = round(pricelist[i])
                    a = r.randint(0, 15)
                    if a <= 3:
                        pricelist[i] += r.randint(2, 15)
                    elif a > 12:
                        pricelist[i] -= r.randint(2, 10)
                    dif[i] -= pricelist[i]
                    dif[i] = -round(dif[i])
                else:
                    a = r.randint(0, 10)
                    if a <= 3:
                        pricelist[i] -= 0.1
                    elif a >= 8:
                        pricelist[i] += 0.1
                    pricelist[i] = round(pricelist[i],1)
                    dif[i] -= pricelist[i]
                    dif[i] = -round(dif[i],1)
            #CONVERT REF TO KEYS AND KEYS TO REF
            for i in range(lines):
                if pricelist[i] > pricelist[0] and curlist[i] == 'ref':
                    pricelist[i] /= pricelist[0]
                    pricelist[i] = round(pricelist[i], 1)
                    curlist[i] = 'keys'
                if pricelist[i] < 1 and curlist[i] == 'keys':
                    pricelist[i] = 0.9
                    pricelist[i] *= pricelist[0]
                    pricelist[i] = round(pricelist[i], 2)
                    fix(pricelist[i])
                    pricelist[i] = round(pricelist[i], 2)
                    curlist[i] = 'ref'


def show():
    for i in range(lines):
        if dif[i] < 0:
            print(namelist[i]+' '+str(pricelist[i])+' '+curlist[i]+' ('+str(dif[i])+')')
        elif dif[i] == 0:
            print(namelist[i] + ' ' + str(pricelist[i]) + ' ' + curlist[i])
        else:
            print(namelist[i] + ' ' + str(pricelist[i]) + ' ' + curlist[i] + ' (+' + str(dif[i]) + ')')
    print('____________________________')

def rewrite():
    file = open('itemlist.txt', 'a+')
    file.seek(0)
    file.truncate()
    for i in range(lines):
        if i != lines-1:
            file.write(namelist[i]+' '+str(pricelist[i])+' '+curlist[i]+'\n')
        else:
            file.write(namelist[i] + ' ' + str(pricelist[i]) + ' ' + curlist[i])
    file.close()

timefile = open('time.txt','r')
tick = int(timefile.read())
lines = readlines(lines)
readtext()
show()
while True:
    time.sleep(tick)
    decide()
    show()
    rewrite()
