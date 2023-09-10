# leetcode link: https://leetcode.com/problems/encode-and-decode-strings/

# lintcode link: https://www.lintcode.com/problem/659/

class Codec:
    def encode(self, strs):
        return ''.join(map(lambda s: f"{len(s)}#{s}", strs))

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


strs = ["we", "say", ":", "yes"]

codec = Codec()

encoded_str = codec.encode(strs)

print("encoded string: " + encoded_str)

decoded_strings = codec.decode(encoded_str)

print(f"decoded string:  {decoded_strings}")
