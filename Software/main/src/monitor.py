import tkinter as tk
from tkinter import scrolledtext
import threading

class AppBrazo:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Brazo Robótico - Monitor Serial")

        # --- INTERFAZ ---
        # Frame para el Monitor Serial
        self.frame_monitor = tk.LabelFrame(self.root, text="Monitor Serial (Status)")
        self.frame_monitor.pack(padx=10, pady=10, fill="both", expand=True)

        # Widget de texto con scroll para los mensajes
        self.monitor = scrolledtext.ScrolledText(self.frame_monitor, width=40, height=10, state='disabled')
        self.monitor.pack(padx=5, pady=5, fill="both", expand=True)

        # Iniciar el bucle de lectura
        self.actualizar_monitor()

    def enviar_comando(self):
        if self.ser and self.ser.is_open:
            self.ser.write(b's')
            self.insertar_texto(">> Enviado: s\n")

    def insertar_texto(self, texto):
        """Inserta texto de forma segura en el monitor"""
        self.monitor.config(state='normal') # Habilitar edición
        self.monitor.insert(tk.END, texto)
        self.monitor.see(tk.END)           # Auto-scroll al final
        self.monitor.config(state='disabled') # Bloquear edición de nuevo

    def actualizar_monitor(self):
        """Revisa el puerto serial sin congelar la GUI"""
        if self.ser and self.ser.is_open:
            if self.ser.in_waiting > 0:
                linea = self.ser.readline().decode('utf-8', errors='replace')
                self.insertar_texto(linea)
        
        # Volver a llamar a esta función en 100ms
        self.root.after(100, self.actualizar_monitor)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppBrazo(root)
    root.mainloop()
