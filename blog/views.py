from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.mail import EmailMessage
from django.utils import timezone
from .models import Post, Type, Curso
from .forms import ContactForm

def base(request):
    cursos = Curso.objects.all()
    tags = Type.objects.all()
    return render(request, 'blog/base.html', {'tags': tags, 'cursos': cursos})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def body(request):
    cursos = Curso.objects.all()
    posts = Post.objects.all()
    return render(request, 'blog/body.html', {'posts': posts, 'cursos': cursos})

def post_list(request):
    tags = Type.objects.all()
    cursos = Curso.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')[:3]
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            email = EmailMessage('Mensagem de contato do site ' + contact.name,
            'Nome: '+ contact.name +
            '\n Telefone: '+ contact.phone_number +
            '\n E-mail: ' + contact.email +
            '\n Mensagem: ' + contact.message, to=[contact.email])
            email.send()
            contact.save()
            return redirect('root_url')
    else:
        form = ContactForm()
    return render(request, 'blog/index.html', {'posts': posts, 'tags': tags, 'form': form, 'cursos': cursos })

def post_by_type(request, pk):
    type = Type.objects.get(pk=pk)
    posts = get_list_or_404(Post, type_post=type)
    return render(request, 'blog/post_filter.html', {'posts': posts, 'tag': type })

def contact(request):
    form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form })
