import urllib


def is_chs(string):
    if isinstance(string, unicode):
        string = string.encode('utf8')
    for c in string:
        if ord(c) > 127:
            return True
    return False


def ensure_unicode(s):
    if s is None:
        return s
    if not isinstance(s, basestring):
        s = '%s' % s
    if isinstance(s, unicode):
        return s
    else:
        return s.decode('utf-8')


def ensure_ascii(s):
    if s is None:
        return s
    if not isinstance(s, basestring):
        s = '%s' % s
    if isinstance(s, str):
        return s
    else:
        return s.encode('utf-8')


def ensure_length(s, maxlen):
    assert(maxlen > 3)
    if len(s) <= maxlen:
        return s
    else:
        return s[:(maxlen-3)] + '...'


def compare_str(str1, str2):
    if str1 > str2:
        return 1
    elif str1 < str2:
        return -1
    else:
        return 0


def equal(str1, str2):
    if (isinstance(str1, unicode) and isinstance(str2, unicode)) or \
            (isinstance(str1, str) and isinstance(str2, str)):
        return (str1 == str2)
    else:
        return (ensure_unicode(str1) == ensure_unicode(str2))


def url_quote(s):
    return urllib.quote(ensure_ascii(s))

def url_unquote(s):
    return urllib.unquote(s)

def url_join(*args):
    args = map(ensure_ascii, args)
    args = map(urllib.quote, args)
    return '/'.join(args)


def md5hash(string):
    import hashlib
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


def split_key_value(line, sep=':'):
    pos = line.find(sep)
    if pos > 0:
        key = line[:pos].strip()
        val = line[pos+1:].strip()
        return (key, val)
    else:
        return (None, None)


def bitmask_string(nums):
    ret = 0
    for num in nums:
        assert isinstance(num, int)
        if num > 0:
            ret |= 1 << (num - 1)
    return hex(ret)


if __name__ == '__main__':
    import sys
    print md5hash('12345')
    print compare_str('Ab', "B")
    print bitmask_string([1, 32])   # '0x80000001'
    if len(sys.argv) > 1:
        print is_chs(sys.argv[1])
