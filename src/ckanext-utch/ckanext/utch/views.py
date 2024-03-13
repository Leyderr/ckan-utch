from flask import Blueprint, jsonify, request
from ckanext.utch.logic.db import db_session,metadata
from ckanext.utch.models.estudiante_model import EstudianteModel
from sqlalchemy.exc import OperationalError
from sqlalchemy import select, Table
utch = Blueprint(
    "utch", __name__)


def get_blueprints():
    return [utch]

# @utch.teardown_app_request
# def shutdown_session(exception=None):
#     db_session.remove()


@utch.route("/utch", methods=["GET"])
def utch_test():
    try:
        estudiante_table = Table('Persona', metadata,schema='general', autoload=True)

        skip = int(request.args.get('skip', 0))
        limit = int(request.args.get('limit', 10))
        query = select([estudiante_table]).order_by(estudiante_table.c.Id).offset(skip).limit(limit)    
        # query_estudiante = db_session.query(EstudianteModel).order_by(EstudianteModel.id).offset(
        #     skip).limit(limit).all()
        results = db_session.execute(query)
        query_estudiante = results.fetchall()
        
        estudiante_data = [dict(row) for row in query_estudiante]
        
        return jsonify(estudiante_data)
        
    except OperationalError as e:
        print("Error de conexión a la base de datos:", e)

        return jsonify({"error": "Error de conexión a la base de datos",
                        "detail": str(e)})
