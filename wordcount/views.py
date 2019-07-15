from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()

    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedword = sorted(worddict.items(),key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedword':sortedword})

def insync(request):
    return render(request,'insync.html')

def about(request):
    return render(request,'about.html')

def career(request):
    return HttpResponse(' <h1 style="border:4px solid blue;">Career page is here here</h1>')