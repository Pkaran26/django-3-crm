from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse
from django.shortcuts import render

class SimpleView(View):
    def get(self, request):
        context = {}
        context['book_list'] = Book.objects.all()
        return render(request, 'product/list.html', context)

    # def post(self, request):
        ...  # code to process a POST request

class BookListTemplateView(TemplateView):
    template_name = 'product/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    # queryset = Book.objects.all()
    template_name = 'product/list.html'

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'product/detail.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'price']
    template_name = 'product/form.html'

    def get_success_url(self):
        return reverse('book_list')
        # return reverse('lawyer_detail', kwargs={'lawyer_slug': self.object.lawyer_slug})

class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'price']
    template_name = 'product/form.html'

    def get_success_url(self):
        return reverse('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'product/delete.html'

    def get_success_url(self):
        return reverse('book_list')
