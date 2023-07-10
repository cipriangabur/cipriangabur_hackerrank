def minion_game(string):
    str_len = len(string)
    vowel = 0
    consonant = 0

    for i in range(str_len):
        if string[i] in 'AEIOU':
            vowel += (str_len - i)
        else:
            consonant += (str_len - i)

    winner, score = ("Stuart", consonant) if vowel < consonant else \
        ("Kevin", vowel) if vowel > consonant else ("Draw", " ")
    print(f"{winner} {score}" if score != " " else f"{winner}")


if __name__ == '__main__':
    s = input()
    minion_game(s)