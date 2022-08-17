from turtle import title
from unicodedata import name
from django.shortcuts import render
from todo_app.models import Item
from django.http import HttpResponseRedirect


def item_list(request):
    items = Item.objects.all()
    return render(
        request,
        "bootstrap/index1.html",
        {"items": items},
    )


def item_add(request):
    if request.method == "GET":
        return render(request, "bootstrap/add_todo.html")
    else:
        item = Item(title=request.POST["title"], contents=request.POST['content'])        
        item.save()
        return HttpResponseRedirect("/")


def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return HttpResponseRedirect("/")  # redirects to homepage


def item_update(request, pk):
    if request.method == "POST":
        item = Item.objects.get(id=pk)
        item = Item(title=request.POST["title"], contents=request.POST['content'])
        item.save()
        return HttpResponseRedirect("/")
    else:
        item = Item.objects.get(id=pk)
        return render(
            request,
            "bootstrap/update.html",
            {"item": item},
        )
