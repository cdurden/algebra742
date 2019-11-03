@templated('Connect4.html')
@lti(request='session', error=error, app=app)
def connect4(lti=lti, assignment=None,q=None,i=None):
    return {}
