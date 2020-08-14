from django.shortcuts import render
from board.models import Post


def board_main_list(request):
    main_list = Post.objects.all().order_by('-id')
    context = {'posts': main_list }
    return render(request, 'main_list.html', context)


def board_create(request):

    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('stock:board_main_list')


    else:
        post_form = PostForm()

    return render(request, 'board_create.html', {'post_form': post_form})

