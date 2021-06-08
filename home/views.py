from django.shortcuts import render, get_object_or_404, redirect
from .models import News, ContactUs
from django.core.paginator import Paginator
from .forms import BMIForm, ContactUsForm


# Create your views here.


def news_list(request):
    news = News.objects.get_active_news()
    last_five_news = news[0:5]

    paginator = Paginator(news, 6)  # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "news": news,
        "last_news": last_five_news,
        "page_obj": page_obj
    }

    return render(request, 'news_list.html', context)


def news_detail(request, slug):
    single_news = get_object_or_404(News, slug=slug)
    context = {
        'single_news': single_news
    }

    return render(request, 'news_detail.html', context)


def calculate_bmi(request):
    if request.method == 'POST':
        form = BMIForm(request.POST or None)
        if form.is_valid():
            height_cm = form.cleaned_data['height']
            weight_kg = form.cleaned_data['weight']

            height_metric = height_cm * 0.01
            bmi = round((weight_kg / (height_metric * height_metric)), 2)
            values = 'بی ام آی شما عدد ' + str(bmi) + ' می باشد'
            context = {
                'form': form,
                'answer': values
            }

            return render(request, 'calculate_bmi.html', context)
    form = BMIForm()
    print(form)
    context = {
        'form': form,
        'answer': None
    }
    return render(request, 'calculate_bmi.html', context)


def contact_us(request):
    if request.method == 'POST':
        print(100000)
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            print(200000)
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            ContactUs.objects.create(
                title=title,
                description=description,
                email=email,
                phone_number=phone_number)
            print(300000)
            return redirect('/')
    print(400000)
    form = ContactUsForm()
    context = {
        "form": form
    }
    return render(request, 'contact_us.html', context)
