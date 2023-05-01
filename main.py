grammar = [
    'S -> aA|dE',
    'A -> aB|aS',
    'B -> bC',
    'C -> bD|bB',
    'D -> cD|λ',
    'E -> λ'
]

def get_number_of_lower(word):
    counter = 0
    for symbol in word:
        if symbol.islower():
            counter += 1
    return counter

def generate_successors(grammar, word):

    successors = ['']
    for symbol in word:
        if symbol.isupper():
            newList = []
            for successor in successors:
                for word in grammar[symbol]:
                    newList.append(successor + word)
            successors = newList
        else:
            for i in range(len(successors)):
                successors[i] += symbol
    return successors


def generate_words(grammar, length, startState):
    newGrammar = {}
    for line in grammar:
        aux = line.split("->")
        state = aux[0].strip()
        values = [x.strip() if x.strip() != "λ" else "" for x in aux[1].split("|")]
        newGrammar[state] = values

    words = newGrammar[startState].copy()
    while len(words) > 0:
        currentWord = words.pop(0)
        if not currentWord.islower() and get_number_of_lower(currentWord) <= length:
            words.extend(generate_successors(newGrammar, currentWord))
        elif len(currentWord) == length:
            print(currentWord)




if __name__ == "__main__":
    generate_words(grammar, 8, "S")
