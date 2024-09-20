from django.shortcuts import render, get_object_or_404
from .models import TO_DO
 
def home(request):
    if request.method == 'POST':
        action = request.POST.get('action', '')
         
        if action == 'create':
            task = request.POST.get('task')
            if task:
                TO_DO.objects.create(task=task)
       
        elif action == 'update':
            task_id = request.POST.get('task_id')
            task_text = request.POST.get('task')
            if task_id and task_text:
                task = get_object_or_404(TO_DO, id=task_id)
                task.task = task_text
                task.save()
       
        elif action == 'delete':
            task_id = request.POST.get('task_id')
            if task_id:
                task = get_object_or_404(TO_DO, id=task_id)
                task.delete()
    tasks = TO_DO.objects.all()
    return render(request, 'task.html', {'tasks': tasks})