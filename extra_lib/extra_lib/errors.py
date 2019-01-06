import sys
import system
def print_fail(message, end = '\n'):
    sys.stderr.write(message.strip() + end)


def print_pass(message, end = '\n'):
    sys.stdout.write(message.strip() + end)


def print_warn(message, end = '\n'):
    sys.stderr.write(message.strip() + end)


def print_info(message, end = '\n'):
    sys.stdout.write(message.strip() + end)


def print_bold(message, end = '\n'):
    sys.stdout.write(message.strip() + end)
class NoEnterError(NameError):
    NoEnterError = Exception
    'no enter get'
class TimeOutError(Exception):
    'timed out'
class ReqeustError(Exception):
    'no response'
class WinError(Exception):
    'win error'
error = Exception
def fail(pas):
    print_fail(pas) 
def warning(error):
    print_warn(error)
def warn(mes):
    if not mes == str:
        str(mes)
    import sys
    print(mes, file=sys.stderr)
def print_warn(mes):
    warn(mes)
def show_warn(mes):
    warn(mes)
def error_warn(mes, error):
    warn(mes)
    try:
        raise error
    except Exception as ex:
        
        if ex == error:
            pass
            
        else:
            warn('a error is found:')
            warn(ex)
            warn('whe cant riase the error that you want')
            if ex == SyntaxError:
                raise SystemExit
            else: raise SystemExit
        






    




