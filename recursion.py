#Глава 3 Рекурсия

#Базовый и рекурсивный случай

#!!!!!!!! БЕСКОНЕЧНЫЙ ЦИКЛ !!!!!!!!!!!!!
'''
def countdownOne(i):
    print(i)
    countdownOne(i-1)
countdownOne(3)
'''
#!!!!!!!! БЕСКОНЕЧНЫЙ ЦИКЛ !!!!!!!!!!!!!

def countdown(i):
    print(i)
    if i <= 1: #Базовый случай
        return
    else:      #Рекурсивный случай
        countdown(i-1)
countdown(5)

