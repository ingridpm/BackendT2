import pytz
import datetime

class Funcion():
    def __init__(self,nombre,horario):
        self.nombre = nombre
        self.horario = horario #"15:00"
        self.asistentes = []

    def disponible(self):
        timezone = pytz.timezone('America/Guatemala')
        fecha_completa = datetime.datetime.now(tz=timezone)
        hora = fecha_completa.strftime("%H")
        minutos = fecha_completa.strftime("%M")
        hora_actual = int(hora)
        min_actual = int(minutos)
        tiempo_funcion = self.horario.split(":")
        hora_funcion = int(tiempo_funcion[0])
        min_funcion = int(tiempo_funcion[1])
        if hora_actual>hora_funcion:
            return False
        elif hora_actual == hora_funcion:
            if min_actual > min_funcion:
                return False
        return True
    