from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TableBooking, Dish, Comment
from .forms import TableBookingForm, CommentsForm


@login_required
def main(request):
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
        if Comment.objects.filter(email=email):
            return render(request, 'main.html', {'form': form})
        else:
            comment = Comment(email=email, text=text)
            comment.save()
            return render(request, 'main.html', {'form': form})
    else:
        form = CommentsForm(initial={'email': request.user.email})
        return render(request, 'main.html', {'form': form})


@login_required
def book_table(request):
    if request.method == "POST":
        form = TableBookingForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            table_number = form.cleaned_data['table_number']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            if TableBooking.objects.filter(table_number=table_number).exists():
                return render(request, 'brone.html', {'form': form})
            else:
                booking = TableBooking(email=email, table_number=table_number, date=date, time=time)
                booking.save()
                return redirect('/main/')
    else:
        print(request.user.email)
        form = TableBookingForm(initial={'email': request.user.email})
    return render(request, 'brone.html', {'form': form})


@login_required
def menu(request):
    dishs = Dish.objects.all()
    first = []
    second = []
    salats = []
    napoys = []
    anothers = []
    for dish in dishs:
        if dish.group == 'first':
            first = first + [dish]
        if dish.group == 'second':
            second = second + [dish]
        if dish.group == 'salat':
            salats = salats + [dish]
        if dish.group == 'napoy':
            napoys = napoys + [dish]
        else:
            anothers = anothers + [dish]
    return render(request, 'menu.html', {'firsts': first, 'seconds': second, 'salats': salats, 'napoys': napoys, 'anothers': anothers})
