from django.urls import re_path,path
from Quiz.views import show_questions , index, submit_query, update_password
urlpatterns = [
    path('', index),
    re_path(r'questions/submit_query/', submit_query , name="submit_query"),
    re_path(r'questions/', show_questions , name='show_questions'),
    re_path(r'update_password/', update_password),
    # re_path(r'tags',views.show_tags),
]