"""LZW"""

class LZW:
    """
    LZW algorythm implementation.
    Contains such methods: encode, decode, find_right_ind.
    """
    def __init__(self, text) -> None:
        self.text = text
        self.dct = None
        self.code = None

    # encode
    def encode(self) -> tuple[list, dict]:
        """
        Compresing or encoding text using LZW algorythm.
        >>> try1 = LZW("abacabacabadaca")
        >>> try1.encode()
        [0, 1, 0, 2, 4, 6, 8, 3, 9]
        >>> try2 = LZW("abdabbadabcadba")
        >>> try2.encode()
        [0, 1, 3, 4, 1, 0, 6, 1, 2, 9, 8]
        >>> try3 = LZW("abacababacabc")
        >>> try3.encode()
        [0, 1, 0, 2, 3, 7, 6, 1, 2]
        >>> try4 = LZW("abacabadabacabae")
        >>> try4.encode()
        [0, 1, 0, 2, 5, 0, 3, 9, 8, 6, 4]
        >>> try5 = LZW("abcbabcdeadaba")
        >>> try5.encode()
        [0, 1, 2, 1, 5, 2, 3, 4, 0, 3, 5, 0]
        """
        # check
        if ".txt" in self.text:
            with open(self.text, "r", encoding="utf-8") as data:
                self.text = data.read()
        # dict
        self.dct = {val: i for i, val in enumerate(sorted(set(self.text)))}

        # result code and text copy
        self.code = []

        # loop
        ind = 0
        while ind != "end":
            ind2 = self.find_right_ind(self.text[ind:])
            if ind2 is not None:
                end = ind + ind2
                self.dct[self.text[ind:end]] = len(self.dct)
                self.code.append(self.dct[self.text[ind : end - 1]])
                ind = end - 1
                self.dct = self.dct
                self.code = self.code
            else:
                self.code.append(self.dct[self.text[ind:]])
                ind = "end"

        return self.code

    def find_right_ind(self, piece: str) -> int:
        """
        Find the right current element and returns index for slicing.
        """
        for i in range(len(piece)):
            if piece[: i + 1] not in self.dct.keys():
                return i + 1

    # decode
    def decode(self, dct: dict, code: list) -> str:
        """
        Decoding text using LZW algorythm.
        >>> lempel = LZW('abacabacabadaca')
        >>> me = lempel.encode()
        >>> dct_1 = {i: val for i, val in enumerate(sorted(set(lempel.text)))}
        >>> lempel.decode(dct_1, me) == 'abacabacabadaca'
        True
        """
        # check
        if dct is None:
            return "No dictinary provided, decoding is not possible."
        elif code is None:
            return "No code provided, decoding is not possible."

        # init
        text = ''
        text += dct[code[0]]
        self.code = code[1:]
        previous = 0

        # cycle
        for current in self.code:
            # if there is no such code in dict we make by taking
            # full previous code and its first character
            if current not in dct:
                dct[len(dct)] = dct[previous] + dct[previous][0]
            # this goes if everything is okay
            else:
                dct[len(dct)] = dct[previous] + dct[current][0]

            text += dct[current]
            previous = current

        return text
    
    def read_file(self, file):
        """
        Simply reads file.
        """
        with open(file, "r", encoding="utf-8") as data:
            return data.read()
    
# If you want to try using file

def write_file(code):
    """
    Writes encoded text to file.
    """
    with open("lzw.txt", "w", encoding="utf-8") as file:
        if isinstance(code, list) is True:
            for elem in code:
                file.write(str(elem))
        else:
            file.write(code)

def read_file(file):
    """
    Simply reads file.
    """
    with open(file, "r", encoding="utf-8") as data:
        return data.read()
 
