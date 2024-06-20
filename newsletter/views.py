# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm
from .mailchimp import add_email_to_list
from .email_utils import send_subscription_email


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            response = add_email_to_list(email)
            if response and "error" not in response:
                send_subscription_email(email)
                messages.success(request, 'You have successfully signed up for the newsletter.')
            else:
                error_message = response.get("error", "An unknown error occurred. Please try again.")
                messages.error(request, error_message)
            return redirect('newsletter_signup')
    else:
        form = NewsletterSignupForm()
    return render(request, 'newsletter/newsletter_signup.html', {'form': form})
