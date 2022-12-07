from palin import isPalindrome


def test_palin():
    assert isPalindrome("aabbaa") == True
    assert isPalindrome("asd") == False
    assert isPalindrome("okoko") == True
    assert isPalindrome("kisnd") == False
