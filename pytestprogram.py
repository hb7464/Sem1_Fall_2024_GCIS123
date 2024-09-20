def check_guess(guess,answer):
    if guess == answer:
        return 0
    elif guess > answer:
        print('too high by',guess-answer)
        return None
    elif guess < answer:
        print('too low by',answer-guess)
        return None
 #   else:
  #      print(abs(guess-answer))
def test_guess_too_high():
    assert check_guess(2000,5) == 0

def test_check_guess_correct():
    assert check_guess(5,5) == 0

def test_guess_too_low():
    assert check_guess(-23020439043094,5) == 0