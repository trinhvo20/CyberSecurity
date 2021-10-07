
def encode(text, key):

    key = key.replace(" ","")    # remove space from key 
    key = key.upper()       # uppercase key
    
    t = list(text) # list of characters in text
    k = list(key)  # list of characters in key
    
    isUpper = True
    keyIndex = 0
    cipher = []
    
    # for each character in text:
    for char in t:
        # if current character is symbol, append it into cipher:
        if ord(char) < 65 or ord(char) > 122:
            cipher.append(char)
        elif ord(char) > 90 and ord(char) < 97:
            cipher.append(char)
        
        # if the character is a letter:
        else:
            # if letter is lowercase, make it uppercase:
            if ord(char) > 90:
                isUpper = False
                char = char.upper()
            # if the letter is uppercase:
            else:
                isUpper = True
            
            # if the keyIndex is out of range, set it back to 0:
            if keyIndex == len(k):
                keyIndex = 0

            # create the cipher:
            c = ord(char) + ord(k[keyIndex]) - 65

            if c > 90:
                c = c - 26

            # if the original text is lowercase, change the cipher to lowercase:
            if isUpper == False:
                c = c + 32

            cipher.append(chr(c))

            keyIndex += 1
    result = ''
    return result.join(cipher)

a = "Get ready for Cyber Storm! We’re going to turn your world upside down on May 14!"
b = "This is my key"
print(encode(a,b))