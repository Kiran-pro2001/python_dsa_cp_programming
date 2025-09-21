'''

412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104

'''


# Solution 

from typing import List


class Solution:
    def fizzBuzz(self, n:int) -> List[str]:  # n = 3
        answer = []
        for index in range(1,n+1): # n = 1,2,3
            if index%3 == 0 and index%5 == 0:
                # Number divisible by 3 and 5
                answer.append("FizzBuzz")
            elif index%3 == 0:
                # Number divisible by 3
                answer.append("Fizz")
            elif index%5 == 0:
                # Number divisible by 5
                answer.append("Buzz")
            else:
                # Number not divisible by 3 or 5 or both
                answer.append(str(index))
        return answer 
obj = Solution()
result = obj.fizzBuzz(3)
print(result)
            
