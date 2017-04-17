from django.shortcuts import render, redirect
import md5
import random
def index(request):
    return render(request, "index/index.html")
def users(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    # print request.session['count']
    request.session['random_words'] = md5.new(str(random.randint(0,10))).hexdigest()
    print request.session['random_words']
    return redirect('/')
# Create your views here.
