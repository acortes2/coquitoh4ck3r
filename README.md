Red Team Payload Installer Script

Este repositorio contiene un script de PowerShell que automatiza la instalación de un payload de Red Team. El script realiza las siguientes acciones:

    Verifica si Python está instalado: Si no está instalado, descarga e instala automáticamente Python 3.10.

    Instala las librerías de Python necesarias: Asegura que las librerías requeridas (como pynput, psutil, pyttsx3, entre otras) estén instaladas en el sistema.

    Elimina eventos de seguridad del visor de eventos: Intenta limpiar los eventos de seguridad en el sistema utilizando wevtutil (requiere permisos elevados).

    Genera un registro de todas las acciones: El script genera un archivo de registro en el escritorio del usuario con el nombre redteam_log.txt que detalla todas las acciones realizadas y cualquier error encontrado.

Este script está diseñado para ser utilizado en un entorno de pruebas de seguridad, en el contexto de una práctica de Red Team y Blue Team, con fines educativos.

¡Advertencia!: Este script debe usarse únicamente con el consentimiento adecuado y en entornos controlados y legales. No se debe ejecutar en sistemas sin la debida autorización, ya que podría ser considerado un ataque malicioso.
Requisitos

    PowerShell (v5.0 o superior).

    Permisos de administrador para ejecutar algunas acciones del script.

Instalación

    Descarga o clona este repositorio.

    Ejecuta el script install_payload.ps1 en un entorno de PowerShell con privilegios de administrador.
