class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            #add the current right letter to our count dic
            current_letter = s[right]
            count[current_letter] = count.get(current_letter, 0) + 1

            #calculate window size
            window_size = right - left + 1

            #highest count of a single letter in our window?
            highest_count = max(count.values())

            # If the letters we MUST change is more than 'k', we shrink.
            if window_size - highest_count > k:
                left_letter = s[left]
                count[left_letter] -= 1  
                left += 1                
            
            #update our longest valid window seen so far.
            #we calculate the window size again just in case we just shrank it.
            current_valid_window_size = right - left + 1
            max_length = max(max_length, current_valid_window_size)

        return max_length
            