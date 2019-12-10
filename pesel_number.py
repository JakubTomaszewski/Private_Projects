'''a programe which converts a pesel number (identification number) to the exact date of birth'''

#program który czyta pesel i pokazuje date urodzenia na jego podstawie

class IncorrectLengthException(Exception): #raises an exception when the length is not 11
    def __init__(self):
        super().__init__("Numer PESEL musi mieć 11 znaków")


print("Podaj swoj PESEL: ", end='')
try:
    pesel=input()
    if len(str(pesel)) != 11:
        print("Zła dł")
        raise IncorrectLengthException
    pesel = str(pesel).zfill(11)

except ValueError:
    print("W numerze PESEL mogą występować jedynie cyfry!")
    exit(0)


print("Twoja data urodzenia to")

if pesel[2]=="2" or pesel[2]=="3":
    rok=int(pesel[0:2]) + 2000
    miesiac=int(pesel[2:4])-20
    miesiac=str(miesiac).zfill(2)
    dzien=int(pesel[4:6])
    print("{}.{}.{}".format(dzien,miesiac,rok))

else:
    rok = int(pesel[0:2]) + 1900
    miesiac=int(pesel[2:4])
    miesiac=str(miesiac).zfill(2)
    dzien = int(pesel[4:6])
    print("{}.{}.{}".format(dzien,miesiac,rok))
