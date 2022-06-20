from typing import Optional, Union

from MD6.hash.hash import Hash


class MD6:
    __size: int
    __key: str
    __levels: int

    def __init__(self,
                 size: Optional[int] = None,
                 key: Optional[str] = None,
                 levels: Optional[int] = None):
        self.__size = 256 if size is None else size
        self.__key = "" if key is None else key
        self.__levels = 64 if levels is None else levels

    def __call__(self, data: Union[str, bytes]):
        return Hash(data, self.__size, self.__key, self.__levels)
