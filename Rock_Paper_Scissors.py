# Start menu

import random

def menu():

    choice=''

    print('< < < WELCOME TO ROCK, PAPER, SCISSORS!! > > >'+'\n')
    print('[1] To Play with a CPU')
    print('[2] To Play with another Player')
    print('[0] EXIT'+'\n')

    choice=input('Please enter your choice ==> ')

    return int(choice)

# Play with

def play_cpu(): # With computer
    again=''

    print('< < < INSTRUCTIONS > > >'+'\n')
    print('Enter R/r for ROCK')
    print('Enter P/p for PAPER')
    print('Enter S/s for SCISSOR'+'\n')
    print('Enter 0 to go back'+'\n')


    while(again!='0'):
        plyopt=''
        cpuopt=''

        plyopt=input('What will be your hand ==> ')

        while(plyopt not in ['r','R','p','P','s','S','0']):
            print('Please Try again!'+'\n')
            plyopt=input('What will be your hand ==> ')

        if(plyopt=='0'):
            break

        rdm=random.randint(1,3)

        if(rdm==1):
            cpuopt='r'
        elif(rdm==2):
            cpuopt='p'
        else:
            cpuopt='s'

        if(plyopt in ['r','R'] and cpuopt=='p'):
            print('Computer Wins !!!'+'\n')
        elif(plyopt in ['p','P'] and cpuopt=='p'):
            print('Draw !!!'+'\n')
        elif(plyopt in ['s','S'] and cpuopt=='p'):
            print('Player Wins !!!'+'\n')

        elif(plyopt in ['r','R'] and cpuopt=='r'):
            print('Draw !!!'+'\n')
        elif(plyopt in ['p','P'] and cpuopt=='r'):
            print('Player Wins !!!'+'\n')
        elif(plyopt in ['s','S'] and cpuopt=='r'):
            print('Computer Wins !!!'+'\n')

        elif(plyopt in ['r','R'] and cpuopt=='s'):
            print('Player Wins !!!'+'\n')
        elif(plyopt in ['p','P'] and cpuopt=='s'):
            print('Computer Wins !!!'+'\n')
        elif(plyopt in ['s','S'] and cpuopt=='s'):
            print('Draw !!!'+'\n')

def play_player(): # with Human
    again=''

    print('< < < INSTRUCTIONS > > >'+'\n')
    print('Enter R/r for ROCK')
    print('Enter P/p for PAPER')
    print('Enter S/s for SCISSOR'+'\n')
    print('Enter 0 to go back'+'\n')
    print("WARNING: AS THIS IS A 2 PLAYER GAME, PLEASE DO NOT VIEW PLAYER 1's HAND !!!"+'\n')

    while(again!='0'):
        plyopt1=''
        plyopt2=''

        plyopt1=input('What will be your hand Player 1 ==> ')

        while(plyopt1 not in ['r','R','p','P','s','S','0']):
            print('Please Try again!'+'\n')
            plyopt1=input('What will be your hand Player 1 ==> ')

        if(plyopt1=='0'):
            break

        plyopt2=input('What will be your hand Player 2 ==> ')

        while(plyopt2 not in ['r','R','p','P','s','S','0']):
            print('Please Try again!'+'\n')
            plyopt2=input('What will be your hand Player 2 ==> ')

        if(plyopt2=='0'):
            break

        rdm=random.randint(1,3)

        if(rdm==1):
            plyopt2='r'
        elif(rdm==2):
            plyopt2='p'
        else:
            plyopt2='s'

        if(plyopt1 in ['r','R'] and plyopt2 in ['p','P']):
            print('Player 2 Wins !!!'+'\n')
        elif(plyopt1 in ['p','P'] and plyopt2 in ['p','P']):
            print('Draw !!!'+'\n')
        elif(plyopt1 in ['s','S'] and plyopt2 in ['p','P']):
            print('Player 1 Wins !!!'+'\n')

        elif(plyopt1 in ['r','R'] and plyopt2 in ['r','R']):
            print('Draw !!!'+'\n')
        elif(plyopt1 in ['p','P'] and plyopt2 in ['r','R']):
            print('Player 1 Wins !!!'+'\n')
        elif(plyopt1 in ['s','S'] and plyopt2 in ['r','R']):
            print('Player 2 Wins !!!'+'\n')

        elif(plyopt1 in ['r','R'] and plyopt2 in ['s','S']):
            print('Player 1 Wins !!!'+'\n')
        elif(plyopt1 in ['p','P'] and plyopt2 in ['s','S']):
            print('Player 2 Wins !!!'+'\n')
        elif(plyopt1 in ['s','S'] and plyopt2 in ['s','S']):
            print('Draw !!!'+'\n')

# initialize

opt=1

# main

while(opt!=0):

    # menu loop

    opt=menu()
    print()

    while(opt not in [1,2,0]):
            print('That is not a valid option. Please try again!'+'\n')
            opt=menu()
            print()

    # conditions

    if(opt==1):
        play_cpu()
        print()
    elif(opt==2):
        play_player()
        print()
    else:
        print('Thank you very much for playing :D')
