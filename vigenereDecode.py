def decode(cipher, key):

    key = key.replace(" ","")    # remove space from key 
    key = key.upper()       # uppercase key
    
    c = list(cipher) # list of characters in cipher
    k = list(key)  # list of characters in key
    
    isUpper = True
    keyIndex = 0
    text = []

    # for each character in cipher:
    for char in c:
        # if current character is symbol, append it into cipher:
        if ord(char) < 65 or ord(char) > 122:
            text.append(char)
        elif ord(char) > 90 and ord(char) < 97:
            text.append(char)
        
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
            
            # create the text:
            t = ord(char) - ord(k[keyIndex]) + 65
            #print(t)
            if t < 65:
                t = t + 26

            # if the original text is lowercase, change the cipher to lowercase:
            if isUpper == False:
                t = t + 32

            text.append(chr(t))

            keyIndex += 1
    result = ''
    return result.join(text)

a = "Zlb jmspw psp Vfjwz Kfmbq! Ux’ym ywaze ds rnyv qwmd uyvjw bxkqvq byal hu Usg 14!"
b = "This is my key"
print(decode(a,b))