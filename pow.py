import hashlib
import itertools

def proof_of_work(prefix, total_len, end=b'\x00\x00\x00'):
    alphanum = list(map(ord, ['0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z']))

    for c in itertools.combinations_with_replacement(alphanum, total_len - len(prefix)):
        guess = bytes(c)
        if hashlib.sha1(prefix+guess).digest().endswith(end):
            return prefix+guess

    raise Exception("Proof of work failed")
