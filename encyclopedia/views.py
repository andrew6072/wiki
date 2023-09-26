from django.shortcuts import render
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_entry(request, title):
    entry = util.get_entry(title)
    if not entry:
        # render Error page
        return render(request, "encyclopedia/entry_not_found.html", {
            "title": title
        })
    return render(request, "encyclopedia/entry_found.html", {
        "entry": markdown.markdown(entry),
        "title": title
    })
