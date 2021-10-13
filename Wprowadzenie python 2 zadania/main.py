import math
import file_manager
import chucknorris.quips as q

def listy(a_list:list,b_list:list):
    out_list = [a_list[i] for i in range(0,len(a_list),2)]
    out_list.extend([b_list[j] for j in range(1,len(b_list),2)])
    return out_list

a_list = [0,1,2,3,4,5,6,7,8]
b_list = [0,1,2,3,4,5,6,7,8]

print(listy(a_list,b_list))

def jakasfunkcja(data_text:str):
    out_dict = dict()
    out_dict['length'] = len(data_text)
    out_dict['letters'] = list(set(data_text))
    out_dict['big_letters'] = data_text.upper()
    out_dict['small_letters'] = data_text.lower()
    return out_dict

print(jakasfunkcja('Dog'))

def jakasfunkcja2(text:str,letter):
    return text.replace(letter,'')

print(jakasfunkcja2('banan','n'))

def przeliczanie(temp:float,temperature_type:str):
    if temperature_type.lower() == 'kelvin':
        return temp + 273.15
    elif temperature_type.lower() == 'fahrenheit':
        return  temp*1.8 + 32
    elif temperature_type.lower() == 'rankine':
        return  (temp+273.15)*1.8
    else:
        return 'blad'

print(przeliczanie(23,'kelvin'))
print(przeliczanie(23,'kevin'))

class Calculator:
    def add(self,a,b):
        return a+b
    def difference(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
calc = Calculator()

print(calc.add(1,2))

class ScienceCalculator(Calculator):


    def power(self,a,b):
        return pow(a,b)

    def squareroot(self,a):
        return math.sqrt(a)

    def log(self,a,b):
        math.log(a,b)

scalc = ScienceCalculator()
print(scalc.squareroot(25))

def odTylu(text:str):
    return '{}'.format(text[::-1])

print(odTylu('ziemniak'))

a = file_manager.FileManager('test')
print(a.read_file())
a.update_file('test')
print(a.read_file())

print(q.random('Test'))