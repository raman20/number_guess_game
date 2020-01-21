from random import randint
    from time import sleep
    c = randint(1,100)
    chance = 5
    while input('press any key to play: ')
        while chance!=0:
            print('loading',end='')
            i=5
            while i!=0:
                sleep(0.3)
                print('.',end=' ')
                i-=1
            u = int(input('enter ur number'))
            if u == c:
                print('u win')
            elif u>c:
                print(f'less than {u}')
            elif u<c:\n",
                print(f'more than {u}')
            else:
                print('wrong choice')
            chance-=1
            print(f'chance left: {chance}')
            print()
        else:
            print(f'computer wins correct ans is {c}')
    else:
        print('\nthanks for playing')
