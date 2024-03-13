from sqlalchemy import Column, Integer, String, Date, Text, DateTime,Boolean
from datetime import datetime
from ckanext.utch.logic.db import base,engine

class EstudianteModel(base):

    __tablename__ = "sga.Estudiante"

    id = Column(Integer, primary_key=True)
    SedeId = Column(Integer)
    GrupoId = Column(Integer)
    PersonaId = Column(Integer)
    JornadaId = Column(Integer)
    ModalidadId = Column(Integer)
    EstadoEstudianteId = Column(Integer)
    GradoEspecificoId = Column(Integer)
    Codigo = Column(String(50))
    Observacion = Column(Text)
    FechaCreacion = Column(DateTime)
    UsuarioCreacion = Column(String(50))
    FechaModificacion = Column(DateTime)
    UsuarioModificacion = Column(String(50))
    Migracion = Column(Boolean)