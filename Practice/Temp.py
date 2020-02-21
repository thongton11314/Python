import re
lyric = """
beautiful is dep
not dep is xau
aade bae bautyr 114 abet 114 were aaaa eee 114 asd 114
thong*ton aha *thong thong* **Thong Thong*****Thong Thong*** * dep's
thong's ae's 11 12 115 11e aaa aaa 115 +thong113+ thong beautiful aade bae
"""

#lyric = """thong's abb 116 11 12 115 115 11e 116 aaa"""

def nonDuplicateWordInList(listOfWord):
    nonDuplicatedList = []
    for eachWord in listOfWord:
        if eachWord not in nonDuplicatedList:
            nonDuplicatedList.append(eachWord)
    return nonDuplicatedList

# has both 'a' and 'e' in it
word = re.findall(r'\w*a\w*e\w*|\w*e\w*a\w*', lyric)
print(nonDuplicateWordInList(word))


