from text_crypter import TextCrypter
from audio_crypter import AudioCrypter


def crypt_text(file_name):
    text_crypter = TextCrypter()

    with open(f'text_files/{file_name}', 'r', encoding='utf-8') as original_file, \
            open(f'text_files/encrypted.txt', 'w', encoding='utf-8') as encrypted_file:
        for line in original_file:
            encrypted_line = text_crypter.encrypt(line.strip())
            encrypted_file.write(encrypted_line + '\n')

    with open(f'text_files/encrypted.txt', 'r', encoding='utf-8') as encrypted_file, \
            open(f'text_files/decrypted.txt', 'w', encoding='utf-8') as decrypted_file:
        for line in encrypted_file:
            decrypted_line = text_crypter.decrypt(line.strip())
            decrypted_file.write(decrypted_line + '\n')


def crypt_audio(file_name):
    audio_crypter = AudioCrypter()
    audio_crypter.encrypt(file_name, "encrypted.wav")
    audio_crypter.decrypt("encrypted.wav", "decrypted.wav")


if __name__ == '__main__':
    crypt_audio("original_audio.wav")
    crypt_text('original.txt')
