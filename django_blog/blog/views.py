from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'base.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'base.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = usercreationform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': 'Account created successfully'})
    else:
        form = usercreationform()
    return render(request, 'register.html', {'form': form})


# CRUD Views for blog posts    

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return render(request, 'login.html', {'error': 'You must be logged in to view this page'})

def ListView(request):
    return HttpResponse("This is the list view")

def DetailView(request, pk):
    return HttpResponse(f"This is the detail view for item {pk}")

def CreateView(request):
    return HttpResponse("This is the create view")

def UpdateView(request, pk):
    return HttpResponse(f"This is the update view for item {pk}")

def DeleteView(request, pk):
    return HttpResponse(f"This is the delete view for item {pk}")


# use LoginRequiredMixin and UserPassesTestMixin for author edit and delete views
class AuthorEditView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        # Implement your logic to check if the user is the author
        return True

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is the author edit view")

class AuthorDeleteView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        # Implement your logic to check if the user is the author
        return True

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is the author delete view")

# Comment Views
@login_required
def CommentCreateView(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'post': post})

@login_required
def CommentUpdateView(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return HttpResponse("You are not authorized to edit this comment.")
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

@login_required
def CommentDeleteView(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return HttpResponse("You are not authorized to delete this comment.")
    if request.method == 'POST':
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)
    return render(request, 'delete_comment.html', {'comment': comment})
