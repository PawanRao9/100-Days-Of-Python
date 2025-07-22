# a = (input("enter a num :"))

# if "pawan" in a :
#     print("sp")
# else :
#     print("correct commad please")    


import random

# Dictionary mapping normal words to code words
code_dict = {
    'hello': 'zeta', 
    'world': 'gamma', 
    'friend': 'delta', 
    'good': 'alpha', 
    'bad': 'beta',
    'how': 'omega',
    'are': 'epsilon',
    'you': 'kappa',
    'doing': 'sigma',
    'today': 'theta',
    'i': 'pi',
    'love': 'lambda',
    'coding': 'mu',
    'wassup': 'olas',
}

# Function to encrypt a sentence into code word language
def encrypt_sentence(sentence):
    words = sentence.split()
    encrypted_words = []
    
    for word in words:
        # Convert word to lowercase and check if it's in the dictionary
        word_lower = word.lower()
        if word_lower in code_dict:
            encrypted_words.append(code_dict[word_lower])
        else:
            # If the word isn't in the dictionary, just keep it as is
            encrypted_words.append(word)
    
    return ' '.join(encrypted_words)

# Function to decrypt a sentence back into normal language
def decrypt_sentence(code_sentence):
    words = code_sentence.split()
    decrypted_words = []
    
    # Inverse dictionary to map code words back to original words
    inverse_code_dict = {v: k for k, v in code_dict.items()}
    
    for word in words:
        if word in inverse_code_dict:
            decrypted_words.append(inverse_code_dict[word])
        else:
            decrypted_words.append(word)
    
    return ' '.join(decrypted_words)

# Example usage
if __name__ == "__main__":
    # Input sentence
    sentence = input("Enter a sentence to encrypt: ")
    
    # Encrypt the sentence
    encrypted = encrypt_sentence(sentence)
    print(f"Encrypted sentence: {encrypted}")
    
    # Decrypt the sentence
    decrypted = decrypt_sentence(encrypted)
    print(f"Decrypted sentence: {decrypted}")
