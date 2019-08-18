from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def post_rota(request):
    return render(request, 'blog/post_rota.html', {})
