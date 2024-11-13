# Define the sets
A = {'a', 'b', 'c', 'd'}
X = {'!', '+', '-'}

# Enter the value of n
n = int(input("Enter the value of n: "))

# Function to check if a word is valid according to the rules
def is_valid_word(word):
    # Rule 1: Must start with a letter from A
    if word[0] not in A:
        return False
    # Rule 2: Must end with a letter from A
    if word[-1] not in A:
        return False
    # Rule 3: Cannot contain two adjacent letters from set X
    for i in range(1, len(word)):
        if word[i] in X and word[i - 1] in X:
            return False
    return True

# Function to generate all possible words of length n
def generate_words(length, current_word=""):
    if len(current_word) == length:
        return [current_word] if is_valid_word(current_word) else []
    else:
        valid_words = []
        for letter in A.union(X):
            valid_words += generate_words(length, current_word + letter)
        return valid_words

# Compute a_n by generating and counting valid words of length n
valid_words = generate_words(n)
a_n = len(valid_words)

print(f"The number of valid words of length {n} (a_{n}) is: {a_n}")
