class Band:
    instances = []

    def __init__(self, name, members=None, list=None):
        self.name = name
        self.members = members
        self.list = list
        Band.instances.append(self.list)
         
    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        return [player.play_solo() for player in self.members]
        # solos = []
        # for player in self.members:
        #     solos.append(player.play_solos)
        # return solos  
              

       
class Musician:
    def __init__(self, name, instrument=None, solos=None):
        self.name = name
        self.instrument = instrument
        self.solos = solos

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solos    

class Guitarist(Musician):
    solos = 'face melting guitar solo'
    def __init__(self, name):
        self.instrument = 'guitar'
        self.name = name
        

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
        
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_solo(self):
        return self.solos    


class Bassist(Musician):
    solos = 'bom bom buh bom'
    def __init__(self, name):
        self.instrument = 'bass'
        self.name = name


    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}" 

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}" 

    def get_solo(self):
        return self.solos 

class Drummer(Musician):
    solos = 'rattle boom crash'
    def __init__(self, name):
        self.instrument = 'drums'
        self.name = name


    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"        

    def get_solo(self):
        return self.solos










   # pass
if __name__ == "__main__":
    musitioan = Musician('banana','potato')
    print(musitioan)
    guitarist = Guitarist('jon')
    print(guitarist)
    print(repr(guitarist))


 # about Guitarist    
    # def __str__(self):
    #     return f"My name is {self.name} and I play {self.instrument}"
        
    # def __repr__(self):
    #     return f"{self.__class__.__name__} instance. Name = {self.name}"

    # def get_instrument(self):
    #     return self.instrument

       

    # about Bassist
    # def __str__(self):
    #     return f"My name is {self.name} and I play {self.instrument}" 

    # def __repr__(self):
    #     return f"{self.__class__.__name__} instance. Name = {self.name}" 

    # def get_instrument(self):
    #     return self.instrument

    # about Drummer
    # def __str__(self):
    #     return f"My name is {self.name} and I play {self.instrument}"

    # def __repr__(self):
    #     return f"{self.__class__.__name__} instance. Name = {self.name}"

    # def get_instrument(self):
    #     return self.instrument    



     


# class Drummer:
#     def __init__(self, name):
#         self.name = name
#         self.instrument = 'drums'

#     def __str__(self):
#         return f"My name is {self.name} and I play drums"

#     def __repr__(self):
#         return f"Drummer instance. Name = {self.name}"

#     def get_instrument(self):
#         return self.instrument

# bassist
    # def __init__(self, name):
    #     self.name = name
    #     self.instrument = 'bass'

    # def __str__(self):
    #     return f"My name is {self.name} and I play bass" 

    # def __repr__(self):
    #     return f"Bassist instance. Name = {self.name}" 

    # def get_instrument(self):
    #     return self.instrument
