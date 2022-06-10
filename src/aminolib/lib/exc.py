class Except(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)
class CheckExceptions:
    def __init__(self,data):
    	raise Except(data)