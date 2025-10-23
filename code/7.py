lines = ['one', 'two', 'three']

with open ('text.txt', 'w') as f:
    for line in lines:
        f.write('\n Cycle run ' + line)
    print('Done!')
