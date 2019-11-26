from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from product.models import Stock, Product, Cart,checkout

@login_required
def addcart(request):
    x=request.GET["pid"]
    qt=Stock.objects.filter(prodid=x)
    qtt=0
    for p in qt:
        qtt=p
    qt = [q for q in range(1, qtt.tot_qty + 1)]
    return render(request,'addcart.html',{"pid":x,"qtt":qt})
def insertcart (request):
    x=request.GET["pid"]
    qt=request.GET["qt"]
    user= User.objects.get(id=request.session.get("_auth_user_id"))
    un= str(user.username)
    pr= Product.objects.get(pid=int(x))
    a=int(str(x))
    b=int(str(qt))
    c=un
    d=float(pr.pcost)
    e=int(str(qt)) * float(pr.pcost)
    f=pr.image
    ct=Cart(username=c,pid=a,units=b,unitprice=d,tuprice=e,image=f)
    ct.save()
    stc = Stock.objects.get(prodid=a)
    stc.tot_qty = stc.tot_qty - b
    stc.save()
    return render(request,'insertcart.html')
@login_required
def viewcart(request):
    user = User.objects.get(id=request.session.get("_auth_user_id"))
    un = str(user.username)
    y=Cart.objects.filter(username=un)
    return render(request,'viewcart.html',{'x':y})
def delete(request):
    cs=Cart.objects.filter(id=int(request.GET["id"]))
    stc = Stock.objects.get(prodid=int(request.GET['pid']))
    stc.tot_qty=stc.tot_qty+ int(request.GET['units'])
    stc.save()
    cs.delete()
    return render(request,'viewcart.html',{'x': display(request)})

def display (request):
    user = User.objects.get(id=request.session.get("_auth_user_id"))
    un = str(user.username)
    ct = Cart.objects.filter(username=un)
    # tp = 0.0
    # ctid=0
    # for p in ct:
    #     tp = tp + float(p.tuprice)
    #     ctid=p.id
    # dic= {"k": ct, "tp":tp, 'ctid':ctid}
    return ct
def modifycart(request):
    x= int(request.GET['pid'])
    qt= Stock.objects.filter(prodid=x)
    qtt = 0
    for p in qt:
        qtt = p
    qt = [q for q in range(1, qtt.tot_qty + 1)]
    oldqt = request.GET['oqt']
    cid = request.GET['id']
    return render(request,'modifyqty.html',{"cartid":cid,"pid":x,"qtt":qt,"oq":oldqt})
def modifiedcart(request):
    cid = int(request.GET["cid"])
    nqt = int(request.GET["nqt"])
    obj = Cart.objects.get(id=cid)
    stc = Stock.objects.get(prodid=int(request.GET['pid']))
    stc.tot_qty = stc.tot_qty - int(nqt) + int(request.GET['oldqty'])
    stc.save()
    obj.units = nqt
    up = obj.unitprice
    obj.tuprice = up * nqt
    obj.save()
    res = Cart.objects.filter(pid=cid)
    return render(request,'viewcart.html',{'x': display(request)})
def checkout (request):
    user = User.objects.get(id=request.session.get("_auth_user_id"))
    un = str(user.username)
    y = Cart.objects.filter(username=un)
    return render(request,'checkout.html')