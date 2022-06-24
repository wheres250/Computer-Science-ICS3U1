"""
Author: Kvin2K
Date: 04/13/2022
Prime numbers questions
"""
while True:
    #Question user would like to test/answer
    var = int(input("Enter the question you would like to answer: "))
#Q1
    if var == 1:
        def isPrime(n):
            """
            Explanation: Testing a number (7) and determing whether it is a prime number or not
                Args:
                n(int) : 7
                Return:
                False if not prime
                True if prime
            """
            if n <= 1 :
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
    def printPrime(n):
        for i in range(2, n + 1):
            if isPrime(i):
                print(i, end = " ")
    if __name__ == "__main__" :
        n = 7
        printPrime(n)
#Q2
    if var == 2:
        def test_prime(n):
            """
            Explanation: that takes in an int n and returns the number of primes less than the number! (Don't include the number itself)
                Args: n(int) : number that we will use to find # of primes.
                Return:
                true
                false
            """
            if (n==1):
                return False
            elif (n==2):
                return True;
            else:
                for x in range(2,n):
                    if(n % x==0):
                        return False
                return True   
#Q3
    if var == 3:
        num = int("Enter a number: ")
        if num > 1:
            """
            Explanation: the user will enter a number and the code will determine if it is prime or not
                Args:
                num(str): allow user to input number
                Return:
                number is prime
                number is not prime
            """
            for i in range(2,num):
                if (num % i) == 0:
                    print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is a prime number")
        else:
            print(num,"is not a prime number")