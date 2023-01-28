from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from youtubesearchpython import VideosSearch


def index(request):
    if request.method == "POST":
        search = request.POST.get("search", None)
        if search:
            return redirect(video, search=search)
    return render(request, "index.html")


def video(request, search):
    if search:
        videosSearch = VideosSearch(search, limit=1)
        data = videosSearch.result()["result"][0]
        if data:
            context = {"id": data["id"]}
            return render(request, "video.html", context)
        else:
            return redirect(index)
    else:
        return redirect(index)
