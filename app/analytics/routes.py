from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from app.analytics import bp
from app.analytics.forms import UploadForm
from app.analytics.services import extract_data

@bp.route('/analytics_upload', methods=['GET', 'POST'])
@login_required
def analytics_upload():
    form = UploadForm()
    
    if form.validate_on_submit():
        file = form.file.data
        filename = form.file.data.filename
        # Read the file into a pandas dataframe and update the database
        url, message = extract_data(file, filename)
        flash(message)
        next_page = url_for(url)
        return redirect(next_page)
    
    return render_template('analytics/analytics_upload.html', title="upload form", form=form)