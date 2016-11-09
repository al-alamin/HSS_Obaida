from django.shortcuts import render
from .models import Post, BlogCategory, BlogTag


def blog(request, author_id=None, cat_id=None, tag_id=None, video=False):
    if video:
        blogs = Post.objects.filter(post_type='blog', video_url__isnull=False)
    else:
        blogs = Post.objects.filter(post_type='blog')
    if author_id is not None:
        blogs = blogs.filter(author_id=author_id)
    elif cat_id is not None:
        blogs = blogs.filter(category=cat_id)
    elif tag_id is not None:
        blogs = blogs.filter(tag=tag_id)

    context = {
        'blogs': blogs.order_by('-date_created')[:20],
    }
    # combine two dictionaries, there is a shorter way in python 3.5
    for key, value in get_cats_tags().items():
        context[key] = value

    return render(request, 'blog/blog.html', context)


def blog_single(request, post_id):
    blog = Post.objects.get(id=post_id)
    recent_blogs = Post.objects.filter(post_type='blog').order_by('-date_created')[:10]
    context = {
        'blog': blog,
        'recent_blogs': recent_blogs,
    }
    # combine two dictionaries, there is a shorter way in python 3.5
    for key, value in get_cats_tags().items():
        context[key] = value
    return render(request, 'blog/blog_single.html', context)


def get_cats_tags():
    """
    helper function for views. To avoid duplication of code in blog and blog_single views
    :return: dictionary
    """
    cats = BlogCategory.objects.all()
    tags = BlogTag.objects.all()
    context = {
        'cats': cats,
        'tags': tags,
    }
    return context
