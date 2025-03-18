n = int(input())

def way_too_long_words(word):

    if len(word) > 10:
        return f"{word[0]}{len(word)-2}{word[-1]}"
    return word

for _ in range(n):
    word = input()
    print(way_too_long_words(word=word))