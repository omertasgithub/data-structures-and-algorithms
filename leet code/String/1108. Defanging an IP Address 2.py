#1108. Defanging an IP Address

#Related topics
#string

x = '1.1.1.1'

#first solurion
def defangIPaddr(address):
    lst = list(address)
    
    for i, n in enumerate(lst):
        if n=='.':
            lst[i] = "[.]"
    return "".join(lst)

#second solution
def defangIPaddr2(address):
    return address.replace('.','[.]')

#thirdsolution
def defangIPaddr3(address):
    return '[.]'.join(address.split('.'))

import re
#4th solution
def defangIPaddr4(address):
    return re.sub('\.', '[.]', address)


#5th solution
def defangIPaddr5(address):
    return ''.join('[.]' if c=='.' else c for c in address)


print(defangIPaddr(x))
print(defangIPaddr2(x))
print(defangIPaddr3(x))
print(defangIPaddr4(x))
print(defangIPaddr5(x))