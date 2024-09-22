from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Cart, Mango, UserProfile, AllFruits, ProductDetails


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def home2(request):
    fruits = AllFruits.objects.all()
    return render(request, 'home2.html', {'fruits': fruits})

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

    user = request.user
    # mangoes = Mango.objects.all().filter(category='Banana')
    
    #     price=request.POST['price']
    #     rating=request.POST['rating']
    #     imgUrl=request.POST['imgUrl']

    #     datasaving = ProductDetails(1,fruitname,price,rating,imgUrl)
    #     datasaving.save()
    # else:
    # username = request.session.get('username')
    if request.method == 'POST':
        fruitname=request.POST['fruitname']
        mangoes = Mango.objects.all().filter(category=fruitname.lower())
        username = request.session.get('username')
        return render(request, 'FruitsTableData/mango2.html', {'mangoes': mangoes, "username": username})
    
def home(request):
    fruits = AllFruits.objects.all()
    return render(request, 'home3.html', {'fruits': fruits})

def productdetails(request):
    #productdetails = ProductDetails.objects.all()
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

def mango(request):
    mangoes = Mango.objects.all()
    return render(request, 'fruitsdata/mango.html', {'mangoes': mangoes})

def fruitWiseList(request,fruitName):
     return render(request,'fruitsdata/mango.html',{'fruitName':fruitName})

def test(request):
    return render(request,'Fruits/test.html')

def test2(request,fruitName):
    return render(request,'Fruits/test2.html',{'fruitName':fruitName})

# views.py


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['productId']
        quantity = request.POST['quantity']
        user = request.POST['user']
        fruitname = request.POST['fruitname']
        price = request.POST['price']


        # Assuming you have a Mango model and the user is logged in
        # product = Mango.objects.get(id=product_id)
        # user = request.user

        # Create a new CartItem and save it to the database
        datasave=Cart(1,user,product_id, fruitname,quantity,price)
        datasave.save()
        #CartItem.objects.create(user=user, product=product, quantity=quantity, img_url=product.imgUrl)
        username = request.session.get('username')
        return render(request, 'cart.html',{"username":username,'message': 'Item added to cart successfully'})
    else:
        return render(request, "cart.html")


def logout(request):
    request.session.pop('username',None)
    return redirect('../')

def mangodet(request):
    if request.method == 'POST':
        print('Iam in if part of mangodet function.....')
        category=request.POST['fruitName']
        print('Fruit name : ',category)
    else:
        print('Iam in else part of mangodet function.....')
        return render(request, 'Fruits/mango.html')

# @login_required
def dashboard(request):
    # print(request,'Rajesh')
    # user = request.user
    # userDetails = UserProfile.objects.get(user=user)
    # print(userDetails)
    # return render(request, "userDashbord.html")
    if request.method == 'POST':
        # username=request.POST['username']
        username = request.session.get('username')
        userDetails = UserProfile.objects.get(username=username)
        print(userDetails, 'koti koti koti koti')
        return render(request, 'userDashbord.html', {"username": username, 'userDetails': userDetails})





'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to your dashboard or another page after login
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')

'''
'''
def mango(request):
    return render(request,'Fruits/mango.html')
'''
def apple(request):
    return render(request,'Fruits/apple.html')
def banannas(request):
    return render(request,'Fruits/banannas.html')
def ber(request):
    return render(request,'Fruits/ber.html')
def cashew(request):
    return render(request,'Fruits/cashew.html')
def coconut(request):
    return render(request,'Fruits/coconut.html')
def custardapple(request):
    return render(request,'Fruits/custardapple.html')
def dragen(request):
    return render(request,'Fruits/dragen.html')
def fig(request):
    return render(request,'Fruits/fig.html')
def grapes(request):
    return render(request,'Fruits/grapes.html')
def guavas(request):
    return render(request,'Fruits/guavas.html')
def jackfruit(request):
    return render(request,'Fruits/jackfruit.html')
def kiwi(request):
    return render(request,'Fruits/kiwi.html')
def orange(request):
    return render(request,'Fruits/orange.html')
def papayas(request):
    return render(request,'Fruits/papayas.html')
def peach(request):
    return render(request,'Fruits/peach.html')
def pears(request):
    return render(request,'Fruits/pears.html')
def pineapple(request):
    return render(request,'Fruits/pineapple.html')
def plum(request):
    return render(request,'Fruits/plum.html')
def pomegranate(request):
    return render(request,'Fruits/pomegranate.html')
def sapota(request):
    return render(request,'Fruits/sapota.html')
def sweetLime(request):
    return render(request,'Fruits/sweetLime.html')