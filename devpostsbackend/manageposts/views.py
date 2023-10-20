from django.http import HttpResponse

# Create your views here.
def get_all_devposts(request):
    # Obtiene todos los posts del archivo 'posts.json' y los expone al frontend
    return HttpResponse("Hi, This is a posts ;)")


def get_posts_from_scraper(request):
    # Obtiene el archivo 'posts.json' del scraper
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        print(request.method)
    return HttpResponse("Get posts from scraper")