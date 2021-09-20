from random import randint 

print ("Введіть ваше число від 1 до 5")
print ("Спробуй вгадать число яке я загадав))) ")
guess = input(" > ")
cguess = (randint(1,5))

print ("Ваше число", guess)
print ("Моє число ", cguess)

if guess == cguess:
    print ("Вітаю,ви виграли...")
if guess != cguess:
    print ("Ти програв)")
