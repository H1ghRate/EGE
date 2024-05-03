with open('9_probnik_yandex4.csv') as f:
    for nums in f:
        a = list(map(int, nums.split(';')))

        