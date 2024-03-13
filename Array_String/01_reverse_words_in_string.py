# https://leetcode.com/problems/reverse-words-in-a-string

# Test case
# "     t  adsfn adfbscns     adsf nsmf    a dfasdnfjams   adjajlsfhjks f as da da d a    "


# Approach 1: swapping words and restitching the string
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


# Approach 2: Bringing each word to the front
# Wouldn't work in python, try in cpp where string is mutable and can be updated in place.
def _reverse(self, s: str, start: int, end: int) -> str:
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    return s


def reverseWords(self, s: str) -> str:
    n = len(s)
    # Reverse the entire string
    s = self._reverse(s, 0, n - 1)

    # Reverse every word.
    k = 0
    while k < n:
        # reverse part of the string
        while k < n and s[k] == " ":
            k += 1
        start = k
        while k < n and s[k] != " ":
            k += 1
        end = k - 1
        s = self._reverse(s, start, end)

    # Trim off extra spaces between words
    idx, jdx = 0, 0
    while jdx < n:
        # moving the words forward
        while jdx < n and s[jdx] == " ":
            jdx += 1
        while jdx < n and s[jdx] != " ":
            s[idx] = s[jdx]
            idx += 1
            jdx += 1
        s[idx] = " "
        idx += 1

    s = s.rstrip(" ")
    return s


# string reverse(string s, int start, int end) {
#     while (start < end){
#         char temp = s[start];
#         s[start] = s[end];
#         s[end] = temp;
#         start++;
#         end--;
#     }
#     return s;
# }

# string reverseWords(string s) {
#     int n = s.length();
#     // Reverse the entire string
#     s = reverse(s, 0, n - 1);

#     // Reverse every word
#     int k = 0;
#     while (k < n) {
#         // reverse part of the string
#         while (k<n && isspace(s[k])) k += 1;
#         int start = k;
#         while (k<n && !isspace(s[k])) k += 1;
#         int end = k - 1;
#         s = reverse(s, start, end);
#     }

#     // Trim off extra spaces between words
#     int idx=0,jdx=0;
#     while (jdx < n) {
#         while (jdx<n and isspace(s[jdx])) jdx++;
#         while (jdx<n and !isspace(s[jdx])) {
#             s[idx] = s[jdx];
#             idx++; jdx++;
#         }
#         while (jdx<n and isspace(s[jdx])) jdx++;

#         if (jdx<n) {
#             s[idx] = ' ';
#             idx++;
#         }
#     }

#     s = s.substr(0, idx);
#     return s;
# }
