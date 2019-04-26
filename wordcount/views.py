from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    texto = request.GET['fulltext']
    wordCount = texto.split()
    wordDict = {}
    for x in wordCount:
        if x in wordDict:
            wordDict[x] += 1
        else:
            wordDict[x] = 1
    def getKey(item):
        item[0]
    sortedDict = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'texto': texto, 'cuenta': len(wordCount), "sortedDict": sortedDict})

def about(request):
    return render(request, 'about.html')
