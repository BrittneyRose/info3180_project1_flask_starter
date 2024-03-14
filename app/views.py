"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import AddPropertyForm
from werkzeug.utils import secure_filename
from app.models import PropertyProfile
from flask import send_from_directory
from . import db
from app.config import Config
UPLOAD_FOLDER = Config.UPLOAD_FOLDER

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/create/', methods=['GET','POST'])
def create():
    form = AddPropertyForm()

    if form.validate_on_submit() and request.method == 'POST':
        title = form.title.data
        description = form.description.data
        room_num = form.room_num.data
        bathroom_num = form.bathroom_num.data
        price = form.price.data
        property_type = form.property_type.data
        location = form.location.data
        
        file = form.file.data
        filename = secure_filename(file.filename)
        destination_folder = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
        os.makedirs(destination_folder, exist_ok=True)
        file.save(os.path.join(app.root_path, UPLOAD_FOLDER, filename))

        property_profile = PropertyProfile(
            title=title,
            description=description,
            room_num=room_num,
            bathroom_num=bathroom_num,
            price=price,
            property_type=property_type,
            location=location,
            photo_filename=filename  
        )
        db.session.add(property_profile)
        db.session.commit()

        flash('Property was successfully added', 'success')
        return redirect(url_for('properties'))
    else:
        flash_errors(form)

    return render_template('create.html', form=form)


@app.route('/properties/', methods=['POST', 'GET'])
def properties():
    properties = PropertyProfile.query.all()
    return render_template('view_properties.html', properties=properties)

@app.route('/properties/<int:property_id>')
def property(property_id):
    property = PropertyProfile.query.get_or_404(property_id)
    return render_template('property.html', property=property)


def get_uploaded_images():
    rootdir = os.path.join(os.getcwd(), 'uploads')
    image_files =[]

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            image_files.append(file)
    return image_files

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


