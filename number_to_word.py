def numberToWords(num):
        l=0
        p=0
        z=0
        if num == 0:
            print("Zero")
            return
        if (num+1)%100!=11 and num%10==0:
            l=l+1
            num=num+1
        d = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
             10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 
             17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        b = {1: "Ten", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 
             8: "Eighty", 9: "Ninety"}
        a = {3: "Hundred", 4: "Thousand",  7: "Million", 10: "Billion"}   
        
        global r1  
        global r    
        h = ''
        k = 0
        c = 0

        # Reverse the number
        temp = j=num
        while temp != 0:
            r = temp % 10
            k = k * 10 + r
            c += 1
            temp //= 10
        m=c
        
        while k != 0:
            r1 = k % 10
            if c in [11 ,8, 5, 2]: 
                r2 = k % 100
                r1 = rev(r2)
                print("r1=",r1)
                if 10 < r1 < 20:
                    h += d[r1] + " "
                    n=c-1
                    if(c==5 or c==8 or c==11):  
                        h += a[n] + " "
                    c -= 2
                    k //= 100
                    continue
                else:
                    r1 = r2 % 10    
            
            if r1 in b and c in [2, 5, 8 ,11]:
                h += b[r1] + " "
            elif c == 1 and r1 in d:
                h += d[r1] + " "
            elif c % 3 == 0 and r1 in d:
                h += d[r1] + " " + a[3] + " "
            elif c > 3  and c % 3 != 0:
                z=c
                print("z=",z)
                if r1 in d:
                    h += d[r1] + " " 
                if z in a:
                    h += a[z] + " "
            c -= 1  
            k //= 10
        if m==7 or m==8 or m==9:
            p=num//1000
            p=p%1000   
            
        if m==7  or m==8 or m==9:
            if(p==0):
                h=h.replace("Thousand ","",1)
        if m==10 or m==11 or m==12:
            o=j//1000000
            o=o%1000
            z=num//1000
            z=z%1000
        if m==10 or m==11 or m==12:
            if o==0:
                h=h.replace("Million ","",1)
            if z==0:
                 h=h.replace("Thousand ","",1)
        if(l==1):
            text=h
            text=text[:-5]
            h=text

        print(h)

def rev(l):
    s = 0
    while l != 0:
        q = l % 10
        s = q + s * 10
        l //= 10
    return s
print("NUMBER TO WORD CONVERTER(INTERNATIONAL SYSTEM)")    
ab=int(input("enter a number(between 0 to 10 billon):"))
numberToWords(ab)
