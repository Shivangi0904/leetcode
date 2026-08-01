class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        vowel_count = 0
        for ch in s[:k]:
            if ch in vowels:
                vowel_count += 1
        max_count = vowel_count
        for right in range(k, len(s)):
            if s[right - k] in vowels:
                vowel_count -= 1
            if s[right] in vowels:
                vowel_count += 1
            max_count = max(max_count, vowel_count)
        return max_count