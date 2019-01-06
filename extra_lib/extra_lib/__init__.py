from subprocess import *
from time import *
from extra_lib.errors import *
from datetime import *
class system:
    import slib as sl
    import os
    import sys
    
    import socket
    import socket as s
    
    import time as _time
    try:
        import tkinter, time, subprocess as sub, extra_lib.wifi as wifi, extra_lib.tijd as tijd, extra_lib.datetijd as datetijd, extra_lib.rekenen as rekenen, subprocess, extra_lib.slib as slib
    except ImportError or NameError:
        print('please wait for a update this is my first time i make a thing i open a link so you can mail me.')
        print('i hope you undestand')
        import tkinter, time, subprocess as sub, extra_lib.wifi, tijd, datetijd, extra_lib.rekenen, subprocess, extra_lib.slib
    main_dir = sl.main_dir
    working = True
    def w():
        global working
        working = True
    def ww():
        global working
        working = False
    def cmd(command):
        return getstatusoutput(command)

    def info(function):
        
        
        
        print(dir(function))
        print(help(function))
    def info_o(function):
        
        import turtle as t
        import turtle
        import tklib, tlib
        print(dir(function))
        print(help(function))
    def win_version():
        import sys
        is_windows = hasattr(sys, 'getwindowsversion')
        return is_windows
    def cmd_filter_haak(op):
        def cmd(command):
            return getstatusoutput(command)
        net = cmd(op)
        
        net_bericht = str(net)
        if '[' in net_bericht:
            haak = '['
            haak2 = ']'
        elif '{' in net_bericht:
            haak = '{'
            haak2 = '}'
        elif '(' in net_bericht:
            haak = '('
            haak2 = ')'
        else:
            print('not a cmd output to filter')
            raise ValueError('geen haken gevonden om op te filteren')
        berijk = range(0, len(net_bericht))
        go = False
        now = False
        message = ''
        for i in berijk:
            
            if net_bericht[i] == haak or go == True or now == True:
                if go == True:
                    if not net_bericht[i] == haak2:
                        message += net_bericht[i]
                go = True
                if net_bericht[i] == haak2:
                    go = False
                    if haak in net_bericht or not haak in net_bericht:
                        now = True
                        go = False
                        if '[' in net_bericht:
                            haak = '['
                            haak2 = ']'
                        elif '{' in net_bericht:
                            haak = '{'
                            haak2 = '}'
                        elif '(' in net_bericht:
                            haak = '('
                            haak2 = ')'
                        else:
                            go = False
                            break
                        continue
        return message
    cmd_filter_haak('ping')
    def filter_zin(zine):
        zin = ''
        into = ''
        f = 0
        lrn = str(zine)
        print(lrn)
        berijk = range(0, len(lrn))
        for i in berijk:
            if i < int(len(lrn) - 1):
                into = into + lrn[int(i)] + lrn[int(i + 1)]
            else: continue
            if '\n' in into:
                zin = zin + into + '\n'
                print(zin)
                into = ''
        return zin
    def filter_regel(zinig):
        if not zinig == str:
            zinig = str(zinig)
        OUTPUT = zinig
        if '0, ' in OUTPUT:
            OUTPUT = OUTPUT.replace('0, ', '')
        
        OUTPUT = OUTPUT.replace('(\'', '')
        OUTPUT = OUTPUT.replace('\')', '')
        formatted_output = OUTPUT.replace('\\n', '\n')
        return formatted_output
    def data():
        return cmd('ping -n 10 -l 1000 8.8.8.8')    
    def cmd_out_list(command_or_data):
        def filter_regel(zinig):
            if not zinig == str:
                zinig = str(zinig)
            OUTPUT = zinig
            if '0, ' in OUTPUT:
                OUTPUT = OUTPUT.replace('0, ', '')
            
            OUTPUT = OUTPUT.replace('(\'', '')
            OUTPUT = OUTPUT.replace('\')', '')
            formatted_output = OUTPUT.replace('\\n', '\n')
            return formatted_output
        def cmd(command):
            return getstatusoutput(command)
        try:
            e = filter_regel(cmd(command_or_data))
            li = str(cmd(command_or_data)).split(sep='\\n')
        except TypeError:
            try:
                e = filter_regel(command_or_data)
                li = str(command_or_data).split(sep='\\n')
            except Exception as ex:
                print('a error raised')
                raise ex('error')
        return [e, li]
    def cmd_out(command_or_data):
        def filter_regel(zinig):
            if not zinig == str:
                zinig = str(zinig)
            OUTPUT = zinig
            if '0, ' in OUTPUT:
                OUTPUT = OUTPUT.replace('0, ', '')
            
            OUTPUT = OUTPUT.replace('(\'', '')
            OUTPUT = OUTPUT.replace('\')', '')
            formatted_output = OUTPUT.replace('\\n', '\n')
            return formatted_output
        def cmd(command):
            return getstatusoutput(command)
        try:
            e = filter_regel(cmd(command_or_data))
            li = str(cmd(command_or_data)).split(sep='\\n')
        except TypeError:
            try:
                e = filter_regel(command_or_data)
                li = str(command_or_data).split(sep='\\n')
            except Exception as ex:
                print('a error raised')
                raise ex('error')
        return e
    import sys

    # Colored printing functions for strings that use universal ANSI escape sequences.
    # fail: bold red, pass: bold green, warn: bold yellow, 
    # info: bold blue, bold: bold white

    class ColorPrint:

        @staticmethod
        def print_fail(message, end = '\n'):
            sys.stderr.write(message.strip())

        @staticmethod
        def print_pass(message, end = '\n'):
            sys.stdout.write(message.strip())

        @staticmethod
        def print_warn(message, end = '\n'):
            sys.stderr.write(message.strip())

        @staticmethod
        def print_info(message, end = '\n'):
            sys.stdout.write(message.strip())

        @staticmethod
        def print_bold(message, end = '\n'):
            sys.stdout.write(message.strip())
    if __name__ == '__main__':
        import time
        start = time.time()
        try:
            cmd('arp -a')
        except Exception as ex:
            print_warn(ex)
            working = False
            pass
        stop = time.time()
        re = stop - start
        if working == True:
            print('func cmd(arp -a) state: working.\nwifi: True\nping module importable: True\ntime to compleet func: ' + str(re))
        start = time.time()
        
        try:
            win_version()
        except Exception as ex:
            print_warn(ex)
            working = False
            pass
        stop = time.time()
        re = stop - start
        if working == True:
            print('func win_version state: working.\nwin_version module importable: True\ntime to compleet func: ' + str(re))
        start = time.time()
        w()
        try:
            cmd_filter_haak('arp -a')
        except Exception as ex:
            print_warn(ex)
            ww()
            pass
        stop = time.time()
        re = stop - start
        if working == True:
            print('func cmd_filter_haak(arp -a) state: working.\nwifi: True\nfilter_haak module importable: True\ntime to compleet func: ' + str(re))
        w()
        try:
            filter_regel('arp -a')
        except Exception as ex:
            print_warn(ex)
            ww()
            pass
        stop = time.time()
        re = stop - start
        if working == True:
            print('func filter_regel(arp -a) state: working.\nwifi: True\nfilter_regel module importable: True\ntime to compleet func: ' + str(re))
        w()
        try:
            cmd_out_list('arp -a')
        except Exception as ex:
            print_warn(ex)
            ww()
            pass
        stop = time.time()
        re = stop - start
        if working == True:
            print('func cmd_out_list(arp -a) state: working.\nwifi: True\ncmd_out_list module importable: True\ntime to compleet func: ' + str(re))
        w()
        try:
            cmd_out('arp -a')
        except Exception as ex:
            print_warn(ex)
            ww()
            pass
        stop = time.time()
        re = stop - start
        if working == True:
            print('func cmd_out(arp -a) state: working.\nwifi: True\ncmd_out module importable: True\ntime to compleet func: ' + str(re))
        w()
        import getpass
        print(getpass.getuser())
class time_modules:
    class datetijd:
        import time as _time
        
        import tijd
        
        import sys
        t = datetime.today()
        import time as _time

        def time_zone():
                LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo
                timez_zone = str(LOCAL_TIMEZONE)
                return timez_zone
        def tijd_en_datum_nu(waarde):
            now = datetime.now()
            
            if waarde.upper() == 'TONEN_TIJD':
                print("de tijd en datum nu is :", end=' ')
                print(now.strftime("%Y-%m-%d %H:%M:%S"), end=' en de tijd in sec sinds 1970 is: ')
                print(_time.time())
                RETURN = str(now.strftime("%Y-%m-%d %H:%M:%S")) + ' tijd sinds 1970: ' + str(_time.time())
                return RETURN
            elif waarde.upper() == 'TONEN_NU':
                print("de tijd en datum nu is :", end=' ')
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
                return now.strftime("%Y-%m-%Y %H:%M:%S")
            elif waarde.upper() == 'RETURN_TIJD':
                RETURN = str(now.strftime("%Y-%m-%d %H:%M:%S")) + ' tijd sinds 1970: ' + str(_time.time())
                return RETURN
                
            elif waarde.upper() == 'RETURN_NU':
                return [int(now.strftime("%Y")), int(now.strftime("%m")), int(now.strftime("%d")), int(now.strftime("%H")), int(now.strftime("%M")), int(now.strftime("%S"))]
            else:
                print('ongeldig commando')


        def maand(ma ,taal):
            now = datetime.now()
            nummer = now.strftime('%m')
            nummer = int(nummer)
            nummer = nummer - 1 #omdat python begint bij lijsten het tellen vanaf 0 inplaats van 1 en het is dan niet 1 tm 12 maar 0 tm 11
            RETURN = True
            if ma.lower() == 'nu': man = True
            else: man = False
            if taal.upper() == 'NL_AF': # NL_AF is een afkorting van NEDERLANDSE_AFKORTINGEN
                maanden = ['jan', 'feb', 'ma', 'ap', 'mei', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec']
            elif taal.upper() == 'NL':
                maanden = ['januari', 'februarie', 'maaart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']
            elif taal.upper() == 'FR':
                maanden = ['Janvier', 'Février', 'Mars', 'Avril', 'mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Décembre']
            elif taal.upper() == 'FR_AF': #FR_AF is een afkorting van FRANSE_AFKORTINGEN
                maanden = ['Janvier', 'Fév', 'Mar', 'Avr', 'mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Déc']
            elif taal.upper() == 'ENG':
                maanden = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            elif taal.upper() == 'ENG_AF':
                maanden = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            else:
                RETURN = False
                print('ongeldig commando')
            if RETURN == True:
                if man == True:
                    return maanden[nummer]
                else:
                    return maanden
            



        def dag_vandaag():
            print('counting from 1970')
            tijd = _time.time()
            tijd = tijd / 60
            tijd = tijd / 60
            tijd = tijd / 24
            tijd = int(tijd)
            
            return tijd
        def dag_vandaag_jaar():
            
            tijd = _time.time()
            tijd = tijd / 60
            tijd = tijd / 60
            tijd = tijd / 24
            tijd = int(tijd)
            times = int(tijd / 365)
            min_ = times * 365
            schrik = int(times / 4)
            schrik = schrik - 1# omdat het jaar 2000 geen schrikkel jaar was
            tijd = tijd - (min_ + schrik)
            return tijd
        def dag(taal):
            taal = taal.lower()
            if taal == 'eng':
                wochentag = ["Monday", "Tuesday", "Wednesday",
                        "Thursday", "Friday", "Saturday", "Sunday"]
            elif taal == 'nl':
                wochentag = ["maandag", "dinsdag", "woensdag",
                        "donderdag", "vrijdag", "zaterdag", "zondag"]
            
            elif taal == 'fr':
                wochentag = ["lundi", "mardi", "mercredi",
                        "jeudi", "vendredi", "samedi", "dimanche"]

            elif taal == 'de':
                wochentag = ["Montag", "Dienstag", "Mittwoch",
                        "Donnerstag", "Freitag", "Samstag", "Sonntag"]
            else:
                wochentag = ["error", "error", "error",
                        "error", "error", "error", "error"]
            
            return wochentag[t.weekday()]
        def dagen(taal):
            taal = taal.lower()
            if taal == 'eng':
                wochentag = ["Monday", "Tuesday", "Wednesday",
                        "Thursday", "Friday", "Saturday", "Sunday"]
            elif taal == 'nl':
                wochentag = ["maandag", "dinsdag", "woensdag",
                        "donderdag", "vrijdag", "zaterdag", "zondag"]
            
            elif taal == 'fr':
                wochentag = ["lundi", "mardi", "mercredi",
                        "jeudi", "vendredi", "samedi", "dimanche"]

            elif taal == 'de':
                wochentag = ["Montag", "Dienstag", "Mittwoch",
                        "Donnerstag", "Freitag", "Samstag", "Sonntag"]
            else:
                wochentag = ["error", "error", "error",
                        "error", "error", "error", "error"]
            
            return wochentag
        def day_to(dag):
            var = tijd.dagen_tot(dag)
            return var
        def times_and_days_pam():
            from time import gmtime, strftime
            import time as _time
            tijd_gmt = _time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", _time.gmtime())
            tijd_local = strftime("%a, %d %b %Y %I:%M:%S %p %Z\n")
            tijd_int_local = [int(strftime("%d")), int(strftime("%m")), int(strftime("%Y")), int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]
            tijd_int_gmt = [int(_time.strftime("%d", _time.gmtime())), int(_time.strftime("%m", _time.gmtime())), int(_time.strftime("%Y", _time.gmtime())), int(_time.strftime("%H", _time.gmtime())), int(_time.strftime("%M", _time.gmtime())), int(_time.strftime("%S", _time.gmtime()))]

            return [tijd_gmt, tijd_int_gmt, tijd_local, tijd_int_local]
        def times_pam():
            from time import gmtime, strftime
            import time as _time
            tijd_gmt = _time.strftime("%I:%M:%S %p %Z", _time.gmtime())
            tijd_local = strftime("%I:%M:%S %p %Z")
            tijd_int_local = [int(strftime("%d")), int(strftime("%m")), int(strftime("%Y")), int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]
            tijd_int_gmt = [int(_time.strftime("%d", _time.gmtime())), int(_time.strftime("%m", _time.gmtime())), int(_time.strftime("%Y", _time.gmtime())), int(_time.strftime("%H", _time.gmtime())), int(_time.strftime("%M", _time.gmtime())), int(_time.strftime("%S", _time.gmtime()))]

            return [tijd_gmt, tijd_int_gmt, tijd_local, tijd_int_local]
        def times():
            from time import gmtime, strftime
            import time as _time
            tijd_gmt = _time.strftime("%H:%M:%S(gmt)", _time.gmtime())
            tijd_local = strftime("%H:%M:%S")
            tijd_int_local = [int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]
            tijd_int_gmt = [int(_time.strftime("%H", _time.gmtime())), int(_time.strftime("%M", _time.gmtime())), int(_time.strftime("%S", _time.gmtime()))]
            return [tijd_gmt, tijd_int_gmt, tijd_local, tijd_int_local]
        def times_and_days():
            from time import gmtime, strftime
            import time as _time
            tijd_gmt = _time.strftime("%d/%m/%Y  %H:%M:%S %Z(gmt)", _time.gmtime())
            tijd_local = strftime("%d/%m/%Y  %H:%M:%S %Z")
            tijd_int_local = [int(strftime("%d")), int(strftime("%m")), int(strftime("%Y")), int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]
            tijd_int_gmt = [int(_time.strftime("%d", _time.gmtime())), int(_time.strftime("%m", _time.gmtime())), int(_time.strftime("%Y", _time.gmtime())), int(_time.strftime("%H", _time.gmtime())), int(_time.strftime("%M", _time.gmtime())), int(_time.strftime("%S", _time.gmtime()))]
            return [tijd_gmt, tijd_int_gmt, tijd_local, tijd_int_local]
        def days():
            from time import gmtime, strftime
            import time as _time
            tijd_gmt = _time.strftime("%d/%m/%Y")
            tijd_local = strftime("%d/%m/%Y")
            tijd_int_local = [int(strftime("%d")), int(strftime("%m")), int(strftime("%Y"))]
            tijd_int_gmt = [int(_time.strftime("%d", _time.gmtime())), int(_time.strftime("%m", _time.gmtime())), int(_time.strftime("%Y", _time.gmtime()))]
            return [tijd_gmt, tijd_int_gmt, tijd_local, tijd_int_local]
        def days_local():
            from time import gmtime, strftime
            import time as _time
            tijd_gmt = _time.strftime("%d/%m/%Y")
            tijd_local = strftime("%d/%m/%Y")
            tijd_int_local = [int(strftime("%d")), int(strftime("%m")), int(strftime("%Y"))]
            tijd_int_gmt = [int(_time.strftime("%d", _time.gmtime())), int(_time.strftime("%m", _time.gmtime())), int(_time.strftime("%Y", _time.gmtime()))]
            return [tijd_local, tijd_int_local]
        def times_local():
            from time import gmtime, strftime
            import time as _time
            tijd_gmt = _time.strftime("%H:%M:%S(gmt)", _time.gmtime())
            tijd_local = strftime("%H:%M:%S")
            tijd_int_local = [int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]
            tijd_int_gmt = [int(_time.strftime("%H", _time.gmtime())), int(_time.strftime("%M", _time.gmtime())), int(_time.strftime("%S", _time.gmtime()))]
            return [tijd_local, tijd_int_local]
        def times_local_pam():
            ret = []
            ret.append(times_pam()[2])
            ret.append(times_pam()[3])
            return ret
        def times_and_days_local():
            from time import gmtime, strftime
            import time as _time
            tijd_gmt = _time.strftime("%d/%m/%Y  %H:%M:%S %Z(gmt)", _time.gmtime())
            tijd_local = strftime("%d/%m/%Y  %H:%M:%S %Z")
            tijd_int_local = [int(strftime("%d")), int(strftime("%m")), int(strftime("%Y")), int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]
            tijd_int_gmt = [int(_time.strftime("%d", _time.gmtime())), int(_time.strftime("%m", _time.gmtime())), int(_time.strftime("%Y", _time.gmtime())), int(_time.strftime("%H", _time.gmtime())), int(_time.strftime("%M", _time.gmtime())), int(_time.strftime("%S", _time.gmtime()))]
            return [tijd_local, tijd_int_local]
        def info():
                '''
        tijd_en_datum_nu(value) = command to retutn or print

        tijd_zone() = returns your time zone
        times_and_days_pam(): returns the date and time of gmt and local
        times_and_days() = returns date and time  of gmt and local in 0 to 24 not in pm or am
        times_pam() = returns the time gmt and local in pm or am
        times() = returns the time gmt and local not in pm or am
        days() = returns the day in gmt and in local
        '''
        def loop():
            pass
        if __name__ == '__main__':
            try:
                print(time_zone())
                work = True
            except Exception as ex:
                print_warn(str(ex))
                work = False
                pass
            if work == True:
                print('func time_zone() state: working.\nmodule importable: True\n')
            import datetijd
        class tijd:
            

            import datetime as _datetime
            def fil(x):
                if x == str:
                    return True
                else:
                    return False
            def tijd_zone():
                    LOCAL_TIMEZONE = _datetime.datetime.now(_datetime.timezone.utc).astimezone().tzinfo
                    LOCAL_TIMEZONE = str(LOCAL_TIMEZONE)
                    return LOCAL_TIMEZONE
            def chek(a):
                    b = time()
                    c = b - a
                    return c
            def nu(waarde):
                
                now = _datetime.datetime.now()
                if waarde.lower() == 'tonen' or 'print':
                    print ("de tijd en datum nu is :")
                    print (now.strftime("%Y-%m-%d %H:%M:%S"))
                    return now.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    return now.strftime("%Y-%m-%d %H:%M:%S")
            def dagen_voorbij_in_dit_jaar(RETURN):
                    tijd = time()
                    tijd = tijd / 60
                    tijd = tijd / 60
                    tijd = tijd / 24
                    tijd = int(tijd)
                    jaren = int(tijd / 365)
                    dagen = jaren * 365
                    schrik = int(jaren / 4)
                    
                    tijd = tijd - (dagen + schrik - 1)#omdat het jaar 2000 geen schrikkeljaar was
                    if not RETURN.upper() == 'RETURN':
                            print(tijd)
                    else:
                            return tijd


            def tijd_nu(uur, minuten, sec):
                    now = _datetime.datetime.now()
                    nu = ''
                    if sec.lower() == 'ja' or 'yes':
                            nu = nu +now.strftime('%H')
                    if sec.lower() and minuten.lower() or sec.lower() and uur.lower() == 'ja' or 'yes':
                            nu = nu + ':'
                    if minuten.lower() == 'ja' or 'yes':
                            nu = nu + now.strftime('%M')
                    if minuten.lower() and uur.lower() == 'ja' or 'yes':
                            nu = nu + ':'
                    if uur.lower() == 'ja' or 'yes':
                            nu = nu + now.strftime('%S')
                    return nu
            def dagen_tot(dag):
                    jaar = 0
                    dag = str(dag)
                    if dag.lower() == 'nieuw jaar':
                            output = 365 - dagen_voorbij_in_dit_jaar('return')
                    dag = int(dag)
                    if dag >= 365:
                            while dag >= 365:
                                    jaar = jaar + 1
                    else:
                            
                            output = dag - dagen_voorbij_in_dit_jaar('RETURN')
                    if output < 0:
                            o = 365 - dagen_voorbij_in_dit_jaar('return')
                            no = dag
                            output = o + no
                    if jaar > 0:
                            return [jaar, output]
                    elif jaar == 0:
                            return output
                    else:
                            raise Exception
            def loading_c(duur, command):
                    a = time()
                    
                    while chek(a) < duur:
                        print('|', end='')
                        sleep(0.1)
                    print(end='\n')
            def loading(duur):
                    a = time()
                    while chek(a) < duur:
                            print('|', end='')
                            sleep(0.1)
                    print(end='\n')
            def times_and_days_pam():
                from time import gmtime, strftime
                import time as _time
                tijd_gmt = _time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", _time.gmtime())
                tijd_local = strftime("%a, %d %b %Y %I:%M:%S %p %Z\n")
                tijd_int_local = [int(strftime("%d")), int(strftime("%m")), int(strftime("%Y")), int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]
                tijd_int_gmt = [int(_time.strftime("%d", _time.gmtime())), int(_time.strftime("%m", _time.gmtime())), int(_time.strftime("%Y", _time.gmtime())), int(_time.strftime("%H", _time.gmtime())), int(_time.strftime("%M", _time.gmtime())), int(_time.strftime("%S", _time.gmtime()))]

                return [tijd_gmt, tijd_int_gmt, tijd_local, tijd_int_local]
            def times_pam():
                from time import gmtime, strftime
                import time as _time
                tijd_gmt = _time.strftime("%I:%M:%S %p %Z", _time.gmtime())
                tijd_local = strftime("%I:%M:%S %p %Z")
                tijd_int_local = [int(strftime("%d")), int(strftime("%m")), int(strftime("%Y")), int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]
                tijd_int_gmt = [int(_time.strftime("%d", _time.gmtime())), int(_time.strftime("%m", _time.gmtime())), int(_time.strftime("%Y", _time.gmtime())), int(_time.strftime("%H", _time.gmtime())), int(_time.strftime("%M", _time.gmtime())), int(_time.strftime("%S", _time.gmtime()))]

                return [tijd_gmt, tijd_int_gmt, tijd_local, tijd_int_local]
            def times():
                from time import gmtime, strftime
                import time as _time
                tijd_gmt = _time.strftime("%H:%M:%S %Z(gmt)", _time.gmtime())
                tijd_local = strftime("%H:%M:%S %Z")
                tijd_int_local = [int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]
                tijd_int_gmt = [int(_time.strftime("%H", _time.gmtime())), int(_time.strftime("%M", _time.gmtime())), int(_time.strftime("%S", _time.gmtime()))]
                return [tijd_gmt, tijd_int_gmt, tijd_local, tijd_int_local]
            def times_and_days():
                from time import gmtime, strftime
                import time as _time
                tijd_gmt = _time.strftime("%d/%m/%Y  %H:%M:%S %Z(gmt)", _time.gmtime())
                tijd_local = strftime("%d/%m/%Y  %H:%M:%S %Z")
                tijd_int_local = [int(strftime("%d")), int(strftime("%m")), int(strftime("%Y")), int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]
                tijd_int_gmt = [int(_time.strftime("%d", _time.gmtime())), int(_time.strftime("%m", _time.gmtime())), int(_time.strftime("%Y", _time.gmtime())), int(_time.strftime("%H", _time.gmtime())), int(_time.strftime("%M", _time.gmtime())), int(_time.strftime("%S", _time.gmtime()))]
                return [tijd_gmt, tijd_int_gmt, tijd_local, tijd_int_local]
            def days():
                from time import gmtime, strftime
                import time as _time
                tijd_gmt = _time.strftime("%d/%m/%Y")
                tijd_local = strftime("%d/%m/%Y")
                tijd_int_local = [int(strftime("%d")), int(strftime("%m")), int(strftime("%Y"))]
                tijd_int_gmt = [int(_time.strftime("%d", _time.gmtime())), int(_time.strftime("%m", _time.gmtime())), int(_time.strftime("%Y", _time.gmtime()))]
                return [tijd_gmt, tijd_int_gmt, tijd_local, tijd_int_local]
            def info():
                    '''chek(a) = chek the difference between the time at a and now for while loops that need to go for a time
            dagen_voorbij_in_dit_jaar(return) = returns the days that are pass in this year if task not is return he prints it
            tijd_nu(hour, min, sec) = returns the time now you say what you want
            dagen_tot(dag) = looks how many days to one day in this or next year
            nu(value) = prints and returns if value is print or tonen else he only returns
            tijd_zone() = returns your time zone
            times_and_days_pam(): returns the date and time of gmt and local
            times_and_days() = returns date and time  of gmt and local in 0 to 24 not in pm or am
            times_pam() = returns the time gmt and local in pm or am
            times() = returns the time gmt and local not in pm or am
            days() = returns the day in gmt and in local
            '''
class errors:
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
            






    










            
            


