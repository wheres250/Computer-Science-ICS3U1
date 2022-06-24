"""
Author: Kvin2K
Date: 05/12/2022
Lab 5: CSIS Encodings Part 2
"""
def main():
    def capital_decoder(inputStr): #Processing
        #here we begin to search for all the uppercase characters
        cap_temp_list = [c for c in inputStr if c.isupper()]
        #Output
        #we output the list of capital characters
        print("".join(cap_temp_list))
        #Output 2
        #we output the number of capital characters
        upper_case_count = len(cap_temp_list)
        print("Count of Capital characters in code word: {0}".format(upper_case_count))
    #Input
    #This is the code that provides the processor to break down and find all the capital letters.
    capital_decoder("tony CAnnot believe That you and tRIsha are Not dAting anymore")

    def sentence_reverser(sentence): #Processing
        # Splitting the Sentence.
        words = Sentence.split(" ")
        # List Comprehension Technique to reverse words
        newWords = [word[::-1] for word in words]
        
        # Forming new sentence with new words aka reverse words
        newSentence = " ".join(newWords)
        return newSentence
    #Input  
    Sentence = "The quick brown Fox jumps over the lazy dog"
    #Output
    print(sentence_reverser(Sentence))

#Part 3: Dunder
if __name__ == '__main__':
    main()


""" 
    sources 
    Capital decoder: https://stackoverflow.com/questions/6602111/how-to-search-for-a-capital-letter-within-a-string-and-return-the-list-of-words
    Sentence Reverser: https://www.geeksforgeeks.org/python-reverse-word-sentence/
    Dunder: https://classroom.google.com/c/NDY0NzA4NzA0MDg4/a/MzU0ODM4NDMyMDIx/details
"""
