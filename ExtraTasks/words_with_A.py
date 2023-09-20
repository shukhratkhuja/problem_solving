words_string = input()

words_list = words_string.split(' ')
print(words_list)

counter = 0
for name in words_list:
    if 'A' in name:
        print(name)
        counter += 1
        continue

print("Kamida 1 ta A harfi ishtirok etgan so'zlar soni: ", counter)