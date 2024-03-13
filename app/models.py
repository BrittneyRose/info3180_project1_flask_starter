from . import db


class PropertyProfile(db.Model):

    __tablename__ = 'property_profiles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(128))
    room_num = db.Column(db.String(80))
    bathroom_num = db.Column(db.String(80))
    price = db.Column(db.String(80))
    property_type = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo_filename = db.Column(db.String(80))

  