from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SupportMessageForm
from .models import SupportMessage

@login_required
def support_view(request):
    if request.method == 'POST':
        form = SupportMessageForm(request.POST)
        if form.is_valid():
            support_msg = form.save(commit=False)
            support_msg.user = request.user
            support_msg.save()
            return redirect('support_thankyou')
    else:
        form = SupportMessageForm()

    return render(request, 'support/support_form.html', {'form': form})

@login_required
def support_thankyou(request):
    return render(request, 'support/support_thankyou.html')

@login_required
def support_messages_view(request):
    messages = SupportMessage.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'support/support_messages.html', {'messages': messages})
