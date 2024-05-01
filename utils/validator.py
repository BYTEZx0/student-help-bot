import re 

def reg_check(reg):
    if re.match(r'^(NA)[0-9]{2}([A-Z]|[a-z]){4}[0-9]{2}$', reg):
        return True
    else:
        return False
    
def subject_code_check(model):
    if re.match(r'^[0-9][A-Z][0-9]{2}[A-Z]*$',model):
        return True
    else:
        return False
    
    