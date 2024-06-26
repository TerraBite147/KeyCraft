from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import FAQ
from .forms import FAQForm


def faq_list_view(request):
    faqs = FAQ.objects.all()
    return render(request, "faq/faq_list.html", {"faqs": faqs})


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def add_faq_view(request):
    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQ added successfully!")
            return redirect("faq_list")
        else:
            messages.error(
                request, "There was an error adding the FAQ. Please try again."
            )
    else:
        form = FAQForm()

    return render(request, "faq/add_faq.html", {"form": form})


@user_passes_test(is_admin)
def edit_faq_view(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    if request.method == "POST":
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQ updated successfully!")
            return redirect("faq_list")
        else:
            messages.error(
                request, "There was an error updating the FAQ. Please try again."
            )
    else:
        form = FAQForm(instance=faq)

    return render(request, "faq/edit_faq.html", {"form": form})


@user_passes_test(is_admin)
def delete_faq_view(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    if request.method == "POST":
        faq.delete()
        messages.success(request, "FAQ deleted successfully!")
        return redirect("faq_list")
    return render(request, "faq/delete_faq.html", {"faq": faq})
