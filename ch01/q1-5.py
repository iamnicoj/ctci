def palindrome_permutation(string):
    bitvector = [0 for _ in range(127)]
    count_odds = 0

    for char in string:
        char_value = ord(char.lower())
        if char_value >= 97 and char_value <= 122:
            bitvector[char_value] += 1
            if bitvector[char_value] % 2 == 1:
                count_odds += 1
            else:
                count_odds -= 1
    
    return count_odds <= 1


def example():
    print(palindrome_permutation('test'))  # False
    print(palindrome_permutation('Test ES'))  # False
    print(palindrome_permutation('Tact Coa'))  # True ('taco cat', 'acto cta', etc )
    print(palindrome_permutation('cosa nostra ctr'))  # true ('cos atrnr tasoc')


if __name__ == "__main__":
    example()