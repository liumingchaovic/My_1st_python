# -*- coding: cp936 -*-
# wordstats.py
# ��������Ҫ�������ַ��ļ���
keep = {'a', 'b', 'c', 'd', 'e',
        'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y',
        'z', ' ', '-', "'"}
def normalize(s):
    '''convert s to a normal string.'''
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
    return result
def make_freq_dict(s):
    '''Returns a dictionary whose keys are the words of s, and whose values
    are the counts of those words.'''
    s = normalize(s)
    words = s.split()
    d = {}
    for w in words:
        if w in d:
            d[w] += 1  #���w���ֹ����ͽ�����ִ�����1
        else:
            d[w] = 1   #���w��һ�γ��֣��ͽ�����ִ�������Ϊ1
    return d

def print_file_stats(fname):
    '''print statistics for the given file.'''
    s = open(fname, 'r').read()
    num_chars = len(s)         #�ڹ淶��s֮ǰ�����ַ���
    num_lines = s.count('\n')  #�ڹ淶��s֮ǰ��������

    d = make_freq_dict(s)
    num_words = sum(d[w] for w in d)  #����s�������ٸ�����

    #����һ���б����е�Ԫ���ɳ��ִ����͵�����ɵ�Ԫ��
    #�������ִ����Ӹߵ�������
    lst = [(d[w], w) for w in d]
    lst.sort()
    lst.reverse()

    #����Ļ�ϴ�ӡ���
    print("The file '%s' has :" %fname)
    print(" %s characters" %num_chars)
    print(" %s lines" %num_lines)
    print(" %s words" %num_words)

    print("\nThe top 10 most frequent words are:")
    i = 1
    for count, word in lst[:10]:
        print('%2s. %4s %s' %(i, count, word))
        i += 1

def main():
    print_file_stats('wordstats.txt')

if __name__ == '__main__':
    main()
