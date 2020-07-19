from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///mydb.db")
session = sessionmaker(bind=engine)()

Base = declarative_base()

class Asistencia(Base):

    __tablename__ = "asistencia"

    estudiante_id = Column(String, primary_key=True)
    nombre = Column(String(30))
    apellido = Column(String(30))
    materia = Column(String(30))

    def __init__(self, estudiante_id, nombre, apellido, materia):
        self.estudiante_id = estudiante_id
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia

asistencia = Asistencia(1,"Juan","Duran","Programacion")
asistencia2 = Asistencia(2,"pedro","Ortiz","Programacion")
asistencia3 = Asistencia(3,"Luis","Gutierrez","Programacion")
asistencia4 = Asistencia(4,"Erika","Muños","Programacion")
asistencia5 = Asistencia(5,"Jose","Perez","Programacion")
asistencia6 = Asistencia(6,"Carlos","Martinez","Programacion")
asistencia7 = Asistencia(7,"Miguel","Herrera","Programacion")
asistencia8 = Asistencia(8,"Roberto","Varela","Programacion")
asistencia9 = Asistencia(9,"Laura","Salazar","Programacion")
asistencia10 = Asistencia(10,"Andrea","Tuñon","Programacion")

session.add_all([asistencia, asistencia2, asistencia3, asistencia4, asistencia5, asistencia6, asistencia7, asistencia8, asistencia9, asistencia10])
session.commit()


