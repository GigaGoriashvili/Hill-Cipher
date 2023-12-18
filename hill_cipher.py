import numpy as np


class HillCipher:
    def __init__(self, modulus, key=None):
        self._modulus = modulus
        self._key = key

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        new_key = self._validate_key(new_key, self._modulus)
        self._key = new_key

    @property
    def modulus(self):
        return self._modulus

    @modulus.setter
    def modulus(self, new_modulus):
        self._modulus = new_modulus

    # key matrix validation
    def _validate_key(self, key, modulus):
        # key must be quadratic
        if key.shape[0] != key.shape[1]:
            raise ValueError("Invalid key matrix. It must be a quadratic matrix.")
        det = np.linalg.det(key)
        # key must have multiplicative inverse in modulo
        if self._find_multiplicative_inverse(det, modulus) == -1:
            raise ValueError("Invalid key matrix. Determinant is not relatively prime to 34")
        return key % modulus

    def _find_multiplicative_inverse(self, det, modulus):
        multiplicative_inverse = -1
        for i in range(modulus):
            inverse = det * i
            if inverse % modulus == 1:
                multiplicative_inverse = i
                break
        return multiplicative_inverse

    def _inverse_key(self, modulus):
        det = int(round(np.linalg.det(self._key))) # determinant casted into int
        det_inv = self._find_multiplicative_inverse(det % modulus, modulus)
        # find adjugate matrix by multiplying determinant to inverse matrix
        adj = np.around(det * np.linalg.inv(self._key)).astype(int) % modulus
        return (det_inv * adj) % modulus

    # function to generate random key matrix
    def _generate_key(self, modulus, size=3):
        matrix = np.random.randint(0, modulus, size=(size, size))
        det = (np.linalg.det(matrix)) % modulus
        # matrix determinant must have multiplicative inverse in modulus
        while self._find_multiplicative_inverse(det, modulus) == -1:
            matrix = np.random.randint(0, modulus, size=(size, size))
            det = (np.linalg.det(matrix)) % modulus
        return matrix

    def update_key(self, size=3):
        self._key = self._generate_key(self._modulus, size)
