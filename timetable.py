def subjects (a,b,c,d,e,f,g,h,p,q,r,s,t):
    sub={"A":a,"B":b,"C":c,"D":d,"E":e,"F":f,"G":g,"H":h,"P":p,"Q":q,"R":r,"S":s,"T":t,"----":'----'}
    return sub

def OriginalTime():
    table=[["A","F","D","B","G","P","P","P","P","H"],["B","G","E","C","A","Q","Q","Q","Q","H"],["C","A","F","D","H","R","R","R","R","E"],["D","B","G","E","----","S","S","S","S","G"],["E","C","A","F","H","T","T","T","D"]]
    return table

def daywise(day,sub):
    #sub=subjects('a','b','c','d','e','f','g','h','p','q','r','s','t','u')
    table=OriginalTime()
    timing=["8am","9am","10:15am","11:15am","1pm","2pm","3pm","4pm","5pm"]
    for i in range(9):
        # if table[day][i] == None or table[day][i]=='----':
        #     print (timing[i],": ----")
        # else:
        #     if "@" in table[day][i]:
        #         print (timing[i],": -@- ",sub[table[day][i]])
        #     else:
        #         if "+" in table[day][i]:
        #             print (timing[i],": -+- ",sub[table[day][i]])
        #         else:
        print (timing[i],":",sub[table[day][i]])


print ("Typee ur subjects. For empty codes type '----' ")
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
sub=subjects(a,b,c,d,e,f,g,h,p,q,r,s,t)
print("Enter the day option:'\n'1. Monday'\n'2. Tuesday'\n'3. Wednesday'\n'4. Thursday'\n'5. Friday")
day=int(input())
daywise(day+1,sub)