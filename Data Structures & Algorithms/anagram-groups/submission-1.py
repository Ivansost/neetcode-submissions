class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # empty dic
        groups = {}

        # Loop through each word in thelist
        for word in strs:
            # sort the word (returns 'a','e') then join it with nothing inbetween (ae) and set key = to that
            key = "".join(sorted(word))
            
            # check if that key is missing from the dictionary 
            if key not in groups:
                # If missing create new with an empty list as the bucket
                groups[key] = []
                
            # since bucket exists, add the original word to it
            groups[key].append(word)
            
        # use .list to return a list of values from the buckets
        return list(groups.values())

        