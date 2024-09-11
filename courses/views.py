from django.shortcuts import render
from .models import Course

# Create your views here.

def course(request, course_name, id):
    course = Course.objects.get(course_name=course_name, id=id)
    course_topics = Course.objects.filter(course_name=course_name)
    
    current_index = list(course_topics).index(course)
    
    prev_topic = None
    next_topic = None
    
    if current_index > 0:
        prev_topic = course_topics[current_index - 1]
        
    if current_index < len(course_topics) - 1:
        next_topic = course_topics[current_index + 1]
    
    
    context = {
        'course': course,
        'course_topics': course_topics,
        'prev_topic': prev_topic,
        'next_topic': next_topic,
    }
    return render(request, 'course_page.html', context=context)