print('Hello welcome to Hangman!')
def secret(x):
    'Insert underscore instead of words'
    a = len(x)
    return '_'*a
def rep(List,target,index):
    'Replace in list!'
    if len(index) == 1:
        List.pop(index[0])
        List.insert(index[0] , target)
        return ''.join(List)
    else:
        for ind in index:
            List.pop(ind)
            List.insert(ind , target)
        return ''.join(List)
def found(Str , Target):
    'Next level finding!'
    index = 0
    indexes = []
    while Target in Str:
        index_1 = Str.index(Target)
        indexes.append((index_1+index))
        Str.pop(index_1)
        index += 1
    return indexes
while True:
    Answer = (input('Please pick a word : ')).lower()
    print('OK, player 2 please guess the word! you have 7 chances!')
    print(secret(Answer))
    Code = list(secret(Answer))
    Progress = secret(Answer)
    lose_count = 0
    Hangman = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    while Progress != Answer:
        Geuss = (input('Please guess a word : ')).lower()
        if len(Geuss) == 1:
            for G in Geuss:
                if G in Answer:
                    index = found(list(Answer),G)
                    Progress = rep(Code,Geuss,index)
                    print('Yep! ',Progress)
                    if Progress in Answer:
                        print('You won!')
                else:
                    print('Nope!' , Progress)
                    print(Hangman[lose_count])
                    lose_count +=1
                    if lose_count == 7:
                        print('You lost! and the answer was ',Answer)
                        Progress = Answer
                        break 
        else:
            print('Invalid input!')
    print('wanna try again? ')
    sec_choice = (input('y/n ')).lower()
    if sec_choice == 'y':
        pass
    else:
        exit()