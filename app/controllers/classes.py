class ElectionStats():
    # TODO estatísticas de candidatos por gênero, cor, idade, partido, 
    # estado civil, profissão, grau de escolaridade, patrimonio e gastos
    # entre eleitos e nao eleitos.
    def __init__(self, candidates=[]) -> None:
        self.__candidates = candidates

class Person:
    def __init__(self, name="", age=0, gender="", color="") -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__color = color
    
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age
    
    def set_gender(self, gender):
        self.__gender = gender
    
    def set_color(self, color):
        self.__color = color
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_gender(self,):
        return self.__gender
    
    def get_color(self):
        return self.__color 


class Candidate(Person):
    def __init__(self, num_code=0, party="", number=0, marital_status="",
                 profession="", schooling="", state="", status="", spent=0,
                 patrimony=0, votes=0, reelected=False) -> None:
        self.__num_code = num_code
        self.__party = party
        self.__number = number
        self.__marital_status = marital_status
        self.__profession = profession
        self.__schooling = schooling
        self.__state = state
        self.__status = status
        self.__patrimony = patrimony
        self.__spent = spent
        self.__votes = votes 
        self.__reelected = reelected

    def set_num_code(self, num_code):
        self.__num_code = num_code
        
    def set_party(self, party):
        self.__party = party

    def set_number(self, number):
        self.__number = number

    def set_marital_status(self, marital_status):
        self.__marital_status = marital_status

    def set_profession(self, profession):
        self.__profession = profession

    def set_schooling(self, schooling):
        self.__schooling = schooling

    def set_state(self, state):
        self.__state = state
        
    def set_status(self, status):
        self.__status = status

    def set_patrimony(self, patrimony):
        self.__patrimony = patrimony

    def set_spent(self, spent):
        self.__spent = spent
        
    def set_votes(self, votes):
        self.__votes = votes

    def set_reelected(self, reelected):
        self.__reelected = reelected
        
    def get_num_code(self):
        return self.__num_code
    
    def get_party(self):
        return self.__party

    def get_number(self):
        return self.__number

    def get_marital_status(self):
        return self.__marital_status

    def get_profession(self):
        return self.__profession

    def get_schooling(self):
        return self.__schooling

    def get_state(self):
        return self.__state

    def get_status(self):
        return self.__status
    
    def get_patrimony(self):
        return self.__patrimony
    
    def get_spent(self):
        return self.__spent
    
    def get_votes(self):
        return self.__votes

    def get_reelected(self):
        return self.__reelected
        