from django.shortcuts import render , reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from Quiz.models import Tag, Question , userprofile , Student
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
            
            except:
                print('error')

            #passwd = check_password(password, passwordd)
            #print (passwd)


            if password == passwordd :
                #user = authenticate(username = username, password = password)
                userr = userprofile.objects.get(registration_number = registration_number, password = passwordd)
            else:
                print("password not matched")
                

            if userr:
                print(userr)
                #return HttpResponse(user.id)
                request.session['registration_id'] = userr.registration_number
                print (user.id)
                request.session['session_id'] = request.session.session_key
                new_id = user.id
                #user.save()
                print(new_id)
                

                return HttpResponseRedirect(reverse('student_form'))
            else:
                print('in else')
                context['error'] = "Error in Connection"
                return render(request, 'Quiz/index.html', context)


        else:
            return render(request , 'Quiz/index.html')
    # except:
    #     return render(request , 'Quiz/index.html')



def student_form(request):
    request.session.set_expiry(300)
    try:
        print(request.session.session_key)
        new_id = request.session['registration_id']
        user_id = request.session['session_id']
        if user_id:
            try:
                if request.method == 'POST':
                    print('post')
                    # #con = {}
                    student_detail = Student(College_Registration_Number = new_id)
                    #student_detail.College_Registration_Number = request.POST[new_id]
                    student_detail.First_Name = request.POST['FName']
                    student_detail.Last_Name = request.POST['LName']
                    student_detail.Graduation_Year = request.POST['GYear']
                    student_detail.Branch = request.POST['Branch']
                    student_detail.Course = request.POST['Course']
                    student_detail.Email = request.POST['Email']
                    student_detail.Phone_Number = request.POST['PNumber']
                    student_detail.save()
                    # print(registration_number)

                    # student_form = student_form()
                    return HttpResponseRedirect(reverse('show_questions'))

                else: 
                    print('else')   
                    return render(request , "Quiz/student_form.html")
            except:
                print('except')   
                return render(request , "Quiz/student_form.html")
        else:
            return render(request , "Quiz/student_form.html")

    except:
        #del request.session['session_id']
        return render(request , "Quiz/index.html")        




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
    s = ['hudavf9' , 'sad7zvzta8g' , '9ddsfwa8wygucs']
    Password = []
    # for i in s:
    length = len(s)
    print(len(s))
    print(length)

    for i in s:
        password = randomPassword()
        Password.append(password)
        
    print(Password)

    
    # for i in s:
    #     user.registration_number = s[i]
    #     for i in Password:
    #         user.password = Password[i]
    #     user.save()

    result = {
        'registration_number' : s,
        'password' : Password
    }
    

    print(result['registration_number'][0])
    print(result['password'][0])

    print(len(s))
    length = len(s)
    for i in range(length):
        print(i)
        user = userprofile()
        user.registration_number = result['registration_number'][i]
        user.password = result['password'][i]
        user.save()
        print(user)


    return HttpResponse(a)





def show_questions(request):
    request.session.set_expiry(300)
    try:
        new_id = request.session['registration_id']
        user_id = request.session['session_id']
        if user_id:
            question = Question.objects.all()   
            #choice = Choice.objects.all()
            context={
                "question" : question,
                #"choice" : choice
            }
            return render(request , 'Quiz/question.html' , context)
    except:
        return render(request , 'Quiz/index.html' , context)




def submit_query(request):
    request.session.set_expiry(300)
    try:
        new_id = request.session['registration_id']
        user_id = request.session['session_id']
        if user_id:
            try:
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

                return HttpResponse("Thanks For Your Submission ")

            except:
                return render(request , 'Quiz/question.html' , context)

    except:
        return render(request , 'Quiz/index.html' , context)
        #     return HttpResponse(Questionn)
        #     # for questn in Questionn:
        #         if questn.correct_option == i:
        #             print('corrected')

            
        #     print(Questionn)
        #     i = request.POST[i]
        #     print(i)

        # for count in request:
        #     #print(i)
        #     ques
        #     #print(count)
            
    # if question_id == None:
    #     return HttpResponse(Question.objects.all())
    # return HttpResponse(Question.objects.get(id = question_id))


# def show_tags(request, tag_id=None):
#     if tag_id == None:
#         return HttpResponse(Tag.objects.all())
#     return HttpResponse(Tag.objects.get(id = tag_id))
