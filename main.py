#Use ', ' to separate

with open('QuestionsToRedoTests.txt', 'r') as file:
    info = []
    length = len(file.readlines())
    file.seek(0)
    for _ in range(length):
        line = file.readline()
        info.append(line.strip().split(', '))
    for i in info:
        print(f'{i[1]}: {i[5]}')
        