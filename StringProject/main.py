#String in Python program

#string with single quotes
import string


def print_string():
    string = 'Welcome to the India '
    print(string)

    #Quotes apply multiple line
    string1 = '''Data
              Market
              Stock'''
    print(string1)

    #print only first and last character
    String2 = 'IloveIndia'
    print(String2[2])
    print(String2[-2])

#string slicing program
def slice_string():
    string3 = 'IloveIndia'
    print(string3[3:10])
    print(string3[2:8])

#deleting and updating string program
def del_update_string():
    string4 = 'IloveIndia'
    #string4 = 'countryy'
    print(string4)

#Escape sequencing in python using string
def escape_sequecing_string():
    string1 = 'I\'m a India'
    string1 = "I'm a \"India \""
    string1 = "C:\\python\\theory"
    print(string1)

#Formating in String
def formating_string():
    string2 ="{} {} {}".format('State', 'Country', 'District')
    string2 = "{1} {0} {0}".format('State', 'Country', 'District')   #position formate
    string2 = "{f} {i} {g}".format(g='State', f='Country', i='District')     #keyword Formate
    print(string2)

#Formatting in integer,Float using string
def integer_float_string():
    string2 = "{0:b}".format(20)
    string2 = "{0:e}".format(12.23)
    print(string2)

def all_method_string():
    str = 'Welcome to the India '
    a = str.capitalize()
    print(a)
    b = str.casefold()
    print(b)
    c = str.center(1)
    print(c)
    d = str.count('i')
    print(d)
    e = str.encode()
    print(e)
    f = str.endswith('a')
    print(f)
    g = str.expandtabs(2)
    print(g)
    h = str.find('to')
    print(h)
    i = str.format_map('the')
    print(i)
    j = str.index('to')
    print(j)
    k = str.isalnum()
    print(k)
    l = str.isalpha()
    print(l)
    m = str.isascii()
    print(m)
    n = str.isdecimal()
    print(n)
    o = str.isdigit()
    print(o)
    p = str.join('Welcome')
    print(p)

if __name__ == "__main__":
    print_string()
    slice_string()
    escape_sequecing_string()
    formating_string()
    integer_float_string()
    all_method_string()
