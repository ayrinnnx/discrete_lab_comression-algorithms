"""LZ77"""

class LZ77:
    """
    Implementation of LZ77 algorythm.
    Encode and decode methods.
    """
    def __init__(self, text, buff_size) -> int:
        self.text = text
        self.buf = buff_size

    def encode(self) -> list:
        """
        Does encoding using LZ77 algorithm.
        >>> lz77 = LZ77('abdabbadabcadba', 5)
        >>> lz77.encode()
        [(0, 0, 'a'), (0, 0, 'b'), (0, 0, 'd'), (3, 2, 'b'), \
(3, 1, 'd'), (5, 2, 'c'), (5, 2, 'b'), (3, 1, None)]
        >>> lz77 = LZ77('abacabacabadaca',5)
        >>> lz77.encode()
        [(0, 0, 'a'), (0, 0, 'b'), (2, 1, 'c'), (4, 7, 'd'), (4, 1, 'c'), (4, 1, None)]
        """
        # check
        if ".txt" in self.text:
            with open(self.text, "r", encoding="utf-8") as data:
                self.text = data.read()

        # init
        code = []
        index = 0

        # cycle
        while index < len(self.text):
            buffer_start = max(index - self.buf, 0)
            offset = 0
            lenght = 0

            # find step
            # step - value that shows how much steps back in buffer we need
            for i in range(buffer_start, index):
                step = 0
                while index+step < len(self.text) and self.text[index+step] == self.text[i+step]:
                    step += 1

                if step > offset:
                    lenght = step
                    offset = index - i

            # check if last or not
            if index + lenght < len(self.text):
                code.append((offset, lenght, self.text[index+lenght]))
            else:
                code.append((offset, lenght, None))
            index += lenght + 1

        return code

    def decode(self, code):
        """
        Does decoding using LZ77 algorithm.
        """
        # check if file
        if isinstance(code, list) is False:
            with open(code, "r", encoding="utf-8") as data:
                code = data.read().split("||")
        else:
            code = [str(elem[0]) + str(elem[1]) + str(elem[2]) for elem in code]

        # decode
        result = ""
        for val in code:
            if val != "" and val != 'one':
                step_back = len(result) - int(val[0])
                result += (
                    result[step_back : step_back + int(val[1])] + str(val[2])
                    if int(val[0]) != 0
                    else str(val[2])
                )
        if result[-1] != 'N':
            return result
        return result[:-1]


# You can try to compare by writing code to file
# But if you want to check, here is the code

def write_file(code):
    """
    Writes encoded text to file.
    """
    with open("compressed_77.txt", "w", encoding="utf-8") as file:
        if isinstance(code, list) is True:
            for elem in code:
                file.write(str(elem[0])+str(elem[1])+str(elem[2])+'||')
        else:
            file.write(code)

def read_file(file):
    """
    Simply reads file.
    """
    with open(file, "r", encoding="utf-8") as data:
        return data.read()

# You are welcome to use your file instead of lorem