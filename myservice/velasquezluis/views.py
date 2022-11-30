from django.contrib.auth import authenticate # Package Necesario
from django.http import HttpResponseRedirect # Package Necesario
from django.shortcuts import render
from velasquezluis.forms import ChatForm, LoginForm
from velasquezluis.models import Chat
import datetime

# Create your views here.
def home(request):
    # --
    # Bloque de código del saludo de bienvenida según la hora actual.
    mensaje = "Considerando que son las "
    currentTime = datetime.datetime.now()
    parsetime = str(currentTime.strftime("%H:%M"))

    if currentTime.hour < 12:
        mensaje += parsetime + ", ¡le doy los buenos días!"
    elif 12 <= currentTime.hour < 18:
        mensaje += parsetime + ", le doy las buenas tardes ~"
    else:
        mensaje += parsetime + ", espero que haya tenido un buen día, buenas noches..."
    print(mensaje)
    # Fin del bloque de tiempo.
    # --
    
    # Validación de la sesión inexistente.
    if not request.session.has_key('username'):
        # Si la sesión no existe, entonces me lleva de vuelta al login.
        return HttpResponseRedirect('/login')
    # Captura del usuario que actualmente levantó la sesión.
    username = request.session['username']
    # Captura de todos los objetos almacenados en la tabla de chats 'velasquezluis_chats' de mi BD.
    current_chat = Chat.objects.filter()
    # Variables que almacenan los datos a utilizar en el historial de chats.
    context = {
        "current_chat": current_chat,
        "username": username,
        "mensaje": mensaje
    }  
    return render(request, 'velasquezluis/index.html', context=context)

# Método de ingreso de chats al sistema y a la BD.
def nuevo_chat(request):
    # Verificar que no exista la sesión
    if not request.session.has_key('username'):
        # Si la sesión no existe, entonces me lleva al login
        return HttpResponseRedirect('/login')
    # Captura del actual usuario en la sesión.
    username = request.session['username']
    # Uso del método POST para rellenar el form de chat.
    if request.method == 'POST':
        chat = ChatForm(request.POST)
        if chat.is_valid: 
            chat.save()
            return HttpResponseRedirect('/')
    else:
        chat = ChatForm()

    return render(request, 'velasquezluis/form.html', {'chat': chat, 'username': username})

# Método de inicio de sesión al sistema.
def login(request):

    # Verificar que no exista la sesión
    if request.session.has_key('username'):
        # Si la sesión existe, entonces me lleva al home
        return HttpResponseRedirect('/nuevo_chat')
    else:
        # Si la sesión no existe, verifica el formulario
        if request.method == 'POST':
            # Si se recibe el formulario
            chat = LoginForm(request.POST)
            if chat.is_valid():
                # Si el formulario es válido, se verifican los datos
                username = chat.cleaned_data['email']
                password = chat.cleaned_data['password']
                # Usa la función authenticate de django.contrib.auth
                user = authenticate(username=username, password=password)
                if user is not None:
                    # Si los datos son válidos, crea la sesión
                    request.session['username'] = user.username
                    return HttpResponseRedirect('/nuevo_chat')
        else:
            # Si no estamos recibiendo el formulario, entonces envíamos uno vacío
            chat = LoginForm()
    
    return render(request, 'velasquezluis/login.html', {'chat': chat})

# Método para logout del sistema, si la sesión tiene una Key, entonces se le elimina y se redirecciona de vuelta al login.
def logout(request):
    if request.session.has_key('username'):
        del request.session['username']

    return HttpResponseRedirect('/login')