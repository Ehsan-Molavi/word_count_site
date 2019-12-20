from django.shortcuts import render
import string

def home(request):
    return render(request, 'home.html')


def count(request):
    text = request.GET['fulltext']
    l = []
    for letter in text.lower():
        if letter not in string.punctuation:
            l.append(letter)
        else:
            continue

    l = ''.join(l)
    words = l.split()
    words_num = {}
    for w in words:
        if w in words_num.keys():
            words_num[w] += 1
        else:
            words_num[w] = 1

    d = {'fulltext':text, 'words':words, 'count':len(words), 'words_num':sorted(words_num.items(), reverse=True, key=lambda item: item[1])}
    return render(request, 'count.html', d)