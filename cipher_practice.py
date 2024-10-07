import string

alphabet=string.ascii_lowercase
print(alphabet)
# test
print(alphabet.index('d'))

def decode_cypher(text, shift):
    decoded = ''
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift) % 26
            decoded += alphabet[new_index]
        else: decoded += letter
    return decoded

#test function
print(decode_cypher('a', 10))

cypher = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

print(decode_cypher(cypher, 10))

# send encoded message
send_cypher = "hey Vishal, fuck you because this exercise was way too hard but necessary at the same time."

def encode_cypher(text, shift):
    decoded = ''
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) - shift) % 26
            decoded += alphabet[new_index]
        else: decoded += letter
    return decoded

# print(encode_cypher(send_cypher, 10))

cypher_2 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."

# print(decode_cypher(cypher_2, 10))

cypher_3 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

# print(decode_cypher(cypher_3, 14))

cypher_4 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# brute force loop that uses decode_cypher function
def shift_loop(text):    
    for i in range(20):
        decoded_text = decode_cypher(text, i)
        print("for indicie " + str(i) + "\n" + decoded_text)

# print(shift_loop(cypher_4))

# Vigenere Cipher →
cypher_5 = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"

keyword = "friends"

import string

# Define the alphabet
alphabet = string.ascii_lowercase

def vigenere_encode(plain_text, keyword):
    encoded = ''
    keyword_repeated = ''
    keyword_index = 0

    # Prepare the repeated keyword to match the length of the plain text
    for letter in plain_text:
        if letter in alphabet:
            keyword_repeated += keyword[keyword_index % len(keyword)].lower()
            keyword_index += 1
        else:
            keyword_repeated += letter  # Keep non-alphabetic characters unchanged

    # Encode the message
    for i in range(len(plain_text)):
        letter = plain_text[i]
        if letter in alphabet:
            shift = alphabet.index(keyword_repeated[i])
            new_index = (alphabet.index(letter) + shift) % 26
            encoded += alphabet[new_index]
        else:
            encoded += letter  # Keep non-alphabetic characters unchanged
            
    return encoded

de_coded_message = vigenere_encode(cypher_5, keyword)
# test the decoder
print(de_coded_message)

message_test = "I hate this so much, what a bad way to learn functional, on the job python usage"

keyword_2 = "hate"

encoded_message = vigenere_encode(message_test, keyword_2)

print(encoded_message)
