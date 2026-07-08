class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # 1. Setup our target counts
        target_counts = {}
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1

        window_counts = {}
        have = 0
        need = len(target_counts)

        # 2. Setup window pointers and variables to track the best answer
        left = 0
        best_left = -1
        best_right = -1
        min_length = float('inf')

        # 3. Start sliding the right pointer
        for right in range(len(s)):
            char = s[right]
            
            # Add character to our window count
            window_counts[char] = window_counts.get(char, 0) + 1

            # Did we just get enough of this specific character?
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            # 4. Shrink the window while it is still valid
            while have == need:
                
                # Check if this is the shortest window we've found so far
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    best_left = left
                    best_right = right

                # Time to shrink: remove the left character from our count
                left_char = s[left]
                window_counts[left_char] -= 1
                
                # Did removing that character break our valid window?
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                
                # Move the left pointer forward
                left += 1

        # 5. Return the result
        if min_length == float('inf'):
            return ""
        else:
            return s[best_left : best_right + 1]