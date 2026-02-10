from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Wallet
from .forms import WalletForm

@login_required
def wallet_list(request):
    wallets = Wallet.objects.filter(user=request.user)
    return render(request, 'wallet/wallet_list.html', {'wallets': wallets})

@login_required
def wallet_create(request):
    if request.method == 'POST':
        form = WalletForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.user = request.user
            wallet.save()
            return redirect('wallet_list')
        else:
            print(form.errors)
    else:
        form = WalletForm()
    return render(request, 'wallet/wallet_form.html', {'form': form})

@login_required
def wallet_update(request, pk):
    wallet = get_object_or_404(Wallet, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WalletForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect('wallet_list')
    else:
        form = WalletForm(instance=wallet)
    return render(request, 'wallet/wallet_form.html', {'form': form})

@login_required
def wallet_delete(request, pk):
    wallet = get_object_or_404(Wallet, pk=pk, user=request.user)
    if request.method == 'POST':
        wallet.delete()
        return redirect('wallet_list')
    return render(request, 'wallet/wallet_confirm_delete.html', {'wallet': wallet})
