from django.shortcuts import render, get_object_or_404
from .models import Post, Comments
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def blog(request):

    posts = Post.objects.all()

    if 'search_btn' in request.GET:
        search_btn = request.GET['search_btn']
        if search_btn:
            posts = posts.filter(name__icontains=search_btn)

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {'posts': paged_posts}

    return render(request, 'blog.html', context)


def blog_details(request, post_id=2):

    if 'search_btn' in request.GET:
        search_btn = request.GET['search_btn']
        posts = Post.objects.all()
        if search_btn:
            posts = posts.filter(name__icontains=search_btn)
            return render(request, 'blog.html', {'posts': posts})

    post = get_object_or_404(Post, pk=post_id)
    comments = Comments.objects.filter(post_id=post_id)

    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'single-blog.html', context)
