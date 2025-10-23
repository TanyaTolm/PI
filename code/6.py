with open ('text.txt', 'a+') as f:
    f.write('\n Hello world')

with open ('text.txt', 'r') as f:
    result = f.readlines()
    print(result)