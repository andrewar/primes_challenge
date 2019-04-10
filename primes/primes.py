import sys

def print_primes(n):
    """Print out the set of prime numbers, and their multiples"""
    primes_list = get_primes(n)
    mult_table = {}

    # Get the largest val for the formatting fields   
    cell_size = len(str(primes_list[-1]**2)) 

    print(" %*s"%(cell_size, " "), end=" ")
    for i in range(len(primes_list)):
        print(" %*s"%(cell_size, primes_list[i]), end=' ')
    print(" ")

    for i in range(len(primes_list)):
        print(" %*s"%(cell_size, primes_list[i]), end=' ')

        for j in range(len(primes_list)):
            val = 0
            if mult_table.get((i,j)):
                 val = mult_table[(i,j)]
            elif mult_table.get((j,i)):
                 val = mult_table[(j,i)]
            else:
                 val = primes_list[i]*primes_list[j]
                 mult_table[(j,i)] = val

            print(" %*s"%(cell_size, val), end=' ')

        print("")


def get_primes(n):
    """ Get (n) primes """
    primes = []
    x = 2
    while len(primes) < n:
        if is_prime(x):
            primes.append(x)
        x+=1 
    return primes

def is_prime(x):
    """ Determine if a number is prime """
    if x==2 or x==3:
        return True

    for i in range(2,int(x/2)+1):
        if x%i == 0:
            return False
    return True

 
if __name__=="__main__":
    if len(sys.argv) != 1:
        print("Please enter the number of primes you want.")
    try:
        print_primes(int(sys.argv[1]))
    except ValueError:
        print("%s is not a number. Please enter a number."%(sys.argv[1]))

