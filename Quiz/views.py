from django.shortcuts import render , reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from Quiz.models import Question , userprofile , Student
import string
import random



def index(request):
        print('try')
    #try:
        print('in')
        if request.method == 'POST':
            print('post')
            #con = {}
            registration_number = request.POST['registration_number']
            password = request.POST['password']
            print(registration_number)
            print(password)
                # password = hashlib.sha256(password.encode())
                # password = password.hexdigest()

            try:
                print('try in')
                user = userprofile.objects.get(registration_number = registration_number)
                print(user)
                passwordd = user.password
                print(user.password)              
            

                if password == passwordd :
                    #user = authenticate(username = username, password = password)
                    userr = userprofile.objects.get(registration_number = registration_number, password = passwordd)
                else:
                    print("password not matched")
                    

                if userr:
                    print(userr)
                    
                    request.session['registration_id'] = userr.registration_number
                    
                    request.session['session_id'] = request.session.session_key
                    
                    return HttpResponseRedirect(reverse('student_form'))
                
                else:
                    print('in else')
                    context['error'] = "Error in Connection"
                    return render(request, 'Quiz/index.html', context)
            except:
                return HttpResponse("Go Back Something wents wrong")


        else:
            return render(request , 'Quiz/index.html')
    # except:
    #     return render(request , 'Quiz/index.html')



def student_form(request):
        request.session.set_expiry(300)
    #try:
        print(request.session.session_key)
        new_id = request.session['registration_id']
        user_id = request.session['session_id']
        if user_id:
            #try:
                if request.method == 'POST':
                    print('post')
                    # #con = {}
                    student_detail = Student.objects.get(College_Registration_Number = new_id)
                    
                    if student_detail.Login_Count == 1:
                        return HttpResponseRedirect(reverse('index'))
                    
                    else:
                        #student_detail.College_Registration_Number = request.POST[new_id]
                        student_detail.First_Name = request.POST['FName']
                        student_detail.Last_Name = request.POST['LName']
                        student_detail.Graduation_Year = request.POST['GYear']
                        student_detail.Branch = request.POST['Branch']
                        student_detail.Course = request.POST['Course']
                        student_detail.Email = request.POST['Email']
                        student_detail.Phone_Number = request.POST['PNumber']
                        student_detail.Login_Count = 1
                        student_detail.save()
                        # print(registration_number)

                        # student_form = student_form()
                        return HttpResponseRedirect(reverse('show_questions'))

                else: 
                    print('else')   
                    return render(request , "Quiz/student_form.html")
            # except:
            #     print('except')   
            #     return render(request , "Quiz/student_form.html")
        else:
            return render(request , "Quiz/student_form.html")

    # except:
    #     return HttpResponseRedirect(reverse('index'))
                




def randomPassword():
    """Generate a random password """
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(6):
        password += random.choice(randomSource)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password




def update_password(request):
    a = randomPassword()
    s = ['199ufewewf9' , 'cffewvdsg' , 'oiufwfs']
    Password = []
    # for i in s:
    length = len(s)
    print(len(s))
    print(length)

    # if request.method == "POST":
    #     passwd = request.POST["image"]
    #     pwd = json.load(passwd)
    #     print(pwd)
    
    for i in s:
        password = randomPassword()
        Password.append(password)
        

    result = {
        'registration_number' : s,
        'password' : Password
    }
    


    print(len(s))
    length = len(s)
    for i in range(length):
        print(i)
        user = userprofile()
        user.registration_number = result['registration_number'][i]
        user.password = result['password'][i]
        user.save()
        print(user)
        student_detail = Student()
        if student_detail:
            student_detail.College_Registration_Number = result['registration_number'][i]
            student_detail.Password = result['password'][i]
            student_detail.save()
            print(student_detail)

    return HttpResponse(a)





def show_questions(request):
    request.session.set_expiry(300)
    try:
        new_id = request.session['registration_id']
        user_id = request.session['session_id']
        if user_id:
            try:
                question = Question.objects.all()   
                #choice = Choice.objects.all()
                context={
                    "question" : question,
                    #"choice" : choice
                }
                return render(request , 'Quiz/question.html' , context)
            except:
                return render(request , 'Quiz/question.html' , context)
        else:
            return render(request , 'Quiz/question.html')
    except:
        return HttpResponseRedirect(reverse('index'))



def submit_query(request):
        request.session.set_expiry(300)
    #try:
        new_id = request.session['registration_id']
        user_id = request.session['session_id']
        if user_id:
            #try:
                result = []
                choice = []
                number = 0
                if request.method == 'POST':
                    
                    print("hey")
                    print(request.POST)
                    requestt = request.POST
                    print("hi")
                    #Question = Question.objects.get(name = i)
                    for i in requestt:
                        print('i is')
                        print(i)
                        question_name = str(i)
                        field = request.POST[i] 
                        choice.append(field)           
                        print('hey')
                        print(field) 
                        student_form = Student.objects.get(College_Registration_Number = new_id)
                        print(question_name)   
                        result.append(question_name)    
                
                print(result)
                print(choice)
                i = 1 
                print(result.pop(0))   
                print(choice.pop(0))
                for i in result:
                    print(i)
                    Questionn = Question.objects.get(question_text=i)
                    
                    for j in choice:
                        if Questionn.correct_option == j:
                            print('corrected')
                            number +=1
                            
                        else:
                            print('incorrect')
                            number +=0
                            
                    print(number)
                    student_form.Score = number
                    student_form.save()
                    #del request.session['session_id']
                
                del request.session['registration_id']
                
                return HttpResponse("Thanks For Your Submission ")

    #         except:
    #             del request.session['session_id']
    #             del request.session['registration_id']
    #             return HttpResponseRedirect(reverse('index'))

    # except:
    #     return HttpResponseRedirect(reverse('index'))






from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, serializers
from .serializers import QuestionSerializer
#from rest_framework.parsers import MultiPartParser, FormParser




# @api_view(['GET', 'POST'])
# def questions_view(request):
#     if request.method == 'GET':
#         return HttpResponse("not Implemented")
#     elif request.method == 'POST':
#         tag_name = request.data['tag_name']
#         question_text = request.data['question_text']
#         choice_text1 = request.data['choice_text1']
#         choice_text2 = request.data['choice_text2']
#         choice_text3 = request.data['choice_text3']
#         choice_text4 = request.data['choice_text4']
#         correct_option = request.data['correct_option']

#         #pub_date = datetime.strptime(request.data['pub_date'], '%Y-%m-%d')
#         Question.objects.create(tag_name=tag_name, question_text=question_text, choice_text1=choice_text1, choice_text1=choice_text1, choice_text2=choice_text2, choice_text3=choice_text3, choice_text4=choice_text4, correct_option=correct_option)
#         return HttpResponse("Question created", status=201)


class questions_view(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    print(serializer_class.data)


#def ll(request):
#     print('ll')
#     if request.method == 'POST':
#         print('post') 
#         print(request.FILES)
#         img = request.FILES('image')
#         print(img)
    