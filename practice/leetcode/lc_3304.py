# LC 3304. Find the K-th Character in String Game I

'''
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.


Example 1:

Input: k = 5
Output: "b"
Explanation:
Initially, word = "a". We need to do the operation three times:
- Generated string is "b", word becomes "ab".
- Generated string is "bc", word becomes "abbc".
- Generated string is "bccd", word becomes "abbcbccd".

Example 2:

Input: k = 10
Output: "c"

Constraints: 1 <= k <= 500

Topics: Math, Bit Manipulation, Recursion, Simulation
'''

# Coding -

'''

# My Code

class Solution:

    def shift_each_char_by_one(self, word: str) -> str:
        next_chars = ""

        for c in word:
            alphabet_index = ord(c) - ord('a')
            next_index = (alphabet_index + 1) % 26
            next_char = chr(next_index + ord('a'))
            next_chars += next_char

        return next_chars


    def kthCharacter(self, k: int) -> str:

        word = "a"

        if(k == 1):
            return 'a'

        while(len(word) < k):
            next_char = self.shift_each_char_by_one(word)

            word += next_char
        
        return word[k - 1]
'''

# Optimized Solution - 
class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = 0
        
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            ans += 1
        return chr(ord("a") + ans)
    
    
k = int(input("Enter the value of K: "))

solution = Solution()
result = solution.kthCharacter(k)
print("Result:", result)