# CMPS 2200 Assignment 5
## Answers

**Name:** Joseph Wagner


Place all written answers from `assignment-05.md` here for easier grading.


- **1a.**
- The greedy approach would be to start with the greatest possible power of two that is less than or equal to $N. Subtract that power of two (incrementing a counter each time for total coins) from $N until that denomination is greater than the running value of $N or the running value of $N is equal to 0. If the value equals 0, return the coin counter. If the value is greater than the denomination but not equal to 0, repeat the process with the the next greatest power of two (2^(k-1)).
- This approach is optimal because since the coins are power of two, each time we subtract the greatest possible denomination from our running value, we will never subtract more than one of the same denomination. Thus, this result will always produce the correct answer optimally, and a way to see this is by thinking about it like converting a decimal number into binary. There is never a time where any binary digit would not be 0 or 1, and likewise we can think of the currency in this fashion - the greatest possible power of two we can subtract from a number will always yield 0 or a number less than that power of two.

- **1b.**
- The worst case for this greedy algorithm would be when N = 2^k - 1, or when we have a value that is one less than some power of two. Thinking about this in terms of binary, this would always yield a binary number with only 1's. 

- The work is O(N). The span would be O(log_2(N)) because the maximum tree depth would be having to recurse all the way down to 2^0. This would take log_2(N) recursions. 





- **2a.**
- Lets say we are given denominations = [1, 5, 7, 10] and we are given $12. Our greedy algorithm would return the minimum number of coins as 3, because it would use 10, 1, 1. However, the true minimum number of coins to make change is 2, as we can use 5, 7 to make $12. Thus, our greedy algorithm is not optimal as it does not always return the correct solution.
- **2b.**
- **3a.**
- The optimal substructure for this problem is MED(S, T) =
  - MED(S[1:], T[1:]), if S[0] = T[0]
  - 1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:],T[1:])), if S[0] != T[0]
- **3b.**



