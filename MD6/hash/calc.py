from typing import List, Tuple

from MD6.constants import Constants


class HashCalc:
    @staticmethod
    def __to_word(i_byte: List[int]):
        return [((i_byte[i + 0] & 0xff) << 56) |
                ((i_byte[i + 1] & 0xff) << 48) |
                ((i_byte[i + 2] & 0xff) << 40) |
                ((i_byte[i + 3] & 0xff) << 32) |
                ((i_byte[i + 4] & 0xff) << 24) |
                ((i_byte[i + 5] & 0xff) << 16) |
                ((i_byte[i + 6] & 0xff) << 8) |
                ((i_byte[i + 7] & 0xff) << 0) for i in range(0, len(i_byte), 8)]

    @staticmethod
    def __from_word(i_word: List[int]):
        return [(i_word[i] >> j * 8) & 0xff for i in range(len(i_word)) for j in range(7, -1, -1)]

    def __init__(self, data: List[int], size: int, key: List[int], levels: int):
        K = key[:64]
        k = len(K)
        self.r = max(80 if k else 0, 40 + int(size / 4))
        self.K = self.__to_word(K + [0x00 for i in range(64 - len(K))])
        self.k = k
        self.ell = 0
        self.L = levels
        self.d = size

    def par(self, M: List[int]):
        P = 0
        B = []
        C = []
        z = 0 if len(M) > Constants.b else 1

        while len(M) < 1 or (len(M) % Constants.b) > 0:
            M.append(0x00)
            P += 8

        M = self.__to_word(M)
        while len(M) > 0:
            B.append(M[:int(Constants.b / 8)])
            M = M[int(Constants.b / 8):]
        i = 0
        p = 0
        l = len(B)

        while i < l:
            p = P if i == (len(B) - 1) else 0
            C += self.__mid(B[i], [], i, p, z)

            i += 1
            p = 0

        return self.__from_word(C)

    def seq(self, M: List[int]):
        P = 0
        B = []
        C = [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]

        while len(M) < 1 or (len(M) % (Constants.b - Constants.c)) > 0:
            M.append(0x00)
            P += 8

        M = self.__to_word(M)

        while len(M) > 0:
            B.append(M[:int((Constants.b - Constants.c) / 8)])
            M = M[int((Constants.b - Constants.c) / 8):]

        i = 0
        p = 0
        l = len(B)

        while i < l:
            p = P if i == (len(B) - 1) else 0
            z = 1 if i == (len(B) - 1) else 0
            C = self.__mid(B[i], C, i, p, z)

            i += 1
            p = 0

        return self.__from_word(C)

    def __f(self, N: List[int]):
        S = Constants.S0
        A = list(N)
        i = Constants.n

        for j in range(self.r):
            for s in range(16):
                x = S
                x ^= A[i + s - Constants.t[5]]
                x ^= A[i + s - Constants.t[0]]
                x ^= A[i + s - Constants.t[1]] & A[i + s - Constants.t[2]]
                x ^= A[i + s - Constants.t[3]] & A[i + s - Constants.t[4]]
                x ^= x >> Constants.rs[s]

                A += [0x00 for i in range(i + s - len(A) + 1)]
                A[i + s] = x ^ ((x << Constants.ls[s]) & 0xffffffffffffffff)

            S = (((S << 1) & 0xffffffffffffffff) ^ (S >> 63)) ^ (S & Constants.Sm)
            i += 16

        return A[(len(A) - 16):]

    def __mid(self, B: List[int], C: List[int], i: int, p: int, z: int):
        return self.__f(Constants.Q + self.K +
                        [((self.ell & 0xff) << 56) | i & 0xffffffffffffff,
                         ((self.r & 0xfff) << 48) | ((self.L & 0xff) << 40) | ((z & 0xf) << 36) | (
                                 (p & 0xffff) << 20) | (
                                 (self.k & 0xff) << 12) | (self.d & 0xfff)] +
                        C + B)

    def __call__(self, M: List[int]) -> Tuple[int, List[int]]:
        while True:
            self.ell += 1
            M = self.seq(M) if self.ell > self.L else self.par(M)

            if len(M) == Constants.c:
                break
        return self.d, M
