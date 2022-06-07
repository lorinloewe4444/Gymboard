#

faecher =['Biologie', 'BG', 'Chemie', 'Chinastudien', 'Deutsch', 'Englisch', 'WR',
'Französisch', 'Geschichte', 'Geografie', 'Griechisch', 'Italienisch', 'Informatik',
'Latein', 'Mathematik', 'Musik', 'Physik', 'PAM', 'PPP', 'Russisch', 'Spanisch', 'Sport']

#Vorlagen
allGyms = ['Gym1', 'Gym2', 'Gym3', 'Gym4']
immers = ['Einsprachig', 'Immersion']
eF = ['EF']
sF = ['GF', 'SF']

#Parent = [Child elements] | First level
Biologie = immers + eF + sF
BG = sF + eF
Chemie = immers + sF
Chinastudien = []
Deutsch = allGyms
Englisch = ['EF', 'GF', 'SF']
WR = ['EF', 'EWR', 'SF']
Französisch = []
Geschichte = immers + eF
Geografie = ['Gym1', 'Gym2', 'Gym4'] + eF
Griechisch = []
Italienisch = sF + ['fakultativ']
Informatik = ['Gym1', 'Gym2', 'fakultativ(archiv)'] + eF
Latein = []
Mathematik = allGyms
Musik = ['fak'] + allGyms + eF
Physik = ['Gym2', 'Gym3', 'Gym4']
PAM = ['AM', 'Physik']
PPP = ['Philosophie', 'Psychologie', 'Pädagogik']
Russisch = []
Spanisch = []
Sport = eF

alleFaecher = []

for fach in faecher:
    exec("alleFaecher.append(%s)" % (fach))

#print(alleFaecher)
for i in faecher:
    print("<li>"+i+"</li>")
