import sys
import subprocess
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Verificação de argumento
if len(sys.argv) < 2:
    subprocess.Popen(['notify-send', 'Sistema', 'O Script precisa de argumentos'])
    sys.exit(1)

# Argumento recebido
action = sys.argv[1]

# Define mensagem e comando
if action == 'logout':
    question = 'Encerrar a sessão?'
    run = ['swaymsg', 'exit']
elif action == 'reboot':
    question = 'Reiniciar o sistema?'
    run = ['systemctl', 'reboot']
elif action == 'poweroff':
    question = 'Desligar o sistema?'
    run = ['systemctl', 'poweroff']
else:
    subprocess.Popen(['notify-send', 'Sistema', f'Ação inválida: {action}'])
    sys.exit(1)

# Janela de confirmação
class Confirmacao(Gtk.Window):
    def __init__(self):
        super().__init__(title="Confirmação")
        self.set_default_size(300, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)
        self.set_border_width(20)

        # Caixa vertical principal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.add(vbox)

        # Label da pergunta
        label = Gtk.Label(label=question)
        label.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label, True, True, 0)

        # Caixa horizontal para os botões
        hbox = Gtk.Box(spacing=10)
        vbox.pack_end(hbox, False, False, 0)

        # Botão "Sim"
        btn_yes = Gtk.Button(label="Sim")
        btn_yes.set_size_request(90, 35)
        btn_yes.connect("clicked", self.on_yes_clicked)
        hbox.pack_start(btn_yes, True, True, 0)

        # Botão "Não"
        btn_no = Gtk.Button(label="Não")
        btn_no.set_size_request(90, 35)
        btn_no.connect("clicked", self.on_no_clicked)
        hbox.pack_start(btn_no, True, True, 0)

    def on_yes_clicked(self, button):
        subprocess.Popen(run)
        Gtk.main_quit()

    def on_no_clicked(self, button):
        print("Cancelado pelo usuário")
        Gtk.main_quit()

# Executa o app
if __name__ == "__main__":
    app = Confirmacao()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
