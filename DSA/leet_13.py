class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)
        
        for i in range(n):
            current_val = roman_map[s[i]]
            # If the next value is greater, subtract current value (e.g., IV, IX)
            if i + 1 < n and current_val < roman_map[s[i + 1]]:
                total -= current_val
            else:
                total += current_val
                
        return total

if __name__ == "__main__":
    sol = Solution()
    test_string = "MCMXCIV"  # Expected output: 1994
    print(f"The integer value of {test_string} is: {sol.romanToInt(test_string)}")
