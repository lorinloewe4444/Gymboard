#

faecher =['Biologie', 'BG', 'Chemie', 'Chinastudien', 'Deutsch', 'Englisch', 'WR',
'Französisch', 'Geschichte', 'Geografie', 'Griechisch', 'Italienisch', 'Informatik',
'Latein', 'Mathematik', 'Musik', 'Physik', 'PAM', 'PPP', 'Russisch', 'Spanisch', 'Sport',
'Theater']

#Vorlagen
allGyms = ['Gym1', 'Gym2', 'Gym3', 'Gym4']
immers = ['GF', 'Immersion']
eF = ['EF']
sF = ['SF']

#Parent = [Child elements] | First level
Biologie = immers + eF + sF
BG = ['GF', 'SF']
Chemie = immers + sF
Chinastudien = []
Deutsch = allGyms
Englisch = ['EF', 'GF']
WR = ['EF', 'EWR', 'SF']
