from django import forms
from .models import UserDetail,UserRelative,RelationType,Celebration, CelebrationParticipants,Leave 


class UserDetailCreationForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields ='__all__'

class UserRelativeCreationForm(forms.ModelForm):
    class Meta:
        model = UserRelative
        fields = '__all__'   

class RelationTypeCreationForm(forms.ModelForm):
    class Meta:
        model = RelationType
        fields = '__all__'            

class CelebrationCreationForm(forms.ModelForm):
    class Meta:
        model = Celebration
        fields = '__all__'       

class CelebrationParticipantsCreationForm(forms.ModelForm):
    class Meta:
        model = CelebrationParticipants
        fields = '__all__'        

class LeaveCreationForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'

        