from math import nan
import random


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&*/\?"

Full_string = lower_case + upper_case + numbers + symbols
print("Lenght of the password:(default:8)")
lenght_pass_raw = input()
if lenght_pass_raw == "":
    lenght_pass = 8
else:
    lenght_pass = int(lenght_pass_raw)
    


password = "".join(random.sample(Full_string, lenght_pass))

print(password)
print("press enter to exit")
pause = input()
