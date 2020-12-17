class Band:
    # new_list = []
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        # band.new_list.append(self.name)
         
    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

       
class Musician:
    def __init__(self, name, instrument=None, solo=None):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo    

class Guitarist(Musician):
    solo = 'face melting guitar solo'
    def __init__(self, name):
        self.instrument = 'guitar'
        self.name = name
        

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
        
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_solo(self):
        return self.solo    


class Bassist(Musician):
    solo = 'bom bom buh bom'
    def __init__(self, name):
        self.instrument = 'bass'
        self.name = name


    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}" 

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}" 

    def get_solo(self):
        return self.solo 

class Drummer(Musician):
    solo = 'rattle boom crash'
    def __init__(self, name):
        self.instrument = 'drums'
        self.name = name


    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"        

    def get_solo(self):
        return self.solo










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
