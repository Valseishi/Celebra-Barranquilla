from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# --- CONFIGURACIÓN DE CORREO SMTP CORREGIDA ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Corregido el servidor SMTP
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# Tu correo real desde donde se enviarán las notificaciones
app.config['MAIL_USERNAME'] = 'perezvillalbavalerie@gmail.com'

# Tu contraseña de aplicación de 16 caracteres generada en Google
app.config['MAIL_PASSWORD'] = 'odtq tghf glwo tvhw'

app.config['MAIL_DEFAULT_SENDER'] = 'perezvillalbavalerie@gmail.com'

# Inicialización de Flask-Mail (Debe ir abajo de las configuraciones)
mail = Mail(app)


# RUTA HOME
@app.route('/')
def home():
    return render_template('index.html')


# RUTA LOGIN
@app.route('/registro')
def login():
    return render_template('registro.html')


# --- RUTA PARA PROCESAR EL FORMULARIO DEL PROFESOR ---
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        # Captura exacta de los inputs 'name' del formulario
        nombre_remitente = request.form['nombre']
        correo_remitente = request.form['correo']
        mensaje_remitente = request.form['mensaje']
        
        # Correo destino (en este caso el mismo correo para pruebas)
        correo_del_profesor = "perezvillalbavalerie@gmail.com"
        
        # Estructura del correo electrónico
        msg = Message(
            subject=f"Nueva cotización de: {nombre_remitente}",
            recipients=[correo_del_profesor]
        )
        
        msg.body = f"""
        Has recibido un mensaje desde el formulario de Celebra Barranquilla:
        
        Nombre del Interesado: {nombre_remitente}
        Correo de contacto: {correo_remitente}
        
        Mensaje o Consulta:
        {mensaje_remitente}
        """
        
        try:
            mail.send(msg)
            print("¡Correo enviado exitosamente!") # Mensaje de confirmación en consola
        except Exception as e:
            print(f"Error al enviar correo: {str(e)}") # Muestra el error si algo falla
            
        # Redirección automática de vuelta a la página principal
        return redirect(url_for('home'))


# EJECUTAR SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)
