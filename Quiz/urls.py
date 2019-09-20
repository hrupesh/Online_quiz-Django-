from django.urls import re_path,path, include
from Quiz.views import show_questions, index, submit_query, update_password , student_form, questions_view
from rest_framework import routers
#from Quiz.views import ll


router = routers.DefaultRouter()
router.register(r'q', questions_view)


urlpatterns = [
    path('', index , name='index'),
    re_path(r'questions/submit_query/', submit_query , name="submit_query"),
    re_path(r'questions/', show_questions , name='show_questions'),
    re_path(r'update_password/', update_password),
    re_path(r'Student_form/', student_form , name='student_form'),
    #re_path(r'qq/', questions_view , name='question_view'),
    #path('upload/' , ll , name='ll'),
    re_path(r'', include(router.urls)),

]
