if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        s = input()

        if s[0] == 'insert':
            pos,value = int(s[1]), int(s[2])
            l.insert(pos,value)
        elif s[0] == 'remove':
            value = int(s[1])
            l.remove(value)
        elif s[0] == 'append':
            value = int(s[1])
            l.append(value)
        elif s[0] == 'sort':
            l.sort()
        elif s[0] == 'pop':
            l.pop()
        elif s[0] == 'reverse':
            l.reverse()
        elif s[0] == 'print':
            print(l)        


main()