import random
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    varGold = request.session.get('gold')

    context = {
        'gold': varGold
    }
    return render(request, 'index.html', context)

def process_money(request):
    if request.POST['gold_value'] == 'farm':
        request.session['gold'] += random.randint(10,20)
    if request.POST['gold_value'] == 'cave':
        request.session['gold'] += random.randint(5,10)
    if request.POST['gold_value'] == 'house':
        request.session['gold'] += random.randint(2,5)
    if request.POST['gold_value'] == 'casino':
        request.session['gold'] += random.randint(-50,50)
    return redirect("/")