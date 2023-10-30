from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .models import Todo
# Create your views here.
User = get_user_model()
# class HomeView(View):
#     template_name = 'home.html'
#     context = {}
#
#     def get(self, request):
#         return render(request, self.template_name)


def home(request):
    return render(request, 'home.html')


def todo(request):
    return render(request, 'todo.html')


class HomeView(View):
    template_name = 'home.html'
    context = {}

    def get(self, request):
        todos = Todo.objects.filter(owner=request.user)
        self.context.update({"todos": todos})
        return render(request, self.template_name, context=self.context)


class TodoView(View):
    template_name = 'todo.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        service_id = request.POST.get('service_id')
        if request.user is None:
            return redirect('/login')
        user = request.user
        if not Todo.objects.filter(Q(owner=user)).exists():
            todo = Todo.objects.create(
                owner=user,
                text=request.POST.get('text'),
            )
            todo.save()
            messages.info(request, 'Todo added successfully')
            return redirect('/')
        return redirect('/')
