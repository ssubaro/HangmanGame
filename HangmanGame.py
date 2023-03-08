class HangmanGame:

    secret_words = {
        'easy': 'cat',
        'intermediate': 'carnival',
        'advance': 'cronometer',
    }

    def __init__(self):
        self.word = None
        self.guesses = set()
        self.game_is_on = True
        self.word_status = None

    def play(self):
        print("======== Welcome Player to the HANGMAN-GAME ========")
        print("Select level difficulty:")
        print(*self.secret_words.keys(), sep=' - ')
        print("Press 0 to end/leave the game")
        level = input()
        while True:
            if level == '0':
                game.game_is_on = False
                break
            elif level in self.secret_words:
                break
            else:
                print('You most enter a valid level')
                level = input()
        self.word = self.secret_words[level]
        self.word_status = '_' * len(self.word)
        while self.game_is_on:
            self.guess()
        replay = input('¿Play again? (y/n): ')
        if replay == 'y':
            self.reset()
            self.play()
        elif replay == 'n':
            print('Thank your for playing the HANGMAN-GAME')

    def guess(self):
        print('Try a letter')
        letter = input()
        if letter == '0':
            self.game_is_on = False
        elif letter.isalpha() and len(letter) == 1:
            self.guesses.add(letter)
            self.update_word_status()
        else:
            print('You most enter only a letter')

    def update_word_status(self):
        current_word_status = ''
        for character in self.word:
            if character in self.guesses:
                current_word_status += character
            else:
                current_word_status += '_'
        self.word_status = current_word_status
        if self.word_status == self.word:
            print('¡Congrats, you WIN!')
            self.game_is_on = False
            print(f"The word was: {self.word}")
        else:
            print(self.word_status)

    def reset(self):
        self.word = None
        self.guesses = set()
        self.game_is_on = True
        self.word_status = None


if __name__ == '__main__':
    game = HangmanGame()
    game.play()