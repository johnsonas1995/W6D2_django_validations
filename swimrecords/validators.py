import re
from django.core.exceptions import ValidationError
from django.utils import timezone

# def validate_first_name(name):
#     pattern = r"^(?!\s*$).+" #regex to match any string with at least one non-space character
#     match = re.search(pattern, name)
#     if not match:
#         print ('This field cannot be blank.')
#         raise ValidationError('This field cannot be blank.test')
    
def validate_stroke(stroke):
    pattern = {'front crawl', 'butterfly', 'breast', 'back', 'freestyle'}
    if stroke not in pattern:
        raise ValidationError(f'{stroke} is not a valid stroke')
    return stroke

def validate_record(record_date):
    if record_date > timezone.now():
        raise ValidationError("Can't set record in the future.")
    return record_date

def validate_record_broken(record_broken_date):
    
    if record_broken_date < timezone.now():
        raise ValidationError("Can't break record before record was set.")
    return record_broken_date
    

