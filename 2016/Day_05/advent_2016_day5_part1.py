
import hashlib

def main():
    i=0
    x=0
    password=""
    while x<8:
        i=str(i)
        user = ("wtnhxymk" + i)
        h = hashlib.md5(user.encode())
        h2 = h.hexdigest()


        if h2.startswith("00000"):
            print (i)
            password += h2[5]
            x += 1
            i = int(i)
            i += 1
            continue
        i=int(i)
        i += 1
    print (password)
if __name__ == '__main__':
    main()

