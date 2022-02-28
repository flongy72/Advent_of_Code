import numpy as np

def main():
    with open("advent_2021_day13.txt") as input:
        paper = np.zeros([1400, 1400], dtype=int)
        new = input.read()
        data = new.split("\n\n")
        co_ords = data[0].splitlines()
        folds = data[1].splitlines()
        for line in co_ords:
            x_ord, y_ord = line.split(",")
            paper[y_ord][x_ord] = 1
        for line in folds:
            fold = line.split()[2]
            j = fold.split("=")
            axis = j[0]
            num = int(j[1])
            if axis == "y":
                for x in range(num + 1, len(paper)):
                    for y in range(len(paper[x])):
                        if paper[x][y] == 1:
                            paper[x-((x-num)*2)][y] = 1
                            paper[x][y] = 0
            if axis == "x":
                for x in range(len(paper)):
                    for y in range(num + 1, len(paper[x])):
                        if paper[x][y] == 1:
                            paper[x][y-((y-num)*2)] = 1
                            paper[x][y] = 0
        for line in range(6):
            print(paper[line][:41])


if __name__ == "__main__":
    main()
