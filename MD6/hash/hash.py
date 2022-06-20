from typing import List, Union

from MD6.hash.generator import HashGenerator


class Hash:
    __byte: List[int]
    hash_generator = HashGenerator()

    def __init__(self, data: Union[str, bytes], size: int, key: str, levels: int):
        self.__byte = self.hash_generator(data, size, key, levels)

    def __str__(self):
        return ''.join(["%02x" % i for i in self.__byte])

    def raw(self):
        return ''.join((chr(i) for i in self.__byte))
