#Use ', ' to separate
import matplotlib.pyplot as pllt

with open('QuestionsToRedoTests.txt', 'r') as file:
    info = []
    length = len(file.readlines())
    file.seek(0)
    for _ in range(length):
        line = file.readline()
        info.append(line.strip().split(', '))
    for i in info:
        print(f'{i[1]}: {i[5]}')
    
    #pllt.barh(
        #[info[i][1] for i in range(1,length)][::-1],
        #[int(info[i][4]) for i in range(1,length)][::-1],
        #color="orange",
        #)
#pllt.xticks([i for i in range(101) if i % 5 == 0])
#pllt.colorbar(["purple" for i in range(1,length) if int(info[i][4]) == 100])
#pllt.show(False)

            