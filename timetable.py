def subjects (a,b,c,d,e,f,g,h,p,q,r,s,t,u):
    sub={"A":a,"B":b,"C":c,"D":d,"E":e,"F":f,"G":g,"H":h,"G@":g,"A+":a,"H+":h,"G+":g,"E+":e,"F+":f,"C+":c,"B+":b,"E@":e,"P":p,"Q":q,"R":r,"S":s,"T":t,"U":u}
    return sub

def OriginalTime():
    table=[["A","F","D","B","G","P","P","P","P"],["B","G","E","C","Aa","Q","Q","Q","Q"],["C","A","F","D","H","R","R","R","R"],["D","B","G","E","----","S","S","S","S"],["E","C","A","F","Hp","T","T","T"]]
    return table

def daywise(day):
    #sub=subjects('a','b','c','d','e','f','g','h','p','q','r','s','t','u')
    table=OriginalTime()
    for i in range(8):
        print (table[day][i])

def main():
    print("Enter the day option:'\n'1. Monday'\n'2. Tuesday'\n'3. Wednesday'\n'4. Thursday'\n'5. Friday")
    day=int(input())
    daywise(day)

if __name__=="__main__":
    main()