# Program Details
## General Implementation
* Hill Cipher program is implemented using OOP, there are two crypter classes, one for text and one for audio.
They inherit from the parent class hill_cipher.

* Key matrix is generated __automatically__ at the moment of creating crypter object, or you can pass certain key as a parameter.
You can update the key any time you want.
* Text crypter only works for __Georgian__ text and audio crypter only for __.wav__ files.
* Methods of audio crypter updates files on its own, but text crypter just returns the modified text.
* The program just uses **inverse** matrix to decrypt data, it doesn't solve the linear system.
> For more detailed information see the comments in code!

## Analysis
### Accuracy
* Text crypter is **fully** accurate, it decrypts the text including punctuation marks and result is
exactly the **same** text as original one since it uses maximal certain modular range.
* Audio crypter is **not fully** accurate, since it uses only specific modular range, while
some numeric data of audio can be **out of** this modular range, so it is not possible to recover data completely with this implementation.

### Time Efficiency
> The Program performance is not the best, however it is **fast enough** to use in some certain cases, since generating the key matrix
is the most inefficient task in my code, but it generates only once during the process and uses **same matrix** for the data at default.
It is important that the time is **linearly** dependent on data size, because number of blocks are **linearly** dependent on data size
and each block is multiplied by the same key **only once**. Thus, it needs asymptotically the same amount of time for bigger data as smaller one.
    
### Storage Efficiency
> The storage efficiency of the code is reasonable, and the memory requirements are generally influenced by the key size and the 
length of the input text. Efficiency for key is **O(size^2)** and for text it is **O(length)**. Same happens for audio, because it needs **linear**
storage efficiency for audio file, and it uses the matrix generated using the **same method** as for text

## Conclusion
### Pros and Cons
> **_Pros_**:
* Customizable alphabet mapping
* High accuracy of Key generation and validation
* Well-structured and readable using OOP and commenting

> **_Cons_**:
* Alphabet Mapping Limitation, only predefined characters
* Decrypted audio is not fully the same as original
* Limited Error Handling


### Use Cases
In the real world, only hill cipher **is not** generally used. There are more advanced cryptographic techniques to encrypt data,
However, generally, this code can be applied to many cases:
* **Safe communication** in chats for text and voice messages by not letting unauthorised user to read this data.
* **Exam paper encryption** can be a useful way to prevent leaking of the information about it.
* **Military communication** involves also confidentiality. Transmitted messages must remain secure by encrypting.






