from django import forms
from all_apps.assignments.models import *
class Upload_assignment(forms.ModelForm):
    class Meta:
        model=AssignmentTopic
        fields="__all__"

        widgets={
            'assignment':forms.Select(attrs={'class':'shadow-sm bg-black-50 border border-black-300 text-black-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black-700 dark:border-black-600 dark:placeholder-black-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light'}),

            'topic_name':forms.TextInput(attrs={'class':'shadow-sm bg-black-50 border border-black-300 text-black-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black-700 dark:border-black-600 dark:placeholder-black-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light','placeholder':'Topic Name 😒'}),

            'pdf':forms.ClearableFileInput(attrs={'class':'block w-full p-3 text-sm text-gray-9 border border-gray-300 rounded-lg cursor-pointer  dark:text-gray-400 focus:outline-none dark:placeholder-gray-400'})
        }

class Add_Category(forms.ModelForm):
    class Meta:
        model=AllAssignment
        fields="__all__"

        widgets={
            'title':forms.TextInput(attrs={'class':'shadow-sm bg-black-50 border border-black-300 text-black-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-black-700 dark:border-black-600 dark:placeholder-black-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light','placeholder':'Category Name 😒'})
        }