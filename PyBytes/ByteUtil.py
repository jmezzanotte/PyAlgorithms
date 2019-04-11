
def _print_ascii_byte_helper(num, bit_val=128):

    """
    Helper function that builds a list that represents they byte for a given value.
    Does not always return a list of length 8, depending on the most significant bit.
    :param num: Number to represent as a byte 
    :param bit_val: The largest byte value in the byte(s). For example 128 for 1 byte. 
    :return: A representation of the byte in a list. 
    """

    #  we can immediately return all 0s
    if num == 0:
        return [0] * 7

    if num == bit_val:
        return [1]

    if num % bit_val != num and num != bit_val:
        return [1] + _print_ascii_byte_helper((num % bit_val), (bit_val / 2))

    if (num % bit_val) == num:
        return [0] + _print_ascii_byte_helper(num, bit_val / 2)


def ascii_byte(num):

    """
    Function that builds a list that represents they byte for a given value.
    :param num: Number to represent as a byte 
    :param bit_value: The largest byte value in the byte(s). For example 128 for 1 byte.
    :return: A representation of the byte in a list. 
    """

    byte = _print_ascii_byte_helper(num)
    return byte + ([0] * (8 - len(byte)))


def is_odd(byte):

    """
    Determines whether or not a byte represents an odd value or not.
    :param byte: An 8 bit byte representation as a list.
    :return: True if byte is odd, False otherwise.
    """

    if not isinstance(byte, list):
        raise TypeError("List is required.")


    if byte[-1] == 0:
        return False
    if byte[-1] == 1:
        return True


def lsbit(byte):

    for index, value in enumerate(byte):
        if value == 1:
            return "0x" + ''.join(str(i) for i in byte[index:])


if __name__ == "__main__":
    import os
    import json
    byte  = ascii_byte(65)
    print byte
    # print is_odd(byte)
    # print lsbit(byte)
    # print byte
    #
    # parent_dir = os.path.dirname(os.path.dirname(__file__))
    # with open(os.path.join(parent_dir, 'tests', 'ascii.json')) as fp:
    #     data = json.load(fp)
    #
    # print print_byte(16) 1 2 4 8 16 32 64 128  256 512 1024 2048 4096 8192 16384 32768
