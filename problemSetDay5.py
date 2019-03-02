# File name: problemSetDay5.py
mysterynumber = 7
guess = int(input('What is your guess?'))
while guess == 7:
    guess = int(input('Great Job!'))
print ('Your Strength is 5!')
strength = 5
while strength <= 10:
    print (strength)
    strength += 1
print ('You are too strong, move on to the next level!')
n = int(input("What is n?"))
m = int(input("What is m?"))
print(n**m)

count = 1
value = 1
while count <= m:
    value = value*n
    count+=1
print(value)