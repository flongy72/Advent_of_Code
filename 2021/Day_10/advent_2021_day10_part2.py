def main():
    with open("advent_2021_day10.txt") as input:
        data = input.read()
        openers = ["{", "(", "[", "<"]
        closers = ["}", ")", "]", ">"]
        completes = []
        scores = {")": 1, "]": 2, "}": 3, ">": 4}
        for string in data.splitlines():
            opening = []
            illegal = False
            for char in string:
                if char in openers:
                    opening.append(char)
                if char in closers:
                    index = closers.index(char)
                    if opening[-1] == openers[index]:
                        opening.pop()
                        continue
                    else:
                        illegal = True
                        break
            if not illegal:
                score = 0
                while opening:
                    opener = opening.pop()
                    closer = closers[openers.index(opener)]
                    score = (score*5) + scores[closer]
                completes.append(score)
        completes.sort()
        print(completes[len(completes)//2])


if __name__ == "__main__":
    main()