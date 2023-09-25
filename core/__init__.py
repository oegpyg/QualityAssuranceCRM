"""from django.shortcuts import render, redirect
from .forms import RecordForm

def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_de_registros')
    else:
        form = RecordForm()
    
    return render(request, 'crear_registro.html', {'form': form})
"""