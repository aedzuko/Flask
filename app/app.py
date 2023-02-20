from flask import Flask, render_template, request,redirect,url_for,jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sa'
app.config['MYSQL_PASSWORD'] = 'C@marazuko4C@marazuko4'
app.config['MYSQL_DB'] = 'adDIMEGESI'

conexion = MySQL(app)

@app.before_request
def before_request():
    print("Antes de la petición....")

@app.after_request
def afert_rquest(response):
    print("Después de la petición....")    
    return(response)

@app.route('/')
def index():
    #return "Hola sss"
    lista = ["A","B","C","D","E","F"]
    data = {
        'titulo':'DataBrain',
        'bienvenida':'Hello',
        'lista':lista,
        'long':len(lista)
    }
    return render_template('index.html',data=data)

#Función para pasar por parámetro de una Url 2 variables
@app.route('/contacto/<nombre>/<int:edad>') #Crea enlace a partir de un decorador
def contacto(nombre,edad):
    data = {
        'titulo':'Contacto',
        'nombre':nombre,
        'edad':edad
    }
    return render_template('contacto.html',data=data)

#Función para crear una query string 
def query_string():
    print(request)
    print(request.args)
    for args in request.args:
        print(request.args.get(args))
    return "Se pasaron las variables con ?param1=x & param2=y"  #Una vista debe de tener siempre return
    
@app.route('/cursos')
def listar_tabla():
    data={}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT [CIDDOCUMENTO] FROM [adDIMEGESI].[dbo].[admDocumentos]"
        cursor.execute(sql)
        tabla = cursor.fetchall()
        data['mensaje']='Succes!'
    except Exception as ex:
        data['mensaje']= 'Error...'
    return jsonify(data)

def pagina_no_encontrada(error):
    #return render_template('404.html'), 404          #Retorna un nuevo template html con la información de página no encontrada
    return redirect(url_for('index'))                 #En caso de no econtrar la url te redirecciona al índice   

if __name__== '__main__':
    app.add_url_rule('/query_string',view_func=query_string)  #declaración del nombre de la url utilizada para usar la función query_string
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True, port=5000)