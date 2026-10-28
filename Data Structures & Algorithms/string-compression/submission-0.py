
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        k = 0

        while i < n:
            prev = chars[i]
            count = 0

            while i < n and chars[i] == prev:
                count += 1
                i += 1

            chars[k] = prev
            k += 1

            if count > 1:
                for char in str(count):
                    chars[k] = char
                    k += 1

        return k



        