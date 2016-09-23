from django.shortcuts import render
from .models import Post, BlogCategory, BlogTag


def blog(request, author_id=None, cat_id=None, tag_id=None):
    blogs = Post.objects.filter(post_type='blog').order_by('date_created')
    if author_id is not None:
        blogs = blogs.filter(author_id=author_id)
    elif cat_id is not None:
        blogs = blogs.filter(category=cat_id)
    elif tag_id is not None:
        blogs = blogs.filter(tag=tag_id)

    context = {
        'blogs': blogs[:20],
    }
    cat_tag_context = get_cats_tags()
    context = {**context, **cat_tag_context}  # new in python3.5. add two dict
    return render(request, 'blog/blog.html', context)


def blog_single(request, post_id):
    blog = Post.objects.get(id=post_id)
    recent_blogs = Post.objects.filter(post_type='blog').order_by('date_created')[:10]
    context = {
        'blog': blog,
        'recent_blogs':recent_blogs,
    }
    cat_tag_context = get_cats_tags()
    context = {**context, **cat_tag_context}  # new in python3.5. add two dict
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
