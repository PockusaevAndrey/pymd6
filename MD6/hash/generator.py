import binascii
from typing import List, Union

from MD6.hash.calc import HashCalc


class HashGenerator:
    def __call__(self, data: Union[str, bytes], size: int, key: str, levels: int) -> List[int]:
        data = self.__byte_convert(data)
        key = self.__byte_convert(key)
        if size <= 0:
            size = 1
        elif size > 512:
            size = 512

        return self.__hash(data, size, key, levels)

    def __hash(self, data: List[int], size: int, key: List[int], levels: int):
        hashCalc = HashCalc(data, size, key, levels)
        d, M = hashCalc(data)
        return self.__crop(d, M, True)

    @staticmethod
    def __byte_convert(input_str: Union[str, bytes]) -> List[int]:
        input_str: bytes = binascii.hexlify(input_str.encode("ascii") if isinstance(input_str, str) else input_str)
        o_byte = [int(input_str[i:i + 2], 16) for i in range(0, len(input_str), 2)]

        return o_byte

    def __crop(self, size: int, data: List[int], right: bool):
        length = int((size + 7) / 8)
        remain = size % 8

        data = data[len(data) - length:] if right else data[:length]
        if remain > 0:
            data[length - 1] &= (0xff << (8 - remain)) & 0xff

        return data
