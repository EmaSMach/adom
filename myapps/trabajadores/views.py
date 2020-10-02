from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from myapps.trabajadores.models import Post, Comentario
from myapps.trabajadores.forms import posteoForm
from .forms import posteoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "trabajadores/trabajadores.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "trabajadores/detalles.html"

@login_required
def postear_oferta(request):
    #author = request.user
    form = posteoForm()
    if request.method == "POST":
        form = posteoForm(request.POST, request.FILES)
        #formset = OfertaInlineFormSet(request.POST, request.FILES)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.autor = request.user
            oferta.save()
            #imagenes = formset.save(commit=False)
            
            return redirect('detalles_post', oferta.id)
    
    return render(request, 'trabajadores/crear.html', {'form': form})



class PostCreateView(CreateView):
    model = Post
    template_name = "trabajadores/crear.html"

    form_class = posteoForm
    #success_url  =  "trabajadores"
    success_url = reverse_lazy('trabajadores')



class PostUpdateView(UpdateView):
    model = Post
    template_name = "trabajadores/editar.html"

    form_class = posteoForm
    #success_url  =  "trabajadores"
    success_url = reverse_lazy('trabajadores')
