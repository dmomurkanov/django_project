from django.shortcuts import render

from common.models import Common


# Create your views here.
def get_common():
    common = Common.get_solo()
    print(common)
    return common