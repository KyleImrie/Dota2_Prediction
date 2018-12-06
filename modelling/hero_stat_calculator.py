import pandas as pd
import numpy as np
import urllib
from bs4 import BeautifulSoup

oldTable = pd.read_csv('Dota2_data/hero_names.csv')
oldTable = oldTable.sort_values('localized_name').reset_index()
soup = BeautifulSoup(open('Dota2_data/dotateamhtml.txt'), 'html.parser')
heroes = soup.find_all('li')

names = []
carry = []
disables = []
initiation = []
nukers = []
pushers = []
support = []
durable = []

for hero in heroes:
    names.append(hero['data-name'])
    carry.append(hero['data-carry'])
    disables.append(hero['data-disabler'])
    initiation.append(hero['data-initiator'])
    nukers.append(hero['data-nuker'])
    pushers.append(hero['data-pusher'])
    support.append(hero['data-support'])
    durable.append(hero['data-durable'])

names[3] = "Anti-Mage"
names[36] = "Io"
names[49] = "Lycan"
names[57] = "Necrophos"
names[106] = "Windranger"

newInfo = pd.DataFrame(names, columns=['localized_name'])
newInfo['carry'] = carry
newInfo['disables'] = disables
newInfo['initiation'] = initiation
newInfo['nukers'] = nukers
newInfo['pushers'] = pushers
newInfo['support'] = support
newInfo['durable'] = durable

newTable = oldTable.join(newInfo.set_index('localized_name'), on='localized_name').drop('index', axis=1)
charList = ['carry', 'disables', 'initiation', 'nukers', 'pushers', 'support', 'durable']
arcWarden = [3, 2, 1, 2, 2, 0, 1]
underlord = [1, 2, 1, 0, 3, 1, 2]
for char in range(len(charList)):
    newTable.at[4, charList[char]] = arcWarden[char]
    newTable.at[98, charList[char]] = underlord[char]
    newTable[charList[char]] = newTable[charList[char]].apply(pd.to_numeric)

newTable.to_csv('hero_chars.csv', index=False)
    