import gi
import subprocess
import os
from pathlib import Path

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

# Caminho para o script de confirmação
POWER_OPTIONS = os.path.expanduser('~/.config/sway/scripts/power-menu.py')

class PowerMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title="Opções de Energia")
        self.set_default_size(220, 280)
        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(20)

        # Captura a tecla ESC para fechar a janela
        self.connect("key-press-event", self.on_key_press)

        # Layout vertical principal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.add(vbox)

        # Título
        label = Gtk.Label(label="Opções de Energia")
        label.set_justify(Gtk.Justification.CENTER)
        label.set_name("titulo")
        vbox.pack_start(label, False, False, 10)

        # Botões de ação
        botoes = [
            ("Suspender", self.call_suspend),
            ("Encerrar Sessão", self.call_logout),
            ("Reiniciar", self.call_reboot),
            ("Desligar", self.call_poweroff),
        ]

        for texto, funcao in botoes:
            btn = Gtk.Button(label=texto)
            btn.set_size_request(160, 35)
            btn.connect("clicked", funcao)
            vbox.pack_start(btn, False, False, 0)

    # Ações dos botões
    def call_suspend(self, widget):
        subprocess.Popen(["systemctl", "suspend"])

    def call_logout(self, widget):
        subprocess.Popen(["python3", POWER_OPTIONS, "logout"])
        Gtk.main_quit()

    def call_reboot(self, widget):
        subprocess.Popen(["python3", POWER_OPTIONS, "reboot"])
        Gtk.main_quit()

    def call_poweroff(self, widget):
        subprocess.Popen(["python3", POWER_OPTIONS, "poweroff"])
        Gtk.main_quit()

    # Fecha a janela com ESC
    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()

# Execução do app
if __name__ == "__main__":
    app = PowerMenu()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
