django-admin startproject webchat
cd webchat
python manage.py startapp chat

# webchat/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat',  # Afegir l'app
]

# Configuració de fitxers estàtics
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Configuració de mitjans (per imatges de perfil)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Missatge(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    editat = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['data']
    
    def __str__(self):
        return f"{self.usuari.username}: {self.text[:50]}"

class PerfilUsuari(models.Model):
    usuari = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    color = models.CharField(max_length=7, default='#007bff')
    
    def __str__(self):
        return self.usuari.username

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Missatge, PerfilUsuari

class RegistreForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MissatgeForm(forms.ModelForm):
    class Meta:
        model = Missatge
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Escriu el teu missatge...',
            })
        }
        labels = {
            'text': ''
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuari
        fields = ['avatar', 'bio', 'color']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'color': forms.TextInput(attrs={'type': 'color'}),
        }
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Missatge, PerfilUsuari
from .forms import RegistreForm, MissatgeForm, PerfilForm

def registre(request):
    if request.method == 'POST':
        form = RegistreForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear perfil automàticament
            PerfilUsuari.objects.create(usuari=user)
            login(request, user)
            messages.success(request, 'Registre completat amb èxit!')
            return redirect('chat')
    else:
        form = RegistreForm()
    return render(request, 'chat/registre.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')
        else:
            messages.error(request, 'Credencials incorrectes')
    return render(request, 'chat/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Sessió tancada correctament')
    return redirect('login')

@login_required
def chat(request):
    if request.method == 'POST':
        form = MissatgeForm(request.POST)
        if form.is_valid():
            missatge = form.save(commit=False)
            missatge.usuari = request.user
            missatge.save()
            return redirect('chat')
    else:
        form = MissatgeForm()
    
    missatges = Missatge.objects.all()
    return render(request, 'chat/chat.html', {
        'form': form,
        'missatges': missatges
    })

@login_required
def obtenir_missatges(request):
    """Vista AJAX per obtenir missatges nous"""
    ultim_id = request.GET.get('ultim_id', 0)
    missatges = Missatge.objects.filter(id__gt=ultim_id)
    
    data = []
    for m in missatges:
        data.append({
            'id': m.id,
            'usuari': m.usuari.username,
            'text': m.text,
            'data': m.data.strftime('%H:%M'),
            'color': getattr(m.usuari.perfilusuari, 'color', '#007bff'),
            'es_propi': m.usuari == request.user
        })
    
    return JsonResponse({'missatges': data})

@login_required
def editar_missatge(request, missatge_id):
    missatge = get_object_or_404(Missatge, id=missatge_id, usuari=request.user)
    
    if request.method == 'POST':
        nou_text = request.POST.get('text')
        if nou_text:
            missatge.text = nou_text
            missatge.editat = True
            missatge.save()
            messages.success(request, 'Missatge editat correctament')
        return redirect('chat')
    
    return render(request, 'chat/editar.html', {'missatge': missatge})

@login_required
def eliminar_missatge(request, missatge_id):
    missatge = get_object_or_404(Missatge, id=missatge_id, usuari=request.user)
    if request.method == 'POST':
        missatge.delete()
        messages.success(request, 'Missatge eliminat correctament')
    return redirect('chat')

@login_required
def perfil(request):
    perfil_obj, created = PerfilUsuari.objects.get_or_create(usuari=request.user)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualitzat correctament')
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil_obj)
    
    return render(request, 'chat/perfil.html', {'form': form})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('registre/', views.registre, name='registre'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('obtenir-missatges/', views.obtenir_missatges, name='obtenir_missatges'),
    path('editar/<int:missatge_id>/', views.editar_missatge, name='editar_missatge'),
    path('eliminar/<int:missatge_id>/', views.eliminar_missatge, name='eliminar_missatge'),
]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}WebChat{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .chat-container {
            max-width: 1200px;
            margin: 20px auto;
        }
        .missatge-propi {
            background-color: #dcf8c6;
            margin-left: auto;
        }
        .missatge-altres {
            background-color: #ffffff;
        }
    </style>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navbar -->
    {% if user.is_authenticated %}
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'chat' %}">
                <i class="bi bi-chat-dots"></i> WebChat
            </a>
            <div class="navbar-nav ms-auto">
                <span class="navbar-text me-3">
                    <i class="bi bi-person-circle"></i> {{ user.username }}
                </span>
                <a class="btn btn-outline-light btn-sm me-2" href="{% url 'perfil' %}">
                    <i class="bi bi-gear"></i> Perfil
                </a>
                <a class="btn btn-outline-danger btn-sm" href="{% url 'logout' %}">
                    <i class="bi bi-box-arrow-right"></i> Sortir
                </a>
            </div>
        </div>
    </nav>
    {% endif %}

    <!-- Missatges -->
    {% if messages %}
    <div class="container mt-3">
        {% for message in messages %}
        <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
        {% endfor %}
    </div>
    {% endif %}

    <!-- Contingut -->
    {% block content %}{% endblock %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
{% extends 'chat/base.html' %}

{% block title %}Registre - WebChat{% endblock %}

{% block content %}
<div class="container">
    <div class="row justify-content-center mt-5">
        <div class="col-md-6">
            <div class="card shadow">
                <div class="card-body p-5">
                    <h2 class="text-center mb-4">
                        <i class="bi bi-person-plus"></i> Registre
                    </h2>
                    <form method="post">
                        {% csrf_token %}
                        {% for field in form %}
                        <div class="mb-3">
                            <label class="form-label">{{ field.label }}</label>
                            {{ field }}
                            {% if field.errors %}
                                <div class="text-danger">{{ field.errors }}</div>
                            {% endif %}
                            {% if field.help_text %}
                                <small class="text-muted">{{ field.help_text }}</small>
                            {% endif %}
                        </div>
                        {% endfor %}
                        <button type="submit" class="btn btn-success w-100">
                            <i class="bi bi-check-circle"></i> Registrar-se
                        </button>
                    </form>
                    <hr>
                    <p class="text-center mb-0">
                        Ja tens compte? <a href="{% url 'login' %}">Inicia sessió</a>
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .form-control {
        margin-bottom: 5px;
    }
</style>
{% endblock %}
{% extends 'chat/base.html' %}

{% block title %}Chat - WebChat{% endblock %}

{% block extra_css %}
<style>
    .chat-box {
        height: 500px;
        overflow-y: auto;
        background-color: #e5ddd5;
        padding: 20px;
        border-radius: 10px;
    }
    .missatge {
        max-width: 70%;
        margin-bottom: 15px;
        padding: 10px 15px;
        border-radius: 10px;
        position: relative;
    }
    .missatge-propi {
        margin-left: auto;
        background-color: #dcf8c6;
    }
    .missatge-altres {
        background-color: #ffffff;
    }
    .missatge-usuari {
        font-weight: bold;
        margin-bottom: 5px;
    }
    .missatge-data {
        font-size: 0.75rem;
        color: #666;
        margin-top: 5px;
    }
    .missatge-accions {
        position: absolute;
        top: 5px;
        right: 5px;
    }
</style>
{% endblock %}

{% block content %}
<div class="container chat-container">
    <div class="card shadow-lg">
        <div class="card-header bg-primary text-white">
            <h4 class="mb-0">
                <i class="bi bi-chat-left-text"></i> Sala de Chat
                <span class="badge bg-light text-dark float-end" id="usuaris-online">
                    <i class="bi bi-people"></i> Online
                </span>
            </h4>
        </div>
        <div class="card-body p-0">
            <!-- Zona de missatges -->
            <div class="chat-box" id="chat-box">
                {% for missatge in missatges %}
                <div class="missatge {% if missatge.usuari == user %}missatge-propi{% else %}missatge-altres{% endif %}"
                     data-missatge-id="{{ missatge.id }}">
                    {% if missatge.usuari != user %}
                    <div class="missatge-usuari" style="color: {{ missatge.usuari.perfilusuari.color }}">
                        {{ missatge.usuari.username }}
                    </div>
                    {% endif %}
                    <div class="missatge-text">
                        {{ missatge.text }}
                        {% if missatge.editat %}
                        <small class="text-muted">(editat)</small>
                        {% endif %}
                    </div>
                    <div class="missatge-data">
                        {{ missatge.data|date:"H:i" }}
                    </div>
                    {% if missatge.usuari == user %}
                    <div class="missatge-accions">
                        <a href="{% url 'editar_missatge' missatge.id %}" class="btn btn-sm btn-outline-secondary">
                            <i class="bi bi-pencil"></i>
                        </a>
                        <form method="post" action="{% url 'eliminar_missatge' missatge.id %}" style="display:inline;">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-sm btn-outline-danger" onclick="return confirm('Segur que vols eliminar aquest missatge?')">
                                <i class="bi bi-trash"></i>
                            </button>
                        </form>
                    </div>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        </div>
        <div class="card-footer">
            <!-- Formulari per enviar missatges -->
            <form method="post" id="form-missatge">
                {% csrf_token %}
                <div class="input-group">
                    {{ form.text }}
                    <button type="submit" class="btn btn-primary">
                        <i class="bi bi-send"></i> Enviar
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script>
    // Auto-scroll al final
    function scrollToBottom() {
        const chatBox = document.getElementById('chat-box');
        chatBox.scrollTop = chatBox.scrollHeight;
    }
    
    // Scroll inicial
    scrollToBottom();
    
    // Actualització automàtica de missatges (polling)
    let ultimId = {{ missatges.last.id|default:0 }};
    
    function actualitzarMissatges() {
        fetch(`/obtenir-missatges/?ultim_id=${ultimId}`)
            .then(response => response.json())
            .then(data => {
                if (data.missatges.length > 0) {
                    const chatBox = document.getElementById('chat-box');
                    data.missatges.forEach(m => {
                        const div = document.createElement('div');
                        div.className = `missatge ${m.es_propi ? 'missatge-propi' : 'missatge-altres'}`;
                        div.dataset.missatgeId = m.id;
                        
                        let html = '';
                        if (!m.es_propi) {
                            html += `<div class="missatge-usuari" style="color: ${m.color}">${m.usuari}</div>`;
                        }
                        html += `<div class="missatge-text">${m.text}</div>`;
                        html += `<div class="missatge-data">${m.data}</div>`;
                        
                        div.innerHTML = html;
                        chatBox.appendChild(div);
                        ultimId = m.id;
                    });
                    scrollToBottom();
                }
            });
    }
    
    // Actualitzar cada 2 segons
    setInterval(actualitzarMissatges, 2000);
    
    // Enviar missatge amb AJAX (opcional)
    document.getElementById('form-missatge').addEventListener('submit', function(e) {
        scrollToBottom();
    });
</script>
{% endblock %}
{% extends 'chat/base.html' %}

{% block title %}Perfil - WebChat{% endblock %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card shadow">
                <div class="card-header bg-primary text-white">
                    <h4 class="mb-0">
                        <i class="bi bi-person-circle"></i> El Meu Perfil
                    </h4>
                </div>
                <div class="card-body">
                    <form method="post" enctype="multipart/form-data">
                        {% csrf_token %}
                        
                        <div class="row mb-3">
                            <div class="col-md-12">
                                <label class="form-label">Nom d'usuari</label>
                                <input type="text" class="form-control" value="{{ user.username }}" disabled>
                            </div>
                        </div>
                        
                        <div class="row mb-3">
                            <div class="col-md-12">
                                <label class="form-label">Email</label>
                                <input type="email" class="form-control" value="{{ user.email }}" disabled>
                            </div>
                        </div>
                        
                        {% for field in form %}
                        <div class="mb-3">
                            <label class="form-label">{{ field.label }}</label>
                            {{ field }}
                            {% if field.errors %}
                                <div class="text-danger">{{ field.errors }}</div>
                            {% endif %}
                        </div>
                        {% endfor %}
                        
                        <button type="submit" class="btn btn-success">
                            <i class="bi bi-check-circle"></i> Guardar Canvis
                        </button>
                        <a href="{% url 'chat' %}" class="btn btn-secondary">
                            <i class="bi bi-arrow-left"></i> Tornar al Chat
                        </a>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .form-control, .form-select {
        margin-bottom: 5px;
    }
</style>
{% endblock %}
{% extends 'chat/base.html' %}

{% block title %}Editar Missatge - WebChat{% endblock %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card shadow">
                <div class="card-header bg-warning">
                    <h4 class="mb-0">
                        <i class="bi bi-pencil"></i> Editar Missatge
                    </h4>
                </div>
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label class="form-label">Missatge</label>
                            <textarea name="text" class="form-control" rows="4" required>{{ missatge.text }}</textarea>
                        </div>
                        <button type="submit" class="btn btn-success">
                            <i class="bi bi-check-circle"></i> Guardar
                        </button>
                        <a href="{% url 'chat' %}" class="btn btn-secondary">
                            <i class="bi bi-x-circle"></i> Cancel·lar
                        </a>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}