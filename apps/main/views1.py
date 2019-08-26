from django.shortcuts import render

from apps.main.utils import group_required


@group_required("group1")
def main(request):
    template = 'main1/main.html'
    return render(request, template)
