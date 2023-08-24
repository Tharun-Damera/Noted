from django.urls import path

from .views import *

app_name = 'notesapp'

urlpatterns = [

    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('', list_notes_view, name='notes'),
    path('addnote/', create_note, name='addnote'),
    path('update/<int:id>', update_note, name='update'),
    
    path('trash/', trash_view, name='trash'),
    path('delete_trash/<int:id>', delete_trash, name='delete_trash'),
    path('move_to_trash/<int:id>', move_to_trash, name='move_to_trash'),

]



