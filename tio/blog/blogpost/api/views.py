from blogpost.models import blog
from rest_framework.decorators import api_view
from blogpost.api.serializers import blogSerializers
from rest_framework.response import Response
@api_view(['GET','POST'])
def blog_posts(request):
    if request.method == 'GET': 
        blogs = blog.objects.all()
        serializer = blogSerializers(blogs, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = blogSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
@api_view()
def blog_post(request, pk):
    blogs = blog.objects.get(pk=pk)
    serializer = blogSerializers(blogs)
    return Response(serializer.data)
    
    