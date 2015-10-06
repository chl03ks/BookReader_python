import string
import re


class fileReader(object):

    def __init__(self):
        super(fileReader, self).__init__()

    def readfile(self):
        file = open('book.txt', 'r')
        print file.read()

    def test_trans(self, line, table):
        return line.translate(table, string.punctuation).lower().strip()

    def printEveryWord(self, wordDic):
        print "\n----------------- Used Words -----------------\n"
        for word in wordDic:
            print word + ": " + str(wordDic[word])

    def top20Words(self, wordDic):
        popular_words = sorted(wordDic, key=wordDic.get, reverse=True)
        top_20 = popular_words[:20]
        print "\n----------------- Top 20 -----------------\n"
        for word in top_20:
            print word

    def splitlines(self):
        table = string.maketrans("", "")
        wordList = []
        wordDic = {}
        with open('book.txt') as file:
            cleanLines = []
            for line in file:
                lines = line.split('\n')
                for lins in lines:
                    cleanLines.append(self.test_trans(lins, table))
                    cleanLines = filter(None, cleanLines)
        for line in cleanLines:
            wordList = re.sub("[^\w]", " ", line).split()
            for word in wordList:
                if word in wordDic:
                    wordDic[word] += 1
                else:
                    wordDic[word] = 1
        self.printEveryWord(wordDic)
        self.top20Words(wordDic)
        return wordDic

    def compareDicToList(self, wordDic):
        print "\nWhat are words do you wanna serach?"
        print "write them separated by spaces:\n"
        count = 0
        words = raw_input()
        notInTheBook = ""
        wordlist = map(str, words.split())
        for word in wordlist:
            if word in wordDic:
                count += 1
            else:
                notInTheBook += word + ","
        print "This are the words that are not in the book: " + notInTheBook


fileReader = fileReader()
wordDic = fileReader.splitlines()
fileReader.compareDicToList(wordDic)
