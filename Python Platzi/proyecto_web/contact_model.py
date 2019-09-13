from google.appengine.ext import ndb

class Contact(ndb.model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()
