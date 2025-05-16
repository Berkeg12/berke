from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Post, Profile
from .forms import PostForm, ProfileForm

# Ana sayfa (opsiyonel)
def home(request):
    return render(request, 'core/home.html')

# Post listeleme (en yeni en üstte)
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/post_list.html', {'posts': posts})

# Post detayı
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'core/post_detail.html', {'post': post})

# Post oluşturma (sadece giriş yapan kullanıcı)
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'core/post_form.html', {'form': form})

# Post güncelleme (sadece sahibi düzenleyebilir)
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('post_list')
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'core/post_form.html', {'form': form})

# Post silme (sadece sahibi silebilir)
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('post_list')
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'core/post_confirm_delete.html', {'post': post})

# Profil görüntüleme
def profile_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'core/profile_detail.html', {'profile': profile})

# Kullanıcı kayıt (register)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

# Profil düzenleme (sadece giriş yapan kullanıcı)
@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/edit_profile.html', {'form': form})




