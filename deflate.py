"""DEFLATE"""
import os
from lz77 import LZ77
from huffman import Huffman

class Deflate:
    """
    Combining lz77 and Huffman codes.
    """
    def __init__(self, path:str) -> None:
        self.path = path
        self.dictionary = None

    def encoding(self, file_write: str = 'encoded.txt') -> None:
        """
        We are coding by lz77 first. Then using Huffman coding.
        """
        lz77 = LZ77(self.path, 5)
        write_file_d(lz77.encode())
        huff = Huffman('compressed_deflate.txt')
        huff.reading()
        self.dictionary = huff.algorithm()
        huff.encoding(self.dictionary, file_write)

    def decoding(self, file_read: str = 'encoded.txt', file_write: str = 'decoded.txt'):
        """
        Decoding process.
        The result will be at compressed.txt
        """
        huffman = Huffman(file_read)
        huffman.decoding(self.dictionary)
        lz77 = LZ77(file_write, 5)
        write_file_d(lz77.decode(file_write))
        os.remove("decoded.txt")

def write_file_d(code, path = 'compressed_deflate.txt'):
    """
    Writes encoded text to file.
    """
    with open(path, "w", encoding="utf-8") as file:
        if isinstance(code, list) is True:
            for elem in code:
                file.write(str(elem[0])+str(elem[1])+str(elem[2])+'||')
        else:
            file.write(code)
