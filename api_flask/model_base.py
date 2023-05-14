import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column, String, Text, Float, DateTime, func, ForeignKey, Table, JSON
from sqlalchemy.orm import class_mapper



db = SQLAlchemy()

class Base(db.Model):

    __abstract__  = True

    __private_list__ = list()

    id            = Column(Integer, primary_key=True)
    # date_created  = Column(DateTime,  default=func.current_timestamp())
    # date_modified = Column(DateTime,  default=func.current_timestamp(), onupdate=func.current_timestamp())

    def patchEntity(self, data):
        return patch_entity(self,data)
    
    @property
    def dictobj(self):
        return object_to_dict(self)
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        # db.session.add(self)
        db.session.commit()
    
    

def patch_entity(obj, data):
    mapper = class_mapper(obj.__class__)
    columns = [
        column.key for column in mapper.columns if column.key not in obj.__private_list__]
    def get_key_value(c): return (c, getattr(obj, c).isoformat()) if isinstance(
        getattr(obj, c), datetime.datetime) else (c, getattr(obj, c))
    for col in columns:
        col_data = data.get(col)
        # print("col col_data",col, col_data)
        if col_data:
            print("setiing", col, col_data)
            setattr(obj, col, col_data)
        # print("form obj", getattr(obj,col))
        # print("")
        if col_data == "":
            # if not getattr(obj, col):
            # print("setting empty from form")
            setattr(obj, col, None)
        # print("====================")

    return obj

def object_to_dict(obj, found=None, append_url=None):
    if found is None:
        found = set()
    mapper = class_mapper(obj.__class__)
    columns = [
        column.key for column in mapper.columns if column.key not in obj.__private_list__]
    def get_key_value(c): return (c, getattr(obj, c).isoformat()) if isinstance(
        getattr(obj, c), datetime.datetime) else (c, getattr(obj, c))
    out = dict()
    for c in columns:
        if isinstance(getattr(obj, c), datetime.datetime):
            out[c] = getattr(obj, c).isoformat()
            continue

        out[c] = getattr(obj, c)
        if append_url and c == 'image_path':
            out[c] = 'http://' + append_url + out[c]

    out['type'] = obj.__class__.__name__
    return out
    for name, relation in mapper.relationships.items():
        # print("name, relation", name,relation)
        # input()
        if name in obj.__private_list__:
            continue
        related_obj = getattr(obj, name)
        if related_obj is not None:
            if relation.uselist:
                out[name] = [object_to_dict(child, found, append_url)
                             for child in related_obj]
            else:
                out[name] = object_to_dict(related_obj, found, append_url)
    return out