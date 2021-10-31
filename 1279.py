a = []
while(True):
    try:
        c = int(input())
        p =[]
        o = True
        if((c%4==0 and c%100!=0) or c%400==0):
            o = False
            p.append("This is leap year.")
            if(c%15==0):
                p.append("This is huluculu festival year.")
            if(c%55 == 0):
                p.append("This is bulukulu festival year.")
        elif(c%15==0):
            p.append("This is huluculu festival year.")
            o = False
        if(o == True):
            p.append("This is an ordinary year.")
        a.append(p)
    except EOFError:
        for i in range(len(a)):
            for k in range(len(a[i])):
                print(a[i][k])
            if(i!=len(a)-1):
                print()
            else:
                break
        break