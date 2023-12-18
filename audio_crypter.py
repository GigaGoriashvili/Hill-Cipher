from hill_cipher import HillCipher
import wave
import numpy as np


class AudioCrypter(HillCipher):
    def __init__(self, key=None, key_size=4, modulus=256):
        # check if certain key is produced by user
        if key is None:  # if NO create automatically
            key = self._generate_key(modulus, size=key_size)
        else:  # if YES validate it
            key = self._validate_key(key, modulus)
        super().__init__(modulus, key)

    def encrypt(self, input_file, output_file):
        # read from original file to encrypt data
        with wave.open(f'audio_files/{input_file}', 'rb') as wave_file:
            # dividing audio files into frames represented by numbers from 0 to 255
            frames = np.frombuffer(wave_file.readframes(wave_file.getnframes()), dtype=np.uint8)
            key_size = self.key.shape[0]
            # padding if number of frames is not divisible by key size
            padding = key_size - len(frames) % key_size
            # arrange frames into vectors of size key
            frames = np.pad(frames, (0, padding), 'constant').reshape(-1, key_size)
            # encrypt frame vectors and "devectorize" them
            encrypted_frames = np.mod(np.matmul(frames, self.key), self.modulus).astype(np.uint8)
            # arrange frames into audio again to the output file
        with wave.open(f'audio_files/{output_file}', 'wb') as output_wave_file:
            output_wave_file.setparams(wave_file.getparams())
            output_wave_file.writeframes(encrypted_frames.tobytes())

    def decrypt(self, input_file, output_file):
        # read from encrypted file to decrypt it
        with wave.open(f'audio_files/{input_file}', 'rb') as wave_file:
            # dividing audio files into frames represented by numbers from 0 to 255
            frames = np.frombuffer(wave_file.readframes(wave_file.getnframes()), dtype=np.uint8)
            key_size = self.key.shape[0]
            # padding if number of frames is not divisible by key size
            padding = key_size - len(frames) % key_size
            # arrange frames into vectors of size key
            frames = np.pad(frames, (0, padding), 'constant').reshape(-1, key_size)
            # find multiplicative inverse of key matrix in the given modulus
            reversed_matrix = self._inverse_key(self.modulus)
            # decrypt frame vectors and "devectorize" them
            decrypted_frames = np.mod(np.matmul(frames, reversed_matrix), self.modulus).astype(np.uint8)
            # arrange frames into audio again to the output file
        with wave.open(f'audio_files/{output_file}', 'wb') as output_wave_file:
            output_wave_file.setparams(wave_file.getparams())
            output_wave_file.writeframes(decrypted_frames.tobytes())
