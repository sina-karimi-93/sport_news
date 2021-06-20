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


def bim_suggestion(bmi):
    """
    Get the bmi and suggest a Diet.
    """
    suggestion = {
        bmi < 18.5: """رژیم غذایی مناسب برای تیپ بدنی کمتر از ۱۸/۵، شامل ۵۵٪ کربوهیدرات، ۲۵٪ پروتئین و ۲۰٪ چربی است. 

غذاهای توصیه شده
اگر متعلق به این گروه هستید، مواد غذایی زیر را در رژیم غذایی خود بگنجانید:

گوشت و مرغ
سبزیجات
شیر و تخم مرغ
انواع دانه‌های روغنی و آجیل
غلات کامل
نان و ماکارونی""",
        all([bmi > 18.5, bmi < 24.9]): """رژیم غذایی مناسب برای تیپ بدنی ۱۸/۵ الی ۲۴ شامل ۴۰٪ کربوهیدرات، ۳۰٪ پروتئین و ۳۰٪ چربی است. 

غذاهای توصیه شده

اگر متعلق به این گروه هستید، مواد غذایی زیر را در رژیم غذایی خود بگنجانید:

روغن‌های سالم مانند روغن زیتون و ذرت
میوه و سبزیجات فراوان
غلات
گوشت و ماهی بدون چربی و سویا
غذاهای سرشار از سدیم و کلسیم""",
        all([bmi > 25, bmi < 29.9]): """افراد با تیپ بدنی ۲۵ تا ۲۹، باید مصرف کربوهیدرات‌ها به ویژه مواد غذایی مانند نان، ماکارونی، آبمیوه‌های صنعتی و غلات را محدودتر کنند و در هنگام مصرف چربی حساسیت بالایی به خرج دهند.

تاکید اصلی برای افراد دارای اندام گلابی شکل، تلاش برای عضله‌سازی و حفظ وزن ایده‌آل بدن است. بهترین راه برای انجام این کار، مصرف پروتئین‌های کم‌چرب، سبزیجات و چربی‌های سالم است""",
        bmi > 30: """غذاهایی که افراد با این تیپ بدنی باید بخورند:

 غذاهای حاوی فیبر، حبوبات و کربوهیدرات‌های ساده از مواردی هستند که باید در برنامه غذایی این افراد گنجانده شوند. این مواد غذایی سبب حفظ انرژی بدن در مدت زمان طولانی می‌شوند. همچنین مصرف جو، برنج قهوه‌ای، عدس، لوبیا و سیب زمینی به این افراد توصیه می‌شود.

غذاهایی که افراد با این تیپ بدنی باید از آن‌ها اجتناب کنند:

افراد این دسته باید در مورد انواع چربی که مصرف می کنند، هوشیار باشند و چربی‌های ناسالم یا حیوانی استفاده نکنند. همچنین مصرف پنیر، خامه، کره، روغن کانولا و دانه‌های روغنی و آجیل در این افراد باید محدودتر شود""",
    }

    return suggestion[True]


def calculate_bmi(request):
    if request.method == 'POST':
        form = BMIForm(request.POST or None)
        if form.is_valid():
            height_cm = form.cleaned_data['height']
            weight_kg = form.cleaned_data['weight']

            height_metric = height_cm * 0.01
            bmi = round((weight_kg / (height_metric * height_metric)), 2)
            values = 'بی ام آی شما عدد ' + str(bmi) + ' می باشد'
            suggestion = bim_suggestion(bmi=bmi)
            context = {
                'form': form,
                'answer': values,
                'suggestion': suggestion
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
