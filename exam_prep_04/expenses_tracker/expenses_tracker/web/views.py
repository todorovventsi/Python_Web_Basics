from django.shortcuts import render, redirect

from expenses_tracker.web.forms import ProfileCreateForm, ExpenseCreateForm, ExpenseEditForm, ExpenseDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from expenses_tracker.web.models import Profile, Expense


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def index(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    total_spending = sum([e.price for e in expenses])
    if not profile:
        return redirect('create profile')

    budget_left = profile.budget - total_spending

    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def expense_create(request):
    if request.method == 'POST':
        form = ExpenseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ExpenseCreateForm()

    context = {
        'form': form
    }

    return render(request, 'expense-create.html', context)


def expense_edit(request, pk):

    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = ExpenseEditForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ExpenseEditForm(instance=expense)

    context = {
        'form': form
    }

    return render(request, 'expense-edit.html', context)


def expense_delete(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = ExpenseDeleteForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ExpenseDeleteForm(instance=expense)

    context = {
        'form': form,
    }

    return render(request, 'expense-delete.html', context)


def profile_details(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    total_expenses = len(expenses)
    budget_left = profile.budget - sum([e.price for e in expenses])

    context = {
        'profile': profile,
        'total_expenses': total_expenses,
        'budget_left': budget_left
    }

    return render(request, 'profile.html', context)


def profile_create(request):

    if request.method == 'POST':
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'home-no-profile.html', context)


def profile_edit(request, pk):
    profile = get_profile()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def profile_delete(request, pk):
    profile = get_profile()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)
