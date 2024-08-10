def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    count_true = 0
    for letter in "true":
        count_true += combined_names.count(letter)
    count_love = 0
    for letter in "love":
        count_love += combined_names.count(letter)
    print(int(str(count_true) + str(count_love)))