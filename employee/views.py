from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .forms import UserDetailCreationForm,RelationTypeCreationForm,CelebrationCreationForm,LeaveCreationForm
from .models import UserDetail,UserRelative,CelebrationParticipants,Leave
from .forms import UserDetailCreationForm,UserRelativeCreationForm,CelebrationParticipantsCreationForm
from .models import UserDetail,Celebration,RelationType
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView 
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse



# Create your views here.

class UserDetailCreationView(CreateView):
    template_name = 'employee/create.html'
    model = UserDetail
    form_class = UserDetailCreationForm
    success_url = '/employee/list/'
    
class UserDetailListView(ListView):
    template_name = 'employee/list.html'
    model = UserDetail
    context_object_name = 'userdetails'

class UserRelativeCreateView(CreateView):
    template_name = "employee/create_relative.html"
    model = UserRelative 
    form_class = UserRelativeCreationForm
    success_url = "/employee/list/"   

class RelationTypeCreateView(CreateView):
    template_name = "employee/create_relationtype.html"
    model = RelationType
    form_class = RelationTypeCreationForm
    success_url = "/employee/list/"

class UserDetailDeleteView(DeleteView):
    model = UserDetail
    template_name = "employee/employee_delete.html"    
    success_url = "/employee/list/"

class UserDetailDetailView(DetailView):
    model = UserDetail
    context_object_name = "userdetails"
    template_name = "employee/employee_detail.html"  

class UserDetailUpdateView(UpdateView):
    model = UserDetail
    form_class = UserDetailCreationForm
    template_name = "employee/employee_update.html" 
    success_url = "/employee/list/" 

class CelebrationCreationView(CreateView):
    template_name = "celebration/create.html"
    model = Celebration
    form_class = CelebrationCreationForm 
    success_url = "/employee/celebration_list/"  

class CelebrationListView(ListView):
    template_name = 'celebration/list.html'
    model = Celebration
    context_object_name = 'celebrations'

class CelebrationParticipantsCreateView(CreateView):
    template_name = "celebration/create_participants.html"  
    model = CelebrationParticipants
    form_class = CelebrationParticipantsCreationForm
    success_url = "/employee/celebration_list/"

class CelebrationDeleteView(DeleteView):
    model = Celebration
    template_name = "celebration/celebration_delete.html"
    success_url = "/employee/celebration_list/"

class CelebrationDetailView(DetailView):
    model = Celebration
    context_object_name = "celebrations"
    template_name = "celebration/celebration_detail.html"

class CelebrationUpdateView(UpdateView):
    model = Celebration
    form_class = CelebrationCreationForm
    template_name = "celebration/celebration_update.html"
    success_url = "/employee/celebration_list/"   

class LeaveCreateView(CreateView):
    template_name = "leave/create.html"
    model = Leave
    form_class = LeaveCreationForm
    success_url = "/employee/leave_list/"   

class LeaveListView(ListView):
    template_name = "leave/list.html"
    model = Leave
    context_object_name = "leaves" 

class LeaveDeleteView(DeleteView):
    model = Leave
    template_name = "leave/leave_delete.html"
    success_url = "/employee/leave_list/"

class LeaveDetailView(DeleteView):
    model = Leave
    context_object_name = "leaves"
    template_name = "leave/leave_detail.html" 

class LeaveUpdateView(UpdateView):
    model = Leave
    form_class = LeaveCreationForm
    template_name = "leave/leave_update.html"
    success_url = "/employee/leave_list/"                

class UpdateStatusView(View):
    
    def post(self, request, pk):
        # Get the task instance
        print("pk....",pk)
        leaves = Leave.objects.get(id=pk)
        print("leave....",Leave)
        
        # Check the current status and update it accordingly
        if Leave.status == "Not Started":
            Leave.status = "In Progress"
        elif Leave.status == "In Progress":
            Leave.status = "Done"
        
        # Save the updated task
        Leave.save()
        
        return redirect(reverse('leave_list')) #lazy reverse

    


    

