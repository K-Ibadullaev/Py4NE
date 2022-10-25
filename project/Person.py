"""
Creates class Person with following properties:
first name, surname, birthday, email
"""


class Person:
    def __init__(self, fname, surname, birthday, email):
        if fname != None and surname != None and birthday!= None and email!= None:
            self.__fname = fname
            self.__surname = surname
            self.__birthday = birthday
            self.__email = email
        else:
            raise ValueError('Check input data!')

       
    @property
    def Fname(self):
        return self.__fname

    @Fname.setter
    def Fname(self, fname):
        if fname != None:
            self.__fname = fname

    @property
    def Surname(self):
        return self.__surname

    @Surname.setter
    def Surname(self, surname):
        if surname != None:
            self.__fname = surname


    @property
    def Birthday(self):
        return self.__birthday

    @Birthday.setter
    def Birthday(self, birthday):
        if birthday != None:
            self.__birthday = birthday 


    @property
    def Email(self):
        return self.__email

    @Email.setter
    def Email(self, email):
        if email != None:
            self.__email = email


    def __str__(self):
        #rep ={
        #    'First name' :   self.__fname,
        #    'Surname' : self.__surname,  
        #    'Birthday': self.__birthday,
        #    'Email' : self.__email
        #    }
        


        #rep = 'Person Object with id' + str(id(self)) +' \n'
        rep = 'First name : %s ' % self.__fname  +' \n'
        rep += 'Surname : %s ' % self.__surname  +' \n'
        rep += 'Birthday : %s ' % self.__birthday  +'\n'
        rep += 'Email : %s ' % self.__email
        return rep        











   