import crud_academico
db = crud_academico.crud()

class crud_alumno:
    def consultar(self):
        #return db.consultar("SELECT * FROM alumnos WHERE nombre like '%" + buscar["buscar"] + "%'")
        return db.consultar("SELECT * FROM alumnos")
    
    def administrar(self, datos):

        if(datos["accion"] == "nuevo"):
         sql = """
            INSERT INTO alumnos (codigo, nombre, direccion, telefono, email)
            VALUES (%s, %s, %s, %s, %s) 
        """
        elif(datos["accion"] == "modificar"):
         sql = """
            UPDATE alumno
            SET codigo = %s, nombre = %s, direccion = %s, telefono = %s, email = %s
            WHERE idAlumno = %s
        """
         valores = (datos["codigo"], datos["nombre"], datos["direccion"], datos["telefono"], datos["correo"], datos["idalumno"])

        elif (datos["accion"] == "eliminar"):
         sql = """
            DELETE FROM alumno
            WHERE idAlumno = %s
        """
        valores = (datos["idalumno"],)
        return db.procesar_consultas(sql, valores)