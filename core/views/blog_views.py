from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import BlogPost
from core.utils.helpers import parse_json, handle_image_upload

@csrf_exempt
def blog_list(request):
    """Handles GET and POST requests for blog posts."""
    if request.method == 'GET':
        posts = BlogPost.objects.all()
        data = [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'author': post.author,
                'published_at': post.published_at,
                'image_url': post.image.url if post.image else None,
            }
            for post in posts
        ]
        return JsonResponse({'blogs': data})
    elif request.method == 'POST':
        data = parse_json(request)
        image_data = data.get('image')
        image_file = handle_image_upload(image_data, "blog_image.jpg")
        blog = BlogPost.objects.create(
            title=data.get('title'),
            content=data.get('content'),
            author=data.get('author'),
            image=image_file
        )
        return JsonResponse({'message': 'Blog created successfully', 'id': blog.id})

@csrf_exempt
def blog_detail(request, blog_id):
    """Handles GET, PUT, and DELETE requests for a specific blog post."""
    blog = get_object_or_404(BlogPost, id=blog_id)
    if request.method == 'GET':
        data = {
            'id': blog.id,
            'title': blog.title,
            'content': blog.content,
            'author': blog.author,
            'published_at': blog.published_at,
            'image_url': blog.image.url if blog.image else None,
        }
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = parse_json(request)
        blog.title = data.get('title', blog.title)
        blog.content = data.get('content', blog.content)
        blog.author = data.get('author', blog.author)
        blog.save()
        return JsonResponse({'message': 'Blog updated successfully'})
    elif request.method == 'DELETE':
        blog.delete()
        return JsonResponse({'message': 'Blog deleted successfully'})
