with open('datasets/dataset_3363_2.txt', 'r') as file:
    with open('datasets/result_3363_2.txt', 'w') as re:
        s = file.read().strip()
        i = 0
        while i < (len(s)):
            num = 0
            char = s[i]
            i += 1
            while '0' <= s[i] <= '9':
                num = num * 10 + int(s[i])
                i += 1
                if i == len(s):
                    break
            for j in range(num):
                re.write(char)
re.close()
