from wtforms.validators import ValidationError

class FileExtensionValidator:
    def __init__(self, allowed_extensions):
        self.allowed_extensions = allowed_extensions

    def __call__(self, form, field):
        if field.data:
            filename = field.data.filename
            if not filename.lower().endswith(tuple(self.allowed_extensions)):
                raise ValidationError(f'Only {", ".join(self.allowed_extensions)} files are allowed.')
