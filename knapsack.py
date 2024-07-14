import os

def unboundedKnapsack(k, arr):
    
    dp = [0] * (k + 1)
    
   
    for i in range(1, k + 1):
        
        for num in arr:
            if num <= i:
                dp[i] = max(dp[i], dp[i - num] + num)
    
    return dp[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        arr = list(map(int, input().rstrip().split()))
        result = unboundedKnapsack(k, arr)
        fptr.write(str(result) + '\n')

    fptr.close()
