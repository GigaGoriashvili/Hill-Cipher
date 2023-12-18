import numpy as np
from hill_cipher import HillCipher


class TextCrypter(HillCipher):
    __georgian_alphabet_mapping = {
        'ა': 0, 'ბ': 1, 'გ': 2, 'დ': 3, 'ე': 4, 'ვ': 5, 'ზ': 6, 'თ': 7, 'ი': 8, 'კ': 9,
        'ლ': 10, 'მ': 11, 'ნ': 12, 'ო': 13, 'პ': 14, 'ჟ': 15, 'რ': 16, 'ს': 17, 'ტ': 18, 'უ': 19,
        'ფ': 20, 'ქ': 21, 'ღ': 22, 'ყ': 23, 'შ': 24, 'ჩ': 25, 'ც': 26, 'ძ': 27, 'წ': 28, 'ჭ': 29,
        'ხ': 30, 'ჯ': 31, 'ჰ': 32,
        '.': 33, ',': 34, '?': 35, '!': 36, '-': 37, ';': 38, ':': 39, '(': 40, ')': 41, '[': 42,
        ']': 43, '{': 44, '}': 45, '<': 46, '>': 47, '"': 48, "'": 49, ' ': 50
    }

    def __init__(self, key=None, key_size=3):
        # for text case modulus is the length of mapping dictionary
        modulus = len(TextCrypter.__georgian_alphabet_mapping)
        # check if certain key is produced by user
        if key is None:    # if NO create automatically
            key = self._generate_key(modulus, size=key_size)
        else:   # if YES validate it
            key = self._validate_key(key, modulus)
        super().__init__(modulus, key)

    # mapping of alphabet vector into numerical one
    def _vector_of_str(self, block):
        vector = []
        for char in block:
            vector.append(self.__georgian_alphabet_mapping[char])
        return vector

    # search for character by corresponding numerical value
    def _get_key_from_value(self, target_value):
        for key, value in self.__georgian_alphabet_mapping.items():
            if value == target_value:
                return key
        return -1

    def encrypt(self, text):
        modulus = super().modulus
        key_size = self._key.shape[0]
        text = text.strip() # remove all spaces around
        if text == '':
            return ''
        # additive chars is the number of padding, if length of text is not divisible by modulus
        additive_chars = (key_size - len(text) % key_size) if len(text) % key_size != 0 else 0
        text += ' ' * additive_chars    # padded text
        # divide text into key sized string blocks
        blocks = [text[i:i + key_size] for i in range(0, len(text), key_size)]
        vectors = [self._vector_of_str(block) for block in blocks]  # convert string blocks into vectors
        encrypted_vectors = [np.dot(self._key, vector) % modulus for vector in vectors]     # encrypt vectors
        encrypted_text = ''
        # build string by corresponding char for encrypted numerical values of vectors
        for vector in encrypted_vectors:
            for i in vector:
                char = self._get_key_from_value(i)
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text):
        if text == '':
            return ''
        modulus = super().modulus
        key_size = self._key.shape[0]
        # find multiplicative inverse of key matrix in the given modulus
        key_inv = self._inverse_key(modulus)
        # divide text into key sized string blocks
        blocks = [text[i:i + key_size] for i in range(0, len(text), key_size)]
        vectors = [self._vector_of_str(block) for block in blocks]  # covert string blocks into vectors
        decrypted_vectors = [np.dot(key_inv, vector) % modulus for vector in vectors]   # decrypt vectors
        decrypted_text = ''
        # build string by corresponding char for encrypted numerical values of vectors
        for vector in decrypted_vectors:
            for i in vector:
                char = self._get_key_from_value(i)
                decrypted_text += char
        return decrypted_text.strip()   # remove spaces from around to eliminate padding added by encryptor
