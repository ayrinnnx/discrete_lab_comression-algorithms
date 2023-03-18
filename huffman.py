"""Huffman coding.
Includes encoding and decoding.
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
        """
        with open(self.path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                for elem in line.strip():
                    self.probability[elem] += line.count(elem)
        return self.probability

    def algorithm(self) -> dict:
        """
        Main algprithm of finding binary code.
        Creates new dict with same keys, but values are interpreted
        as '0' and '1'. The result of code is reversed.
        """
        value_dic = defaultdict(str) #dict to which we will add 0 and 1
        items = sorted(self.probability.items()) # ('letter', counting)
        while len(items) > 1:
            summing_value = items[0][1] + items[1][1]
            items.append((items[0][0] + items[1][0], summing_value))
            for letter in items[0][0]:
                value_dic[letter] += '0'
            for letter in items[1][0]:
                value_dic[letter] += '1'
            del items[0]
            del items[0]
            items.sort(key = lambda x: x[1])
        for key, elem in value_dic.items():
            value_dic[key] = elem[::-1]
        return value_dic

    def encoding(self, dictionary, file_write = 'encoded.txt'):
        """
        Encoding of the text.
        """
        encoded_file = open(file_write, 'w', encoding='utf-8')
        with open(self.path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                for letter in line:
                    encoded_file.write(dictionary[letter])
                encoded_file.write('\n')
        encoded_file.close()

    def decoding(self, dictionary, file_read = 'encoded.txt', file_write = 'decoded.txt'):
        """
        Decoding given code.
        """
        reversed_dic = dict([(value, key) for key, value in dictionary.items()])
        code_keys = reversed_dic.keys()
        file_write = open(file_write, 'w', encoding='utf-8')
        with open(file_read, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for ind, line in enumerate(lines):
                decoded_str = ''
                find_elem = ''
                for elem in line:
                    find_elem += elem
                    if find_elem in code_keys:
                        decoded_str += reversed_dic[find_elem]
                        find_elem = ''
                file_write.write(decoded_str)
                if ind != len(lines) - 1:
                    file_write.write('\n')
        file_write.close()




trying = Huffman("read.txt")
res = trying.reading()
dic = trying.algorithm()
trying.encoding(dic)
trying.decoding(dic)
