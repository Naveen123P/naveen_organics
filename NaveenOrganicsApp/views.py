from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Cart, Mango, UserProfile, AllFruits, ProductDetails


# Create your views here.

def register(request):
    if request.method == 'POST':
        print("I am in if condition...")
        name = request.POST['username']
        pwd = request.POST['password']
        emailID = request.POST['email']
        mobile_no = request.POST['mobile']
        address= request.POST['address']
        confirmPassword1= request.POST['confirm-password']
        print(name, pwd, emailID)
        if (pwd == confirmPassword1):
            # Check if the username already exists
            if UserProfile.objects.filter(username=name).exists():
                return render(request, 'register.html', {'msg': 'Username already exists. Please choose a different username.'})
            elif UserProfile.objects.filter(email=emailID).exists():
                return render(request, 'register.html', {'msg1': 'emailID already exists. Please choose a different emailID.'})
            # If the username doesn't exist, proceed with registration
            else:
                datafetch = UserProfile.objects.all().last()
                i = datafetch.id
                datasaving = UserProfile(i+1, name, pwd, emailID,mobile_no,address)
                datasaving.save()
                return render(request, 'success.html')
        else:
            return render(request, 'register.html', {'msg2': 'Please enter the the same password'})
    else:
        return render(request, 'register.html', {'msg': 'Welcome to Naveen Organics',})

def login(request):
    if request.method == 'POST':
        username1=request.POST['username']
        password1=request.POST['password']
        print(username1,password1)
        dataFetch=UserProfile.objects.all().filter(username=username1,password=password1).count()
        print(dataFetch)
        if dataFetch == 0:
            print("Iam in if condition of datafetch is none....")
            return render(request, "login.html", {'msg': "Username does not exist or wrong password "})
        else:
            fruits = AllFruits.objects.all()
            request.session['username'] = username1
            return render(request, 'userProfile.html', {'username': username1,'fruits': fruits})     
    else:
        print('i am in main else condition....')
        return render(request, "login.html", {"msg": "Wellcome to Naveen Organics"})
    
def mango2(request):
    if request.method == 'POST':
        fruitname=request.POST['fruitname']
        mangoes = Mango.objects.all().filter(category=fruitname.lower())
        username = request.session.get('username')
        return render(request, 'FruitsTableData/mango2.html', {'mangoes': mangoes, "username": username})
    
def home(request):
    fruits = AllFruits.objects.all()
    return render(request, 'index.html', {'fruits': fruits})

def productdetails(request):
    if request.method == 'POST':
        fruitname=request.POST['fruitname']
        price=request.POST['price']
        rating=request.POST['rating']
        imgUrl=request.POST['imgUrl']
        print(fruitname,price,rating,imgUrl)
        datasaving = ProductDetails(1,fruitname,price,rating,imgUrl)
        datasaving.save()
        username = request.session.get('username')
        return render(request, 'FruitsTableData/productDetails.html',{"username": username, "fruitname": fruitname,"price": price, "rating": rating, "imgUrl" :imgUrl})

def logout(request):
    request.session.pop('username',None)
    return redirect('../')

# @login_required
def dashboard(request):
    if request.method == 'POST':
        # username=request.POST['username']
        username = request.session.get('username')
        userDetails = UserProfile.objects.get(username=username)
        print(userDetails, 'koti koti koti koti')
        return render(request, 'userDashbord.html', {"username": username, 'userDetails': userDetails})