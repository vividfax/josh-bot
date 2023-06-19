import random
import re


def main():

    code = ""
    samples = readSamples('sampleList.txt')
    ipsum = readSamples('ipsum.txt')
    random.seed(ipsum[0][-1])
    random.shuffle(samples)
    intsArr = splitSentences(ipsum[0])
    intsArr = stripPunctuation(intsArr)
    for i in range(len(intsArr)):
        ints = splitWords(intsArr[i])
        code += writeD2(i+1, samples, ints)
        # print(code)
    code += "hush"
    writeTidal(code, 'my.tidal')


def splitSentences(ipsum):
    sentences = re.split('[.] |, ', ipsum)
    return sentences


def stripPunctuation(sentences):
    newSentences = []
    for i in range(len(sentences)):
        sentences[i] = sentences[i].replace("'", '')
        sentences[i] = sentences[i].replace("-", '')
        sentences[i] = sentences[i].replace(",", '')
        sentences[i] = sentences[i].replace(":", '')
        sentences[i] = sentences[i].replace(";", '')
        newSentences.append(sentences[i])
    return newSentences


def splitWords(lines):
    arr = []
    words = lines.split(' ')

    for i in range(len(words)):
        letter = words[i][0]
        arr.append([ord(letter.lower()), len(words[i])])
    return arr


def readSamples(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines


def writeD(i, samples):
    d = "d" + str(i) + " $ "
    d += random.choice(["fast", "hurry"]) + " "
    d += str(random.choice([1, 2, 0.5])) + " $ sound \""
    for i in range(random.randint(1, 4)):
        if random.randint(0, 3) == 0:
            d += random.choice(["~", "."]) + " "
        else:
            d += random.choice(samples).strip() + ":"
            d += str(random.randint(0, 100))
            if random.randint(0, 2) == 0:
                d += random.choice(["*", "!", "/", "@"])
                d += str(random.randint(2, 4))
            d += " "
    d = d.strip(". ")
    d += "\" # legato 1\n\n"
    return d


def writeD2(i, samples, ints):
    d = "d" + str(i)
    d += " $ slow 2"
    d += " $ sound \""

    for i in range(len(ints)):
        # print(ints[i])
        d += samples[ints[i][0]].strip() + ":" + str(ints[i][1])
        d += " "

    d = d.strip(". ")
    d += "\" # legato 1\n\n"
    return d

def writeTidal(text, filename):
    with open(filename, 'w') as f:
        f.write(text)


main()
