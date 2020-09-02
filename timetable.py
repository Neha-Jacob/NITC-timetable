def subjects (a,b,c,d,e,f,g,h,p,q,r,s,t):
    sub={"A":a,"B":b,"C":c,"D":d,"E":e,"F":f,"G":g,"H":h,"P":p,"Q":q,"R":r,"S":s,"T":t}
    return sub

def OriginalTime(A,B,C,D,E,F,G,H,P,Q,R,S,T):
    table=[[A,F,D,B,G,E,P,P,H],[B,G,E,C,A,Q,Q,Q,H],[C,A,F,D,H,R,R,R,E],[D,B,G,E,"----",S,S,S,G],[E,C,A,F,H,T,T,T,D]]
    return table

def putting_subjects():
    a=input("Slot A:")
    b=input("Slot B:")
    c=input("Slot C:")
    d=input("Slot D:")
    e=input("Slot E:")
    f=input("Slot F:")
    g=input("Slot G:")
    h=input("Slot H:")
    p=input("Slot P:")
    q=input("Slot Q:")
    r=input("Slot R:")
    s=input("Slot S:")
    t=input("Slot T:")
    return a,b,c,d,e,f,g,h,p,q,r,s,t


def daywise(day):
    print("Enter your subjects for your required slots and type 'None' for others")
    a,b,c,d,e,f,g,h,p,q,r,s,t=putting_subjects()
    sub=subjects(a,b,c,d,e,f,g,h,p,q,r,s,t)
    table=OriginalTime(sub["A"],sub["B"],sub["C"],sub["D"],sub["E"],sub["F"],sub["G"],sub["H"],sub["P"],sub["Q"],sub["R"],sub["S"],sub["T"])
    list1=["8-9",   "9-10" ,  "10:15-11:15","11:15-12:15" ,  "1-2"  , "2-3" ,  "3-4"  , "4-5"  ,"5-6"]
    for i in range(9):
        print (list1[i],table[day-1][i])
def main():
    print("Enter the day option:'\n'1. Monday'\n'2. Tuesday'\n'3. Wednesday'\n'4. Thursday'\n'5. Friday")
    day=int(input())
    daywise(day)

if __name__=="__main__":
    main()