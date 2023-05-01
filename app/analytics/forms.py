from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired
from app.analytics.file_extension_validation import FileExtensionValidator

class UploadForm(FlaskForm):
    file = FileField('File', validators=[DataRequired(), FileExtensionValidator(['.csv', '.xlsx'])])
