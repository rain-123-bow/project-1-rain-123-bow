from django.shortcuts import render
import random
from . import util, urls

import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show(request, name):
    return render(request, "encyclopedia/target.html", {
        "entries": markdown2.markdown(util.get_entry(name))
    })

def search(request):
    search_word = request.GET.get('wd', '')
    try:
        return render(request, "encyclopedia/target.html", {
            "entries": markdown2.markdown(util.get_entry(search_word))
        })
    except:
        return render(request, "encyclopedia/no_match.html")


def no_match(request):
    return render(request, "encyclopedia/no_match.html")

def create_newpage(request):
    return render(request, "encyclopedia/create_newpage.html")

def create(request):
    title_copy = request.GET.get('title', '')
    content_copy = request.GET.get('content', '')
    util.save_entry(title_copy, content_copy)
    return render(request, "encyclopedia/success.html", {
        "entries": markdown2.markdown(util.get_entry(title_copy))
    })

def random_page(request):
    list1 = util.list_entries()
    num = len(list1)
    randomNum = random.randrange(num)-1
    return render(request, "encyclopedia/target.html", {
        "entries": markdown2.markdown(util.get_entry(list1[randomNum]))
    })