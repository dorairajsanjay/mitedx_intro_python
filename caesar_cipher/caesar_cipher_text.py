
# coding: utf-8

# In[52]:


### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


# In[53]:

### DO NOT MODIFY THIS FUNCTION ###
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


# In[ ]:


### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'


# In[ ]:

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        if shift > 26:
            print("Shift must be less than 27")
            return {}

        alists = [string.ascii_lowercase,string.ascii_uppercase]

        shift_dict = {}

        for alist in alists:

            for letter in alist:

                index = alist.index(letter)

                new_index = index + shift
                if new_index > 25: 
                    new_index = new_index - 26 

                shift_dict[letter] = alist[new_index]

        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)

        encrypted_text = []

        for letter in self.message_text:
            if letter in shift_dict.keys():
                encrypted_letter = shift_dict[letter]
            else:
                encrypted_letter = letter

            encrypted_text.append(encrypted_letter)

        return "".join(encrypted_text)


# In[ ]:

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        pass #delete this line and replace with your code here

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        pass #delete this line and replace with your code here

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        pass #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        pass #delete this line and replace with your code here


# In[ ]:

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        pass #delete this line and replace with your code here


# In[ ]:

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())


# In[34]:

import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        

    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
             another letter (string). 
    '''
    
    if shift > 26:
        print("Shift must be less than 27")
        return {}
    
    alists = [string.ascii_lowercase,string.ascii_uppercase]
    
    shift_dict = {}
    
    for alist in alists:
        
        for letter in alist:

            index = alist.index(letter)

            new_index = index + shift
            if new_index > 25: 
                new_index = new_index - 26 

            shift_dict[letter] = alist[new_index]
    
    return shift_dict


# In[38]:

print(build_shift_dict(26))


# In[60]:

def apply_shift(text, shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift        

    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''

    shift_dict = build_shift_dict(shift)
    
    encrypted_text = []
    
    for letter in text:
        if letter in shift_dict.keys():
            encrypted_letter = shift_dict[letter]
        else:
            encrypted_letter = letter
            
        encrypted_text.append(encrypted_letter)
        
    return "".join(encrypted_text)


# In[73]:

print(apply_shift("Hello World This is me!",13))


# In[90]:

def decrypt_message(encrypted_text):
    '''
    Decrypt self.message_text by trying every possible shift value
    and find the "best" one. We will define "best" as the shift that
    creates the maximum number of real words when we use apply_shift(shift)
    on the message text. If s is the original shift value used to encrypt
    the message, then we would expect 26 - s to be the best shift value 
    for decrypting it.

    Note: if multiple shifts are  equally good such that they all create 
    the maximum number of you may choose any of those shifts (and their
    corresponding decrypted messages) to return

    Returns: a tuple of the best shift value used to decrypt the message
    and the decrypted message text using that shift value
    '''
    WORDLIST_FILENAME = 'words.txt'
    word_list = load_words(WORDLIST_FILENAME)
    
    best_shift_value = 0
    best_decrypted_text = ""
    best_match_count = 0
    
    for shift_value in range(26):
        
        match_count = 0
        words_text = encrypted_text.split(' ')
        
        decrypted_text = []
        
        for word in words_text:
        
            decrypted_word = apply_shift(word,26-shift_value)
            
            decrypted_text.append(decrypted_word)

            if is_word(word_list,decrypted_word):
                match_count += 1
                
        if match_count > best_match_count:
            best_match_count = match_count
            best_decrypted_text = " ".join(decrypted_text)
            best_shift_value = shift_value
            
    return(best_shift_value,best_decrypted_text)
        


# In[91]:

print(decrypt_message("Uryyb Jbeyq Guvf vf zr!"))


# In[ ]:



