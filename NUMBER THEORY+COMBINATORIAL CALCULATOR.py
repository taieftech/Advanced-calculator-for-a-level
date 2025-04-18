import sympy as sp
import itertools
import time
def main():
    try:    
        print("WELCOME TO NUMBER THEORY AND COMBINATORIAL CALCULATOR".center(65))
        print(time.strftime('%H h %M m %S s').center(60))
        a1=int(input("1.NUMBER THEORY Or 2.COMBINATORICS: "))
        type1=2
        if a1==type1:
            b1=int(input('1.Combinations 2.Permutations: '))
            b4=1
            if b1==b4:
                a2=set(input("Type the elements: "))
                a3=int(input("Number of elements in each subsets: "))
                print("Total possible combinations: ",len(list(itertools.combinations(a2,a3))))
                b2=input("Want to see the subsets? Type 'yes' if u are: ")
                b3='yes'
                if b2==b3:
                    print(list(itertools.combinations(a2,a3)))
                    while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                        else:
                            print('Thanks for using!')
                else:
                    print("Thanks for using!")
            else:
                a2=set(input("Type the elements: "))
                a3=int(input("Number of elements in each subsets: "))
                print("Total possible permutations: ",len(list(itertools.permutations(a2,a3))))
                b2=input("Want to see the subsets? Type 'yes' if u are: ")
                b3='yes'
                if b2==b3:
                    print(list(itertools.permutations(a2,a3)))
                    while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                        else:
                            print('Thanks for using!')
                else:
                    print("Thanks for using!")
                    
        else:
            a1=int(input("Type the Number\n1.Divisibility\n2.G.C.M\n3.L.C.M\n4.The number of divisors\n5.The sum of divisors\n6.The count of the numbers which are relatively prime\n7.Prime number check\nType= "))
            if a1==1:
                print("DIVISIBILITY".center(30))
                a2=(input("To divide: "))
                a3=(input("The divisor: "))
                print("The remainder is =",eval(a2)%eval(a3))
                
                if eval(a2)%eval(a3)==0:
                    print("It's divisible!")
                    while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                        else:
                            print('Thanks for using!')
                else:
                    print("It's not divisible!")
            elif a1==2:
                print("G.C.D".center(30))
                a2=int(input("1.Numerical 2.Algebraic .Type 1 or 2: "))
                if a2==1:
                    a3=int(input("1st Number: "))
                    a4=int(input("2nd Number"))
                    print('G.C.D is= ',sp.gcd(a3,a4))
                    while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                        else:
                            print('Thanks for using!')
                else:
                   x=sp.symbols('x')
                   a3=sp.sympify(input("Your 1st expression: "))
                   a4=sp.sympify(input("Your 2nd expression: "))
                   print("G.C.D is: ",sp.gcd(a3,a4))
                   while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                        else:
                            print('Thanks for using!')
            elif a1==3:
                print("L.C.M".center(30))
                a2=int(input("1.Numerical 2.Algebraic .Type 1 or 2: "))
                if a2==1:
                    a3=int(input("1st Number: "))
                    a4=int(input("2nd Number"))
                    print('L.C.M is= ',sp.lcm(a3,a4))
                    while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                        else:
                            print('Thanks for using!')
                else:
                   x=sp.symbols('x')
                   a3=sp.sympify(input("Your 1st expression: "))
                   a4=sp.sympify(input("Your 2nd expression: "))
                   print("L.C.M is: ",sp.lcm(a3,a4))
                   while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                        else:
                            print('Thanks for using!')
            elif a1==6:
                print("THE COUNTS OF THE NUMBER BEING RELATIVELY PRIME".center(30))
                a2=int(input("Type the number: "))
                print("Euler's Totient. It's= ",sp.totient(a2))
                while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                        else:
                            print('Thanks for using!')
            elif a1==4:
                print("THE NUMBER OF DIVISORS".center(30))
                a2=int(input("The number: "))     
                print("Total divisors: ",len(sp.divisors(a2)))
                while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                a3=input("Want to see? Type 'yes' if you are: ") 
                a4='yes' 
                if a3==a4:
                    print("Divisors: ",sp.divisors(a2)) 
                    while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                else:
                    print("Thanks")
                    while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                        else:
                            print('Thanks for using!')
            elif a1==5:
                print("THE SUM OF DIVISORS".center(30))
                a2=int(input("The number: "))
                print("Sum is :",sum(sp.divisors(a2)))
                while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
            elif a1==7:
                print("PRIME CHECKING".center(30))
                a2=input('The Number: ')
                if sp.totient(eval(a2))==eval(a2)-1:
                    print("It's a prime number!")
                    while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()
                else:
                    print("It's not a prime!")
                    while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()

    except:
        print("Invalid input! Use integer if it's recommended!\nFollow as guided!")
        while True:
                        x=input("Want to continue? Type 'yes' if you are: ")
                        y='yes'
                        if x==y:
                            main()                    
main()
#Note:Using eval type was necessary!