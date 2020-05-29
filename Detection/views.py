from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import User,App,Review,blockwords,WorkAssign,WorkProgress,Work

# Create your views here.
def index(request):
    mydict={
        "id":"1001",
        "name":"Athira"
    }
    return render(request,"new.html", context=mydict)
def home(request):
    mydict={
        "id":"1001",
        "name":"Athira",
        "course":"MCAd"
    }
    return render(request,"student.html", context=mydict)
def reg(request):
    return render(request,"reg.html")
def temp(request):
    return render(request,"template.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def forgot_pswd(request):
    return render(request,"forgot_pswd.html")
def postData(request):
    a=request.POST.get('appname')
    my_dict={
        'A':a,
        'data':""
        } 
    if request.method=="POST":
        AlData=App()
        AlData.appname=request.POST.get('appname')
        AlData.description=request.POST.get('description')
        AlData.developer=request.POST.get('developer')
        AlData.size="Size"
        AlData.save()
    
    return HttpResponse(a)

def loadData(request):
    wa=WorkAssign.objects.filter(username__id=request.session["sid"]).select_related('workname').all()
    joined = []
   
    for x in wa:
        joined.append({
            
            'workname': x.workname.workname,
            'workprogress': x.workname.workprogres,
            'id': int(x.id),
            'workid':x.workname.id,

        })


   

    my_dict={
        'data':joined,
        'username':request.POST.get('username')
    }
    print ("dict['Name']: ", my_dict['username'])
    return render(request,'app.html',context=my_dict)

def user_chk(request):
    if request.method=="POST":
        userData=User.objects.filter(username=request.POST.get('username'),password=request.POST.get('pass'))
        print(request.POST.get('username'))
        print(userData.count())

        if userData.count()>0:
            for us in userData:
                request.session["sid"]=us.id
                print(us.id)
                return loadData(request)
        else:
            my_dict={
            'A':"Wrong Password", 
            'data':""
             } 
    return render (request,"login.html")

def reviewApp(request):
    
    AlData=Work.objects.filter(pk=request.GET["workid"])
    my_dict={
        'data':AlData,
        'id':request.GET["id"]

    }
    return render (request,"reviewapp.html",context=my_dict)

def sendreview(request):
     if request.method=="POST":
        obj= Work.objects.get(pk=request.POST.get("workid"))
        print(obj.workprogres)
        obj.workprogres = request.POST.get("status")
        obj.save()
        return loadData(request)

     if request.method=="POST1":
        msg=WorkProgress()
        msg.work=get_object_or_404(WorkAssign, pk=request.POST.get("workid"))
        msg.username=get_object_or_404(User, pk=request.session["sid"])
        msg.detail=request.POST.get("review")
        msg.status=request.POST.get("status")
        msg.save()
        return loadData(request)


def seereview(request):
    AlData=Review.objects.filter(appname=get_object_or_404(App, pk=request.GET["id"]))
    my_dict={
        'data':AlData
    }
    return render (request,"seereviews.html",context=my_dict)


def saveUser(request):
    if request.method=="POST":
        ur=User()
        ur.name=request.POST.get('name')
        ur.username=request.POST.get('username')
        ur.email=request.POST.get('email')
        ur.password=request.POST.get('password')
        ur.desg=request.POST.get('status')
        ur.save()
    return render(request,"login.html") 