def reverser(word):
    word = word.split(' ')
    res = " ".join(word[::-1])
    print(res)

test_cases1='Nine Eight Seven Six Five Four Three Two One'
test_cases2='The cat in the hat sat on the mat'
test_cases3='efficiency check to sentences long very of reversal the testing'
reverser(test_cases1)
reverser(test_cases2)
reverser(test_cases3)