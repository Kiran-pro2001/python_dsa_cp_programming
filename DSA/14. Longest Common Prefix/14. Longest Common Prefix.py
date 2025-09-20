'''

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 


'''
# logic explanation - https://youtu.be/Dt6gzsNrghQ?si=XfzcE6oUv5UQBNYf&t=400


# strs = [strin1, strin2, strin3]
# The first element (string1) will be the longest prefix that can be possible. Because any other values, they have to have all the characters that are present in the string 1. How can it happen, let's assume that, in the example, currently the substring1 is the value "xyz" something like this, now even if all other values like "xyzabc" something like that, and then "xyzabcd" and all the long values. 
# ["xyz", "xyzabc","xyzabcd"]

# Still the longest common prefix has to be the first substring as it's whole. It can never be longer than the first string inside the given array. That is the given fact. So using this logic we will try to treat that what if the first string is the longest common substring, and by treating this we will try to compare this with all the remaining strings that are currently present inside the array, and that's how we will be able to reach to the solution. 




# Code 

class Solution: 
    
 
 


