#Q.1- Write a python code to find a valid email address from a text.
import re
str = input('Enter text ')
emails = re.finditer('[_\w\.]+@[gmail.com |yahoo.com]+', str) 
for m in emails:
    print('Match is at: {}, End: {}, Pattern found: {}'.format(m.start(), m.end(), m.group()))


#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
import re
n = input('Enter text ')
number = re.finditer('((\+91-))[789]{1}\d{9}', n) 
for m in number:
    print('Match is at: {}, End: {}, Pattern found: {}'.format(m.start(), m.end(), m.group()))
