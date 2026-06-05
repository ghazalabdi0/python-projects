#global variables and imports
from abc import ABC, abstractmethod   #for class and inheriting
import string
import random


#create password generator abstract class
class PasswordGeneratortAbstract(ABC):
    @abstractmethod
    def generate_password(self, length=8):
        pass

#create numeric password generator
class NumericPasswprdGenerator(PasswordGeneratortAbstract):
    letters = string.digits
    def generate_password(self, length=8):
        # result=""
        # for _ in range(length):
        #     result += str(random.choice(self.letters))
        # return result
       return "".join(str(random.choice(self.letters)) for _ in range(length))

#create letters password generator
class LettersPasswordGenerator(PasswordGeneratortAbstract):
    letters=string.ascii_letters
    def generate_password(self, length=8):
        # result=""
        # for _ in range(length):
        #     result += str(random.choice(self.letters))
        # return result
       return "".join(str(random.choice(self.letters)) for _ in range(length))

#create mixed password generator
class MixedPasswordGenerator(PasswordGeneratortAbstract):
    letters=string.ascii_letters + string.digits
    def generate_password(self, length=8):
        # result=""
        # for _ in range(length):
        #     result += str(random.choice(self.letters))
        # return result
        return "".join(str(random.choice(self.letters)) for _ in range(length))
    
#run the app
generator1 = NumericPasswprdGenerator()
print(generator1.generate_password(15))

generator1 = LettersPasswordGenerator()
print(generator1.generate_password())

generator1 = MixedPasswordGenerator()
print(generator1.generate_password())