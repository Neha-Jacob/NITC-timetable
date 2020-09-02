def subjects (a,b,c,d,e,f,g,h,p,q,r,s,t,u):
    sub={"A":a,"B":b,"C":c,"D":d,"E":e,"F":f,"G":g,"H":h,"G@":g,"A+":a,"H+":h,"G+":g,"E+":e,"F+":f,"C+":c,"B+":b,"E@":e,"P":p,"Q":q,"R":r,"S":s,"T":t,"U":u}
    return sub

def OriginalTime():
    table=[["A","F","D","B","G","P/E+","P","P","H"],["B","G","E","C","A@","Q/F+","Q","Q","H"],["C","A","F","D","H","R/G+","R","R","E@"],["D","B","G","E","----","S/C+","S","S","G@"],["E","C","A","F","H+","T/B+","T","T","D+"]]
    return table

def daywise(day,sub):
    #sub=subjects('a','b','c','d','e','f','g','h','p','q','r','s','t','u')
    table=OriginalTime()
    ind=0
    timing=["8am","9am","10:15am","11:15am","1pm","2pm","3pm","4pm","5pm"]
    for i in range(9):
        if table[day][i] == None or table[day][i]=='----':
            print (timing[i],": ----")
        else:
            if "@" in table[day][i]:
                ind=(table[day][i]).find('@')
                if ind==3:
                    x=(table[day][i])[0:1]
                    y=(table[day][i])[2:3]
                    if (sub[x]=='----' and sub[y]=='----'):
                        print(timing[i],": ----")
                    else:
                        if sub[x]=='----':
                            print (timing[i],": extra->",sub[y])
                        else:
                            if sub[y]=='----':
                                print(timing[i],": ",sub[x])
                            else:print (timing[i],": ",sub[x],", extra-> ",sub[y])
                else:
                    x=(table[day][i])[0:1]
                    if sub[x]=='----':
                            print(timing[i],": ----")
                    else:
                        print (timing[i],": extra-> ",sub[x])
            else:
                if "+" in table[day][i]:
                    ind=(table[day][i]).find('+')
                    if ind==3:
                        x=(table[day][i])[0:1]
                        y=(table[day][i])[2:3]
                        if (sub[x]=='----' and sub[y]=='----'):
                            print(timing[i],": ----")
                        else:
                            if sub[x]=='----':
                                print (timing[i],": extra->",sub[y])
                            else:
                                if sub[y]=='----':
                                    print(timing[i],": ",sub[x])
                                else:
                                    print (timing[i],": ",sub[x],", extra-> ",sub[y])
                    else:
                        x=(table[day][i])[0:1]
                        if sub[x]=='----':
                            print(timing[i],": ----")
                        else:
                            print (timing[i],": extra-> ",sub[x])
                else:
                    print (timing[i],": ",sub[table[day][i]])


def main():
    print ("Type ur subjects. For empty codes type '----' ")
    a=input("A. ")
    b=input("B. ")
    c=input("C. ")
    d=input("D. ")
    e=input("E. ")
    f=input("F. ")
    g=input("G. ")
    h=input("H. ")
    p=input("P. ")
    q=input("Q. ")
    r=input("R. ")
    s=input("S. ")
    t=input("T. ")
    u=input("U. ")
    sub=subjects(a,b,c,d,e,f,g,h,p,q,r,s,t,u)
    t="Yes"
    while(t=="Yes"):
        print("Enter the day option:'\n'1. Monday'\n'2. Tuesday'\n'3. Wednesday'\n'4. Thursday'\n'5. Friday")
        day=int(input())
        daywise(day-1,sub)
        t=str(input("Do you want to continue? Yes/No  "))
        if not(t=="Yes") and not(t=="No"):
            print("ERROR!!! Invalid Input. Terminated")

if __name__=="__main__":
    main()