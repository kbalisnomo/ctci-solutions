import pytest

def string_compression(string):
    result = []
    saved = string[0]
    count = 0
    for i in range(len(string)):
        if string[i] == saved:
            count += 1
        else:
            result.append(saved)
            result.append(str(count))
            saved = string[i]
            count = 1
    result.append(saved)
    result.append(str(count))
    compressed_string = "".join(result)
    return compressed_string if len(compressed_string) < len(string) else string

class Test():
    def test_string_compression_small(self):
        string = "aabcccccaaa"
        assert string_compression(string) == "a2b1c5a3"
    def test_string_compression_long(self):
        string = "abc"
        assert string_compression(string) == string

