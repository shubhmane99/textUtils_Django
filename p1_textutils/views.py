from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'shubham'}
    return render(request, 'index.html',params)
    # return HttpResponse("Home")



def analyze(request):
    # get the input text
    djtext = request.GET.get('text','default')

    # check checkbox value
    removepunc = request.GET.get('removepunc','off')

    # check full caps value 
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    
    punctuations = '''!()-[]{};:'\,<>./?@#$%^&*_~'''
    analyzed = ""
    # check which checkbox is on
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)

    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose':'Changed to uppercase ','analyzed_text':analyzed}

        return render(request, 'analyze.html',params)

    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char.upper()
        
            
        params = {'purpose':'remove newline','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    else:
        return HttpResponse("Error")

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')
# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("new line remove")


# def spaceremoval(request):
#     return HttpResponse("space")

# def charcount(request):
#     return HttpResponse("charcount")