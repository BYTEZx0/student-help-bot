import re 

def reg_check(reg):
    if re.match(r'^(NA)|(na)[0-9]{2}([A-Z]|[a-z]){4}[0-9]{2}$', reg):
        return True
    else:
        return False