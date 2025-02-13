from typing import List
def shift(array: List[int]) -> List[int]:
    byte_stream = []
    byte_number = 0
    while byte_number < 189:
        new_byte = array[6] ^ array[4] ^ array[3] ^ array[1] ^ array[0] # Dodanie bitu, który opuszcza listę (indeks 6), do strumienia
        byte_stream.append(array[6])
        array = [new_byte] + array[:-1] # Przesunięcie bitów: nowy bit na miejsce 0, reszta w prawo
        byte_number += 1
    return byte_stream
def LSFR():  # Bity st. 6, 5, 3, 2 -> pozycje w liście: 0, 1, 3, 4
    # indeksy:    [0, 1, 2, 3, 4, 5, 6]
    # stopień:    [6, 5, 4, 3, 2, 1, 0]
    # Wybrany klucz początkowy
    seed = [1, 0, 0, 0, 0, 1, 1]
    list_of_bytes = shift(seed)
    print(list_of_bytes)
    # Konwersja strumienia bitów na ciąg tekstowy
    stream_of_bytes = ''.join(map(str, list_of_bytes))
    # Podział na okresy
    period1 = stream_of_bytes[:63]
    period2 = stream_of_bytes[63:126]
    period3 = stream_of_bytes[126:189]
    print("Period 1:", period1)
    print("Period 2:", period2)
    print("Period 3:", period3)

LSFR()

def encryption():
    information = "11110110111011011110111111111111111"
    key = "11000010001010010110010011101101111"
    # Zamieniamy ciąbi bitów na listy aby móc liczyć XOR konkretnych bitów
    information_array = [int(bit) for bit in information]
    key_array = [int(bit) for bit in key]
    cryptogram_stream = ''
    # Dla każdego bitu z klucza i informacji jawnej liczymy XOR
    for i in range(len(key_array)):
        cryptogram = key_array[i] ^ information_array[i]
        cryptogram_stream += str(cryptogram)
    print("Zaszyfrowany ciąg bitów: ", cryptogram_stream)
    return cryptogram_stream

def decryption():
    cryptogram = encryption()
    key = "11000010001010010110010011101101111"
    # Zamieniamy ciąbi bitów na listy aby móc liczyć XOR konkretnych bitów
    cryptogram_array = [int(bit) for bit in cryptogram]
    key_array = [int(bit) for bit in key]
    information_stream = ''
    # Dla każdego bitu z klucza i szyfrogramu liczymy XOR
    for i in range(len(key_array)):
        information = key_array[i] ^ cryptogram_array[i]
        information_stream += str(information)
    print("Odszyfrowany ciąg bitów: ", information_stream)
    return information_stream

decryption()