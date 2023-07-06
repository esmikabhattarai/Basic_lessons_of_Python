#DICTONARY
a = { 
     'ASTRAL PROJECTION' : 'Out of body expreience',
     'Esmika' : 'Pythom programmer'
}
print(a['ASTRAL PROJECTION'])
print(a['Esmika'])

b = { 
    'USELESS' : 'NOT OF ANY USE',
    'DESTINY' : 'DISTINCT POINT'
}
print(b['USELESS'])
print(b['DESTINY'])
updatebat = {
     'FUTURE' : 'EVENT THAT WILL HAPPEN',
     'OK' : 'okay/fine'
}
b.update(updatebat)
print(b)
c = {
  'JUSTIN BIEBER' : 'CANADIAN AUTHOR',
  'SELENA GOMEZ' : 'MOST FOLLOWED CELEBRITY IN INNSTAGRAM'
}
print(c['JUSTIN BIEBER'])
print(c['SELENA GOMEZ'])
updatece = {
    'HALEY BIBER' : 'WIFE'
}
c.update(updatece)
print(c)
d = {
    'SIGNIFICANT' : 'LOVED ONES',
    'VALUABLE' : 'IMPORTANT',
    'NUMBER' : [1,2,3,4,]
}
print(d['SIGNIFICANT'])
print(d['VALUABLE'])
print(d['NUMBER'])
print(d.keys()) #PRINT KEYS
print(d.values()) #PRINT VALUES
print(list(d.keys())) #PRINTS ONLY KEY 
print(d.items()) #PRINNT THE ITMS[BY SHOWING both; KEYS + VALUES]
#UPDATE 
updatedic = { #UPDATE THE DICTONARY BY ADDING KEYS-VALUES
    'LOVE' : 'BLIND'
}
d.update(updatedic)
print(d)
print(d.get('ESMI'))
z = {
    'RAMESH' : 'NAME',
    'ESMIKA' : ' LUXURY'
}
print(z)
updatez1 = {
    'MAYA' : 'LOVE'
}
z.update(updatez1)
print(z)
p = {
    'OCTOBER' : 'FUN'
}
print(p)
p1 = {
    'ESMI' : 'WILD'
}
p.update(p1)
print(p)
print(p.get('OCTOBER'))
print(p['OCTOBER'])
#DIFFERENCE BETWEEN .get and []syntax in dictionary
print(p1.get('ESMI1')) #RETURN NONE AS ESMI1 IS NOT PRSENT IN DIC
#print(p1['ESMI1']) #SHOWS AN ERROR AS ESMI1 IS NOT PRSENT IN DIC
#SET
a = {1,2,3,4,5,1}
print(type(a))
print(a)
#FOR EMPTY SET
s = {} #SHOWS DICTIONARY INSTEAD OF SET
print(type(s))
a = set()
print(type(a))
b = set()
print(type(b))
b.add(6) #ADDING VALUES TO AN EMPTY SETS
b.add(9)
b.add(6)
b.add(7)
b.add(3)
b.add((1,2,3,4,5,7))
print(b)
c.add(8)

                                                                                                                                                                                         