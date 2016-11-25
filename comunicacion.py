#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

import webapp2
import json
import jinja2
import time
import logging
import datetime
import pytz


from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import app_identity
from google.appengine.api import mail
from pytz.gae import pytz
from pytz import timezone

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

class PruebaDB(ndb.Model):
    nombre = ndb.StringProperty()
    fecha_registro = ndb.DateTimeProperty()

class ProveedorDB(ndb.Model):
    nombre = ndb.StringProperty()
    nit = ndb.StringProperty()
    direccionOficina = ndb.StringProperty()
    ciudadOficina = ndb.StringProperty()
    direccionBodega = ndb.StringProperty()
    ciudadBodega = ndb.StringProperty()
    alistamientoDiario = ndb.StringProperty()
    alistamientoDiarioEvento = ndb.StringProperty()
    contactoComercial = ndb.StringProperty()
    transportista = ndb.StringProperty()
    contactos = ndb.JsonProperty()


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def get_user():
        user = users.get_current_user()
        return user

class MainHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class GuardarProveedor(MainHandler):
    def post(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        nombre = self.request.get('nombre').upper().replace(',',' ')
        nit = self.request.get('nit').upper().replace(',',' ')
        direccionOficina = self.request.get('direccionOficina').upper().replace(',',' ')
        ciudadOficina = self.request.get('ciudadOficina').upper().replace(',',' ')
        direccionBodega = self.request.get('direccionBodega').upper().replace(',',' ')
        ciudadBodega = self.request.get('ciudadBodega').upper().replace(',',' ')
        lineaProductos = self.request.get('lineaProducto').upper().replace(',',' ')
        enviosDiaNormal = self.request.get('enviosDiaNormal').upper().replace(',',' ')
        enviosDiaEvento = self.request.get('enviosDiaEvento').upper().replace(',',' ')
        comercialAsignado = self.request.get('comercialAsignado').upper().replace(',',' ')
        transportista = self.request.get('operador').upper().replace(',',' ')

        # argumentos = self.request.arguments()
        # proveedor = {}
        # for argumento in argumentos:
        #     proveedor[argumento] = self.request.get(argumento)

        # ProveedorDB(proveedor = proveedor).put()
        # self.response.write(proveedor)
        contacto1 = {'nombre':self.request.get('contactos[0][nombreContacto]').upper().replace(',',' '), 'cargo':self.request.get('contactos[0][cargoContacto]').upper().replace(',',' '), 'telefono':self.request.get('contactos[0][telefonoContacto]').upper().replace(',',' '), 'celular':self.request.get('contactos[0][celularContacto]').upper().replace(',',' '), 'email':self.request.get('contactos[0][emailContacto]').lower().replace(',',' '), 'tipo_contacto':self.request.get('contactos[0][tipoContacto]').upper().replace(',',' ')}
        contacto2 = {'nombre':self.request.get('contactos[1][nombreContacto]').upper().replace(',',' '), 'cargo':self.request.get('contactos[1][cargoContacto]').upper().replace(',',' '), 'telefono':self.request.get('contactos[1][telefonoContacto]').upper().replace(',',' '), 'celular':self.request.get('contactos[1][celularContacto]').upper().replace(',',' '), 'email':self.request.get('contactos[1][emailContacto]').lower().replace(',',' '), 'tipo_contacto':self.request.get('contactos[1][tipoContacto]').upper().replace(',',' ')}
        contacto3 = {'nombre':self.request.get('contactos[2][nombreContacto]').upper().replace(',',' '), 'cargo':self.request.get('contactos[2][cargoContacto]').upper().replace(',',' '), 'telefono':self.request.get('contactos[2][telefonoContacto]').upper().replace(',',' '), 'celular':self.request.get('contactos[2][celularContacto]').upper().replace(',',' '), 'email':self.request.get('contactos[2][emailContacto]').lower().replace(',',' '), 'tipo_contacto':self.request.get('contactos[2][tipoContacto]').upper().replace(',',' ')}
        contacto4 = {'nombre':self.request.get('contactos[3][nombreContacto]').upper().replace(',',' '), 'cargo':self.request.get('contactos[3][cargoContacto]').upper().replace(',',' '), 'telefono':self.request.get('contactos[3][telefonoContacto]').upper().replace(',',' '), 'celular':self.request.get('contactos[3][celularContacto]').upper().replace(',',' '), 'email':self.request.get('contactos[3][emailContacto]').lower().replace(',',' '), 'tipo_contacto':self.request.get('contactos[3][tipoContacto]').upper().replace(',',' ')}
        contacto5 = {'nombre':self.request.get('contactos[4][nombreContacto]').upper().replace(',',' '), 'cargo':self.request.get('contactos[4][cargoContacto]').upper().replace(',',' '), 'telefono':self.request.get('contactos[4][telefonoContacto]').upper().replace(',',' '), 'celular':self.request.get('contactos[4][celularContacto]').upper().replace(',',' '), 'email':self.request.get('contactos[4][emailContacto]').lower().replace(',',' '), 'tipo_contacto':self.request.get('contactos[4][tipoContacto]').upper().replace(',',' ')}
        contacto6 = {'nombre':self.request.get('contactos[5][nombreContacto]').upper().replace(',',' '), 'cargo':self.request.get('contactos[5][cargoContacto]').upper().replace(',',' '), 'telefono':self.request.get('contactos[5][telefonoContacto]').upper().replace(',',' '), 'celular':self.request.get('contactos[5][celularContacto]').upper().replace(',',' '), 'email':self.request.get('contactos[5][emailContacto]').lower().replace(',',' '), 'tipo_contacto':self.request.get('contactos[5][tipoContacto]').upper().replace(',',' ')}
        contacto7 = {'nombre':self.request.get('contactos[6][nombreContacto]').upper().replace(',',' '), 'cargo':self.request.get('contactos[6][cargoContacto]').upper().replace(',',' '), 'telefono':self.request.get('contactos[6][telefonoContacto]').upper().replace(',',' '), 'celular':self.request.get('contactos[6][celularContacto]').upper().replace(',',' '), 'email':self.request.get('contactos[6][emailContacto]').lower().replace(',',' '), 'tipo_contacto':self.request.get('contactos[6][tipoContacto]').upper().replace(',',' ')}

        contactos = json.dumps([contacto1, contacto2, contacto3, contacto4, contacto5, contacto6, contacto7])

        ProveedorDB(nombre = nombre,
                    nit = nit,
                    direccionOficina = direccionOficina,
                    ciudadOficina = ciudadOficina,
                    direccionBodega = direccionBodega,
                    ciudadBodega = ciudadBodega,
                    alistamientoDiario = enviosDiaNormal,
                    alistamientoDiarioEvento = enviosDiaEvento,
                    contactoComercial = comercialAsignado,
                    transportista = transportista,
                    contactos = contactos).put()

        self.response.write('Registrado')

    def get(self):
        self.response.write('GET yeah!!')

def send_approved_mail(sender_address):
    # [START send_mail]
    mail.send_mail(sender=sender_address,
                   to="carlos.torres.co@gmail.com",
                   subject="Nuevo registro - Formulario proveedores FACO",
                   body="""Dear Albert:
Your example.com account has been approved.  You can now visit
http://www.example.com/ and sign in using your Google Account to
access new features.
Please let us know if you have any questions.
The example.com Team
""")
    # [END send_mail]


class sendEmail(MainHandler):
    def get(self):
        send_approved_mail('falabellanewsletter@gmail.com'.format(app_identity.get_application_id()))
        self.response.content_type = 'text/plain'
        self.response.write('Sent an email to Albert.'+ app_identity.get_application_id())


class fecha(webapp2.RequestHandler):
    def get(self):
        i = datetime.datetime.now()

        self.response.write("dd/mm/yyyy format =  %s/%s/%s" % (i.day, i.month, i.year))
        self.response.write(pytz.all_timezones);

        PruebaDB(nombre = 'Test',
                    fecha_registro = i).put()

class SacarProveedores(MainHandler):
    def post(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'application/json'
        datos_email = [p.to_dict(exclude = ['fecha_envio']) for p in ProveedorDB.query().fetch()]
        self.response.write(json.dumps(datos_email))
    def get(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'application/json'
        datos_email = [p.to_dict(exclude = ['fecha_envio']) for p in ProveedorDB.query().fetch()]
        self.response.write(json.dumps(datos_email))


app = webapp2.WSGIApplication([('/guardar_proveedor', GuardarProveedor),
                               ('/sacar_proveedores', SacarProveedores), 
                               ('/email', sendEmail),
                               ('/fecha', fecha)],
                              debug=True)