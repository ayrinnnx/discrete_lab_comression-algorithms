"""Huffman coding.
Includes encoding and decodind.
"""
from collections import defaultdict


class Huffman:
    """
    A class to represent the Huffman coding algorithm.
    Attributes:
        path (str): A string representing the path of the file to be compressed or decompressed.
    """

    def __init__(self, path: str) -> None:
        self.path = path
        self.probability = defaultdict(int)

    def reading(self) -> dict:
        """
        Reading our txt file, representing it as dictionary of letters and their occurance.
        Sorting it from the most usable.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                for elem in line.strip():
                    self.probability[elem] += line.count(elem)
        # sorting dictionary from the less usable till the most
        self.probability = dict(
            sorted(self.probability.items(), key=lambda item: item[1])
        )
        return self.probability


trying = Huffman("read.txt")
res = trying.reading()
print(res)
