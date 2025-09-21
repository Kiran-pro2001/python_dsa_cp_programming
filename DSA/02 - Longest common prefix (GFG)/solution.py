'''

Longest common prefix
Difficulty: EasyAccuracy: 38.66%Submissions: 15K+Points: 2

Given two strings str1 and str2 of the same length. Find the longest prefix of str1 which is common in str2. Return the length of the longest common prefix.


Example 1:

Input: 
str1 = "geeks"
str2 = "dgeek"
Output: 4
Explanation: 
Longest prefix from str1 present in str2 is "geek". Hence, the answer is 4.
Example 2:

Input:
str1 = "practicegeeks"
str2 = "coderpractice"
Output: 8
Explanation: 
Longest prefix from str1 present in str2 is "practice". Hence, the answer is 8.
 

Expected Time Complexity: O(|str1|*|str2|)
Expected Auxiliary Space: O(|str1|)


'''

class Solution:
    def longestCommonPrefix(self, str1, str2):
        # code here
        if str1 in str2:
            return len(str1)
        else:
            for char in str1: 
                str1 = str1[:-1] # I am taking str1 as the reference, and removing the last char to match with str2
                if str1 in str2:
                    return len(str1)