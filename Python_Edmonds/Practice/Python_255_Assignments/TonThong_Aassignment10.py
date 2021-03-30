word_1 = 'azcbobobegghakl' #aooea
word_2 = 'qwertyuiop' #euio
word_3 = 'asdfghjkl' #a
word_4 = 'zxcvbnm' #

#Test word_1
print(''.join(map(str, list(filter(lambda char: char in ['a', 'e', 'o', 'i', 'u'], word_1)))))
#Test word_2
print(''.join(map(str, list(filter(lambda char: char in ['a', 'e', 'o', 'i', 'u'], word_2)))))
#Test word_3
print(''.join(map(str, list(filter(lambda char: char in ['a', 'e', 'o', 'i', 'u'], word_3)))))
#Test word_4
print(''.join(map(str, list(filter(lambda char: char in ['a', 'e', 'o', 'i', 'u'], word_4)))))
