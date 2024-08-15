#q4:
names = {} #create dic
names['H'] = 'Hydrogen'
names['He'] = 'Helium'
names['Li'] = 'Lithium'
names['Be'] = 'Beryllium'
names['B'] = 'Boron'

atoms = {} #create dic
atoms['H'] = '1'
atoms['He'] = '2'
atoms['Li'] = '3'
atoms['Be'] = '4'
atoms['B'] = '5'

mass = {} #create dic
mass['H'] = '1.0078'
mass['He'] = '4.0026'
mass['Li'] = '6.9410'
mass['Be'] = '9.0122'
mass['B'] = '10.811'

symbol = input("please write symbol") #ask the user choose symbol
value1 = names.get(symbol) #symbol name
value2 = atoms.get(symbol) #symbol atoms
value3 = mass.get(symbol) #symbol mass

print(symbol + ": " + value1 + ", " + value2 + ", " + value3) #print symbol information

