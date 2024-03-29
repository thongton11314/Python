lyrics = '''Remember those walls I built
Well, baby, they're tumbling down
And they didn't even put up a fight
They didn't even make a sound

I found a way to let you win
But I never really had a doubt
Standing in the light of your halo
I got my angel now

It's like I've been awakened
Every rule I had you break it
It's the risk that I'm taking
I ain't never gonna shut you out

Everywhere I'm looking now
I'm surrounded by your embrace
Baby, I can see your halo
You know you're my saving grace

You're everything I need and more
It's written all over your face
Baby, I can feel your halo
Pray it won't fade away

I can feel your halo (halo) halo
I can see your halo (halo) halo
I can feel your halo (halo) halo
I can see your halo (halo) halo

Hit me like a ray of sun
Burning through my darkest night
You're the only one that I want
Think I'm addicted to your light

I swore I'd never fall again
But this don't even feel like falling
Gravity can't forget
To pull me back to the ground again

Feels like I've been awakened
Every rule I had you break it
The risk that I'm taking
I'm never gonna shut you out

Everywhere I'm looking now
I'm surrounded by your embrace
Baby, I can see your halo
You know you're my saving grace

You're everything I need and more
It's written all over your face
Baby, I can feel your halo
Pray it won't fade away

I can feel your halo (halo) halo
I can see your halo (halo) halo
I can feel your halo (halo) halo
I can see your halo (halo) halo
I can feel your halo (halo) halo
I can see your halo (halo) halo

I can feel your halo (halo) halo
I can see your halo (halo) halo
Halo, halo

Everywhere I'm looking now
I'm surrounded by your embrace
Baby, I can see your halo
You know you're my saving grace

You're everything I need and more
It's written all over your face
Baby, I can feel your halo
Pray it won't fade away

I can feel your halo (halo) halo
I can see your halo (halo) halo
I can feel your halo (halo) halo
I can see your halo (halo) halo

I can feel your halo (halo) halo
I can see your halo (halo) halo
I can feel your halo (halo) halo
I can see your halo (halo) halo
'''
#Convert lyric into a list
def toList(lyrics):
    return lyrics.replace('\n',' ').replace(', ', ' ').replace('(', ' ').replace(')', ' ').split(' ')

#Strip the list. No extra space in list
def strip(list):
    result = []
    for eachWork in list:
        if len(eachWork.strip()) > 0:
            result.append(eachWork)
    return result

#Find the frequency of word
def createFrequencyDict(list):
    myDict = {}
    for word in list:         
        myDict[word] = list.count(word)
    return myDict

#Get top frequency
def getTop(dict, topValue):
    newDict = {}
    for key in dict:
        if dict[key] >= topValue:
            newDict[key] = dict[key]
    return newDict

#List
list = toList(lyrics)
#List without extra space
stripList = strip(list)
#Frequency 
mostFrequency = createFrequencyDict(stripList)
#Print out the most frequency
print("The most frequency: %d times" % max(mostFrequency.values()))
#Print out the top frequency
print("Top frequency " + str(getTop(mostFrequency, 20)))




