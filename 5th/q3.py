class student: # class
    def __init__(self, firstName, lastName, gender, fakulta, degree, year, specialist, telephone, mazavRefuei): # define attributes
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.fakulta = fakulta
        self.degree = degree
        self.year = year
        self.specialist = specialist
        self.telephone = telephone
        self.mazavRefuei = mazavRefuei

    def set_student(self, firstName, lastName, gender, fakulta, degree, year, specialist, telephone, mazavRefuei): # set attributes
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.fakulta = fakulta
        self.degree = degree
        self.year = year
        self.specialist = specialist
        self.telephone = telephone
        self.mazavRefuei = mazavRefuei

    def get_student(self, firstName, lastName, gender, fakulta, degree, year, specialist, telephone, mazavRefuei): # get attributes
        return self.firstName
        return self.lastName
        return self.gender
        return self.fakulta
        return self.degree
        return self.year
        return self.specialist
        return self.telephone
        return self.mazavRefuei


class massage:# class
    def __init__(self, type, date, massageTherapist, charge):  # define attributes
        self.type = type
        self.date = date
        self.massageTherapist = massageTherapist
        self.charge = charge

    def set_massage(self, type, date, massageTherapist, charge):  #  set attributes
        self.type = type
        self.date = date
        self.massageTherapist = massageTherapist
        self.charge = charge

    def get_massage(self, type, date, massageTherapist, charge):  # get attributes
        return self.type
        return self.date
        return  self.massageTherapist
        return self.charge


student1 = student('Yarden', 'Rimon' , 'feamle', 'economic' ,'information system','nothing', '2', '0505953344', 'good') # create student 1 from student type
massage1 = massage('Foot Massage', 'Today’s date', 'Dr. No', 180) # create massage 1 from massage type
massage2 = massage('Back Massage', 'Today’s date', 'Dr. J', 220) # create massage 2 from massage type
massage3 = massage('Neck Massage', 'Today’s date', 'Dr. Jekyll', 250) # create massage 3 from massage type

print(vars(student1)) #print
print('first massage:')
print(vars(massage1))
print('second massage:')
print(vars(massage2))
print('third massage:')
print(vars(massage3))
print('total amount of three massages-')
print(massage1.charge + massage2.charge + massage3.charge)