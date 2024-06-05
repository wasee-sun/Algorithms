#recurssion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
#permutation
def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)

    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)
            
if __name__ == "__main__":
    print(permute("AB", ""))