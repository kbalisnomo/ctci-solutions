import pytest

def urlify(str, t_len):
    result = []
    for i in range(t_len):
        if str[i] == ' ':
            result.append("%20")
        else:
            result.append(str[i])
    return ''.join(result)

class Test():
    def test_urlify(self):
        str = "Mr John Smith    "
        t_len = 13
        expected = "Mr%20John%20Smith"
        assert urlify(str, t_len) == expected
