id = '64127321'

with open('id.txt', 'w') as f:
    for i in range(1,17):
        data = f'{id}{str(i):>02}'
        # f.write(data + '\n')
        print(data)