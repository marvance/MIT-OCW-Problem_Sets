# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        letter_dictionary = {}

        punctuation = list(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")

        for i, char in enumerate(vowels_permutation.lower()):
            letter_dictionary[VOWELS_LOWER[i]] = char
        for i, char in enumerate(vowels_permutation.upper()):
            letter_dictionary[VOWELS_UPPER[i]] = char
        for char in CONSONANTS_LOWER:
            letter_dictionary[char] = char
        for char in CONSONANTS_UPPER:
            letter_dictionary[char] = char
        for symbol in punctuation:
            letter_dictionary[symbol] = symbol
        return letter_dictionary
        
        
        
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        encrypted_message = []
        for char in self.message_text:
            encrypted_message.append(transpose_dict[char])
        return ''.join(encrypted_message)
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        #list of possible vowel transpositions from possible vowels permutations
        tranpose_dict_list = []
        #list of decrypted messages
        de_message_list = []
        #list of all permutations (letter orders) of aeiou
        perm_list = get_permutations('aeiou')
        #for each possible permutation
        for perm in perm_list:
            #add to trans_dict_list the dictionary that assigns
            #transpositions according to the current permutation
            tranpose_dict_list.append(self.build_transpose_dict(perm))
        #for dictonary in list of possible transposition dictionaries
        for dic in tranpose_dict_list:
            #decrypted message equals text after you transpose it 
            #with the current dictionary
            de_message = self.apply_transpose(dic)
            #append current decrypted message to list of decrypted messages
            de_message_list.append(de_message)
        #store True or False values when checking to see if
        #a portion of the message is a real word
        test = []
        #store messages plus their number of True values from test[]
        big_test = []
        #get list of valid words to compare decrypted text to
        word_list = self.get_valid_words()
        #for message in list of decrypted messages
        for mes in de_message_list:
            #decrypted words equals each word in message separated
            de_words = mes.split()
            print("decrypted words: ", de_words)
            #for each word in decrypted message
            for word in de_words:
                #check to see if it's a real word
                if is_word(word_list, word):
                    #if it is, append a value of True to list of 
                    #"is it a word?" booleans
                    test.append(1)
                else:
                    #if it's not, append a value of false
                    test.append(0)
            #append to list of _______ a tuple containing the total number of True values for 
            #the current message in message list,
            #plus the message itself
            big_test.append((sum(test), mes))
            print("big test: ",big_test)
            #you're done using test, so delete all its contents
            del test[0:len(test)]
        #best choice is the maximum key in big_test
        best_choice = max(big_test)
        #store possible decrypted messages that might become result
        possible_de_message = []
        #for tuple in list of messages and number of True values
        for tup in big_test:
            #if the first tuple has the max number of True values
            #and the second tuple is not already in possible decrypted messages
            if tup[0] == best_choice[0] and tup[1] not in possible_de_message:
                #add to possible decrypted messages the second tuple
                possible_de_message.append(tup[1])
        #initialize empty string to hold result
        de_string = ''
        #for message in possible results
        for mes in possible_de_message:
            #result equals current result, a comma to separate, and the message 
            de_string = de_string + ', ' + mes
            #return everything after the comma in result 
        return de_string[1:]
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
