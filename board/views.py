from django.shortcuts import render, redirect, get_object_or_404
from board.models import Post, Comment
from board.forms import PostForm,CommentForm
import xml.etree.ElementTree as ET
import requests
from board import GetStockCode
from django.core.paginator import Paginator
from django.db.models import Q
from stock.models import User




## 원본 ##
# def board_main_list(request):
#
#     companyNamedict= GetStockCode.Get_CSV_Maching_dict()
#     print("bbbbbbb")
#     companyName=request.POST.get('machingstock')
#
#     # 종목 서치할 수 있게
#     if companyName != None:
#         print(companyName)
#         xmldict=GetStockCode.Get_XML_maching_dict()
#         corpcode=xmldict[companyName]
#         print(corpcode)
#
#         choice_list = Post.objects.filter(maching_code__contains=corpcode).order_by('-id')
#         context = {'posts': choice_list,'companydict':companyNamedict,'corpcode': corpcode, 'ChoicCodeName':companyName }
#
#     else:
#         print('선택한 종목이 없습니다')
#         main_list = Post.objects.all().order_by('-id')
#         context = {'posts': main_list,'companydict':companyNamedict }
#
#     return render(request, 'bbs.html', context)





### 원본 ###
#
# def board_main_list(request):
#     companyNamedict = GetStockCode.Get_CSV_Maching_dict()
#     print("bbbbbbb")
#     companyName = request.POST.get('machingstock')
#
#
#     # 회사이름으로 필터 (None이 아닐 경우)
#     if companyName != None:
#         print('회사이름'+companyName)
#         xmldict = GetStockCode.Get_XML_maching_dict()
#
#
#         if companyName =="":
#             print('선택한 종목이 없습니다')
#             main_list = Post.objects.all().order_by('-id')
#             print(main_list)
#             paginator = Paginator(main_list,5)
#             page = request.GET.get('page')
#             bbspage = paginator.get_page(page)
#             context = {'posts': main_list, 'companydict': companyNamedict, 'bbspage': bbspage}
#
#         else:
#             corpcode = xmldict[companyName]
#             print('회사코드'+corpcode)
#
#             choice_list = Post.objects.filter(maching_code__contains=corpcode).order_by('-id')
#             paginator = Paginator(choice_list,5)
#             page = request.GET.get('page')
#             bbspage = paginator.get_page(page)
#             context = {'posts': choice_list, 'companydict': companyNamedict, 'corpcode': corpcode,
#                        'ChoicCodeName': companyName, 'bbspage': bbspage}
#
#
#     else:
#         print('선택한 종목이 없습니다')
#         main_list = Post.objects.all().order_by('-id')
#         paginator = Paginator(main_list, 10)
#         page = request.GET.get('page')
#         bbspage = paginator.get_page(page)
#         context = {'posts': main_list, 'companydict': companyNamedict, 'bbspage': bbspage}
#
#     return render(request, 'bbs.html', context)




## 테스트 ##

def board_main_list(request):
    companyNamedict = GetStockCode.Get_CSV_Maching_dict()
    user_name = request.session['userss']
    user_id = request.session['user_id']
    kw = request.GET.get('search_key', '')
    print(kw)


    companyName = request.POST.get('machingstock')

    # 회사이름으로 필터 (None이 아닐 경우)
    if companyName != None:

        print('회사이름'+companyName)
        xmldict = GetStockCode.Get_XML_maching_dict()

        if kw != None:
            print('3들어')
            main_list = Post.objects.all().order_by('-id')
            post = main_list.filter(
                Q(title__icontains=kw) |
                Q(contents__icontains=kw)
                # Q(author__username__icontain=kw)
            ).distinct()
            paginator = Paginator(post, 10)
            page = request.GET.get('page')
            bbspage = paginator.get_page(page)
            context = {'posts': post, 'companydict': companyNamedict, 'bbspage': bbspage}

        if companyName == '':
            print('선택한 종목이 없습니다')
            main_list = Post.objects.all().order_by('-id')
            paginator = Paginator(main_list, 10)
            page = request.GET.get('page')
            bbspage = paginator.get_page(page)
            context = {'posts': main_list, 'companydict': companyNamedict, 'bbspage': bbspage, 'userss': user_name, 'user_id': user_id}



        else:
            corpcode = xmldict[companyName]
            print('회사코드'+corpcode)

            choice_list = Post.objects.filter(maching_code__contains=corpcode).order_by('-id')
           # kw = Post.objects.filter(maching_code__contains=corpcode).order_by('-id')
            paginator = Paginator(choice_list, 10)
            page = request.GET.get('page')
            bbspage = paginator.get_page(page)
            context = {'posts': choice_list, 'companydict': companyNamedict, 'corpcode': corpcode,
                       'ChoicCodeName': companyName, 'bbspage': bbspage, 'userss': user_name, 'user_id': user_id}

            if kw != None:
                print('2들어옴')
                post = choice_list.filter(
                    Q(title__icontains=kw) |
                    Q(contents__icontains=kw)
                    # Q(author__username__icontain=kw)
                ).distinct()
                paginator = Paginator(post, 10)
                page = request.GET.get('page')
                bbspage = paginator.get_page(page)
                context = {'posts': choice_list, 'companydict': companyNamedict, 'corpcode': corpcode,
                           'ChoicCodeName': companyName, 'bbspage': bbspage, 'userss': user_name, 'user_id': user_id}



    else:
        print('선택한 종목이 없습니다')
        main_list = Post.objects.all().order_by('-id')

        paginator = Paginator(main_list, 10)
        page = request.GET.get('page')
        bbspage = paginator.get_page(page)
        context = {'posts': main_list, 'companydict': companyNamedict, 'bbspage': bbspage, 'userss': user_name, 'user_id': user_id}

        if kw != None:
            print('1들어옴')
            print(kw)
            print(main_list)
            post = main_list.filter(
                Q(title__icontains=kw) |
                Q(contents__icontains=kw)
                # Q(author__name__icontain=kw)
            ).distinct()
            print(post)
            paginator = Paginator(post, 10)
            page = request.GET.get('page')
            bbspage = paginator.get_page(page)
            context = {'posts': post, 'companydict': companyNamedict, 'bbspage': bbspage, 'userss': user_name, 'user_id': user_id}


    return render(request, 'bbs.html', context)




def board_create(request):
    print('board_create')
    user_name = request.session['userss']
    user_id = request.session['user_id']
    companyNamedict = GetStockCode.Get_CSV_Maching_dict()
    companyName = request.POST.get('machingstock')
    print(companyName)
    xmlDict = GetStockCode.Get_XML_maching_dict()
    match_code = ''
    if companyName is not None:
        match_code = xmlDict[companyName]
        print(match_code)


    if request.method == 'POST':
        post_form = PostForm(request.POST)
        print('포스트로 들오온')
        print(post_form.errors)

        if post_form.is_valid():
            print('폼이상')
            if match_code != '':
                print(post_form)
                # commit=False : db에 넣지말고 객체를 가져와라->post에 넣어줌
                post = post_form.save(commit=False)
                post.maching_code = match_code
                post.stock_name = companyName
                post.save()
            #post_form.save()
            return redirect('board:bbs_main')

    else:
        post_form = PostForm()
        print('get으로 들어온다 ')

    return render(request, 'bbs_create.html', {'post_form': post_form, 'companydict': companyNamedict, 'userss': user_name, 'user_id': user_id })





def board_detail(request, post_id):
    user_name = request.session['userss']
    user_id = request.session['user_id']
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        print("디테일 포스트로 들어옴 ")

    else:
        post_form = PostForm(instance=post)
        for i in post_form.fields:  # 수정이 되지 않도록 처리
            post_form.fields[i].disabled = True
        comment_form = CommentForm()
        print("디테일 엘스 들어옴 ")

    return render(request, 'bbs_detail.html', {'post_form': post_form, 'post': post, 'comment_form': comment_form, 'userss': user_name, 'user_id': user_id})


### 원본 ###
# def board_send_comment(request, post_id):
#     print("Comment 들어왔다")
#     post = get_object_or_404(Post, pk=post_id)
#     comment = Comment(comment=post)
#
#     if request.method == "POST":
#         print("post 들어왔다 ")
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             # comment = form.save(commit=False)
#             # comment.post = post
#             comment.save()
#             print("comment pk: {}".format(comment.pk))
#             return redirect(request, 'board:bbs_detail', post_id=post_id)
#
#             # return redirect("/stock/bbs/" + str(post_id) + '/detail')
#     else:
#         form = CommentForm(request.GET)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect(request,'board:bbs_detail', post_id=post_id)
#
#     print("pComment 그린다 ")
#     return redirect(request,'board:bbs_detail', post_id=post_id)





### 테스트 ###

def board_send_comment(request, post_id):

        print("Comment 들어왔다")
        post = get_object_or_404(Post, pk=post_id)
        comment = Comment(comment=post)
        # comment_list = Comment.objects.all().order_by("comment_id")
        # print(comment_list)
        post_form = PostForm(request.POST, instance=post)


        if request.method == "POST":
            print("post 들어왔다 ")
            form = CommentForm(request.POST, instance=comment)

            if form.is_valid():
                comment.save()
                page = request.GET.get('page', '1')
                paginator = Paginator(comment_list, 10)
                print("page")
                print(page)
                commentpage = paginator.get_page(page)
                context = {'comment_list': comment_list,'post_form': post_form, 'post': post, 'comment_form': form, 'commentpage': commentpage}

                return render(request, 'bbs_detail.html',context)

                # return redirect("/stock/bbs/" + str(post_id) + '/detail')
        else:
            form = CommentForm(request.GET)
            page = request.GET.get('page','1')
            paginator = Paginator(comment_list, 10)
            commentpage = paginator.get_page(page)

            context = {'comment_list': comment_list,'post_form': post_form, 'post': post, 'comment_form': form, 'commentpage': commentpage}


            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                page = request.GET.get('page', '1')
                paginator = Paginator(comment, 10)
                commentpage = paginator.get_page(page)

                context = {'comment_list': comment_list,'post_form': post_form, 'post': post, 'comment_form': form, 'commentpage': commentpage}

                return render(request, 'bbs_detail.html', context)

        print("pComment 그린다 ")
        return render(request, 'bbs_detail.html', context)

    # else:
    #     print('선택한 종목이 없습니다')
    #     main_list = Post.objects.all().order_by('-id')
    #     paginator = Paginator(main_list, 10)
    #     page = request.GET.get('page')
    #     bbspage = paginator.get_page(page)
    #     context = {'posts': main_list, 'companydict': companyNamedict, 'bbspage': bbspage}
    #
    # return render(request, 'bbs.html', context)





def board_update(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid(): # 입력한 데이터에 문제가 없다면
            post_form.save() # 포스트 폼에 저장한다
            return redirect('board:bbs_detail', post_id=post_id)
            # 네임스페이스가 posts이고 urlpattern에서 name이 list인
            # url로 리다이렉션

    else:
        post_form = PostForm(instance=post)
        # 수정 시 빈 칸이 아니라 instance에 post 데이터를 가져오는 칸을 만들어줌

    return render(request, 'bbs_create.html', {'post_form': post_form})



def board_delete(request, post_id):
    post = Post.objects.get(id=post_id) # id가 인자로 넘어온 id와 일치한 객체만 post에 넘겨줌
    post.delete()

    return redirect('board:bbs_main')



# def board_search(request):
#     post = Post.objects.all().order_by('id')
#     kw = request.GET.get('kw','')
#
#     if kw:
#         post = post.filter(
#             Q(title__icontains=kw) |
#             Q(contents__icontains=kw) |
#             Q(author__username__icontain=kw)
#         ).distinct()












