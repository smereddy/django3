from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Comment, Client, Vehicles
from django.urls import reverse_lazy


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'

    def get_queryset(self):
        return Client.objects.filter(author=self.request.user)

    # def get_context_data(self, **kwargs):
    #     context = super(ClientListView, self).get_context_data(**kwargs)
    #     context['object_list'] = Client.objects.filter(author=self.request.user)
    #     return context




class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ('comment',)
    success_url = reverse_lazy('client_list')
    template_name = 'comments/edit.html'


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comments/delete.html'
    success_url = reverse_lazy('client_list')


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comments/create.html'
    fields = ('comment',)
    success_url = reverse_lazy('client_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.client_id = self.kwargs["client_id"]
        form.instance.author = self.request.user
        return super().form_valid(form)


class VehiclesListView(LoginRequiredMixin, ListView):
    model = Vehicles
    template_name = 'vehicles/list.html'


class VehiclesUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicles
    success_url = reverse_lazy('client_list')
    fields = ('make', 'model', 'VIN', 'last_service_date', 'date_of_purchase',)
    template_name = 'vehicles/edit.html'


class VehiclesDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicles
    template_name = 'vehicles/delete.html'
    success_url = reverse_lazy('client_list')


class VehiclesCreateView(LoginRequiredMixin, CreateView):
    model = Vehicles
    template_name = 'vehicles/create.html'
    success_url = reverse_lazy('client_list')
    fields = ('make', 'model', 'VIN', 'last_service_date', 'date_of_purchase',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.client_id = self.kwargs["client_id"]
        return super().form_valid(form)
