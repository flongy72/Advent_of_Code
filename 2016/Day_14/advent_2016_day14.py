import hashlib


def main():
    hashes = {}
    i=0
    keys = []
    while len(keys) < 64:
        if i not in hashes:
            user = ("ahsbgdzn" + str(i))
            h = hashlib.md5(user.encode())
            h2 = h.hexdigest()
            hashes[i] = h2
        else:
            h2 = hashes[i]
        for x in range(len(h2)-2):
            if h2[x] == h2[x+1] == h2[x+2]:
                # print(i)
                # print(h2)
                char = h2[x]*5
                for j in range(1, 1001):
                    k = i + j
                    if k not in hashes:
                        user = ("ahsbgdzn" + str(k))
                        h = hashlib.md5(user.encode())
                        h2 = h.hexdigest()
                        hashes[k] = h2
                    else:
                        h2 = hashes[k]
                    if char in h2:
                        # print("True")
                        # print(i)
                        # print(h2)
                        keys.append(i)
                        break
                break
        i += 1
    def stretch_hash(index, string, multiple):
        if multiple == 0:
            hashes[k] = h2
            return string
        if multiple == 2017:
            string = string + str(index)
        h = hashlib.md5(user.encode())
        h2 = h.hexdigest()


    print(keys[63])

if __name__ == '__main__':
    main()