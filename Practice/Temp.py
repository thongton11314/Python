import re
lyric = """
beautiful is dep
not dep is xau
aade bae bautyr abet were aaaa eee 
thong*ton aha *thong thong* **Thong Thong*****Thong Thong*** *
"""

# has a '*' in it
word = re.findall(r"[\w]+[^ae]+\w*", lyric)
print(word)
