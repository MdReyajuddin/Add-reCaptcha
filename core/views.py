import requests

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from forms import CommentForm
from .models import Comment


# Create your views here.
def comments(request):
    comments_list= Comment.objects.order_by('-created_at')

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            captcha_response = request.POST.get['g-recaptcha-response']
            data={
                'secret': '6LcdyuAUAAAAAGtSgh1HroDq1k6SMMHjX0g8AJ9c',
                'response': captcha_response
                }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            if result['success']:
                form.save()
                messages.success(request, 'New comment added with success!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('comments')
    else:
        form=CommentForm()

    return render(request, 'comments.html', {'form': form, 'comments': comments_list})