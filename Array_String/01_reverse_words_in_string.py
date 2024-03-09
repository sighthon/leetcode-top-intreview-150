# https://leetcode.com/problems/reverse-words-in-a-string

# Test case
# "     t  adsfn adfbscns     adsf nsmf    a dfasdnfjams   adjajlsfhjks f as da da d a    "


def reverseWords(self, s: str) -> str:
    s = s.lstrip(" ")
    s = s.rstrip(" ")

    n = len(s)
    idx = 0
    jdx = n - 1
    front_rem, end_rem = "", ""

    while idx < jdx:
        word_front = ""
        while idx < n and s[idx] != " ":
            word_front += s[idx]
            idx += 1

        word_end = ""
        while jdx > 0 and s[jdx] != " ":
            word_end = s[jdx] + word_end
            jdx -= 1

        # meaning you are operating on the same word
        if idx > jdx:
            break

        middle_string = s[idx + 1 : -(n - jdx)]
        middle_string = middle_string.lstrip(" ")
        middle_string = middle_string.rstrip(" ")

        # print(front_rem,"XX",word_front,"XX",middle_string, "XX",word_end,"XX",end_rem)

        if middle_string:
            s = f"{front_rem}{word_end} {middle_string} {word_front}{end_rem}"
        else:
            s = f"{front_rem}{word_end} {word_front}{end_rem}"
        n = len(s)
        idx = len(front_rem) + len(word_end) + 1
        jdx = n - (len(end_rem) + len(word_front) + 2)
        front_rem = s[:idx]
        end_rem = s[jdx + 1 :]
        # print(s)
        # print(idx, s[idx], jdx, s[jdx])

    return s
