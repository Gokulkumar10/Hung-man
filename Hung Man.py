import random


def hung_man(a):

    if attempts == 0:
        print('You Loose\nYou let a kind man die')
        print('     O_|    ')
        print('    /|\     ')
        print('    / \ ')

    if a == 1:
        print('Last breaths counting.  Take care!')
        print('   \ O_|/    ')
        print('     |      ')
        print('    / \ ')

    if a == 2:
        print('   \ O /|    ')
        print('     |      ')
        print('    / \ ')

    if a == 3:
        print('   \ O /    ')
        print('     |      ')
        print('    / \ ')

    if a == 4:
        print('   \ O     ')
        print('     |     ')
        print('    / \ ')

    if a == 5:
        print('     O     ')
        print('     |     ')
        print('    / \ ')

    if a == 6:
        print('     O     ')
        print('     |     ')
        print('    /   ')

    if a == 7:
        print('     O     ')
        print('     |     ')

    if a == 8:
        print('     O     ')

    if a == 9:
        print('')


def placed_pos(letter, index, pos):
    p = ''
    for i in range(len(pos)):
        if i == index:
            pos[index] = letter
            break
    for j in pos:
        p += j
    print('{}\n{}'.format(p, len(pos) * '-'))
    return pos


def intro():
    name = input('Enter your name :')
    print(f'Welcome {name}')
    print('=' * 20)
    print('***** Try to guess the words from Car Brands Name ******')
    print('Try to guess it less than 10 attempts')


if __name__ == '__main__':
    random_words = ['toyato', 'hyndai', 'tata', 'benz', 'hero']
    random_word = random.choice(random_words)
    size = len(random_word)
    p = [' ' for x in range(size)]
    attempts = 10
    chances = 0
    normal_word = [random_word[x] for x in range(size)]
    intro()
    print('The word is {}'.format(random_word))
    while chances != size:
        guess_letter = input('Guess the word:\n')
        if guess_letter in normal_word:
            index = normal_word.index(guess_letter)
            p = placed_pos(guess_letter, index, p)
            chances += 1
            normal_word[index] = '-'

        else:
            attempts -= 1
            print('{} turns left.'.format(attempts))
            print('  {}'.format('-' * 9))
            hung_man(attempts)
            if attempts == 0:
                break
    if chances == size:
        print('your won')
    else:
        print("Don't worrry try again")