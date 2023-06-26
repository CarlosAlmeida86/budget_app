from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Transaction

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'budget/transaction_list.html', {'transactions': transactions})

def add_transaction(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = float(request.POST.get('amount'))
        category = request.POST.get('category')
        date = request.POST.get('date')

        transaction = Transaction(title=title, amount=amount, category=category, date=date)
        transaction.save()
        return redirect('transaction_list')
    return render(request, 'budget/add_transaction.html')

