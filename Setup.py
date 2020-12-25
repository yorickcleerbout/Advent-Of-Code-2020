import os

for i in range(1, 26):
    if i < 10:
        day = "0" + str(i)
    else:
        day = i

    if not os.path.exists(f'Day_{day}'):
        os.mkdir(f'Day_{day}')
        f = open(f'Day_{day}/Day_{day}.py', 'w+')
        f.close()
        f = open(f'Day_{day}/README.md', 'w+')
        f.close()
