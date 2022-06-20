class Constants:
    b = 512
    c = 128
    n = 89

    S0 = 0x0123456789abcdef
    Sm = 0x7311c2812425cfa0

    Q = [
        0x7311c2812425cfa0, 0x6432286434aac8e7, 0xb60450e9ef68b7c1,
        0xe8fb23908d9f06f1, 0xdd2e76cba691e5bf, 0x0cd0d63b2c30bc41,
        0x1f8ccf6823058f8a, 0x54e5ed5b88e3775d, 0x4ad12aae0a6d6031,
        0x3e7f16bb88222e0d, 0x8af8671d3fb50c2c, 0x995ad1178bd25c31,
        0xc878c1dd04c4b633, 0x3b72066c7a1552ac, 0x0d6f3522631effcb
    ]

    t = [17, 18, 21, 31, 67, 89]
    rs = [10, 5, 13, 10, 11, 12, 2, 7, 14, 15, 7, 13, 11, 7, 6, 12]
    ls = [11, 24, 9, 16, 15, 9, 27, 15, 6, 2, 29, 8, 15, 5, 31, 9]
