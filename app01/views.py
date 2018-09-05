from django.shortcuts import render,HttpResponse,redirect
from app01.models import Book
# Create your views here.
import json

def login(request):
    if request.method =='GET':
        return render(request,'login.html')
    else:
        buser = request.POST.get('username')
        bpasswd = request.POST.get('password')
        if buser == 'lisl' and bpasswd == '123456':
            return redirect('index.html')
        else:
            login_status = "<script>alert('用户名或密码错误')</script>"
            return render(request,'login.html',{'login_status':login_status})


def index(request):
    print(request.method)
    if request.method =='GET':
        queryset = Book.objects.all()
        print(queryset)
        return render(request, 'index.html',{'all_of_book':queryset})
    else:
        print(request.POST)
        cid =request.POST.get('id')
        print(type(cid))
        ctitle = request.POST.get('title')
        cprice = request.POST.get('price')
        cpublish = request.POST.get('publish')
        cpub_date = request.POST.get('pub_date')
        result=Book.objects.filter(id=cid).update(title=ctitle,publish=cpublish,price=cprice,pub_date=cpub_date)
        if result ==0:
            update_result = 'alert("修改失败")'
        else:
            update_result = 'alert("修改成功")'

        return render(request, 'result.html', {'update_result': update_result})


def query_all(request):

    if request.method =='GET':
        return redirect('index.html')
    else:
        title=request.POST.get('title')
        book_obj = Book.objects.filter(title=title).first()
        dic={}
        dic['id']=str(book_obj.id)
        dic['title']=book_obj.title
        dic['price']=str(book_obj.price)
        dic['publish']=book_obj.publish
        dic['pub_date']=str(book_obj.pub_date)
        print(dic)
        dic_json = json.dumps(dic)
        return HttpResponse(dic_json)

def delete(request):
    if request.method == 'GET':
        return redirect('index.html')
    else:
        print(request.POST)
        cid =request.POST.get('id')
        result=Book.objects.filter(id=cid).delete()
        if result ==0:
            update_result = 'alert("删除失败")'
        else:
            update_result = 'alert("删除成功")'

        return render(request, 'result.html', {'update_result': update_result})

def create(request):
    if request.method =='GET':
        return redirect('index.html')
    else:
        dict = request.POST.dict()
        result_count = Book.objects.filter(**dict).count()
        if result_count:
            create_result="alert('已存在，创建失败')"
            return render(request,'result.html',{'create_result':create_result})
        else:
            book_obj=Book.objects.create(**dict)
            create_result = "alert('创建成功')"
            return render(request, 'result.html', {'create_result': create_result})

def search(request):
    print(request.GET.dict())
    if request.method == 'POST':
        key2 = request.POST.get('key')
        content = request.POST.get('content')
        if content:
            queryset=Book.objects.filter(**{key2:content})
        else:
            queryset = Book.objects.all()
        return render(request,'index.html',{'all_of_book':queryset})
    else:
        return redirect('index.html')