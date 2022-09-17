class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = filter(lambda ch: ch.isalnum(), s)   # x for x in
                                                              # filter out alphanumeric
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)   # make into lower case

        filtered_chars_list = list(lowercase_filtered_chars)   # make into a list
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list