import subprocess
from modules import cbpi
from modules.core.hardware import ActorBase
from modules.core.props import Property


@cbpi.actor
class GembirdUSB(ActorBase):

    socket_no = Property.Select(label="Socket No", options=[1,2,3,4,5])

    def on(self, power=100):
        try:
            print self.socket_no
            command = "sudo sispmctl -o " + str(self.socket_no)
            subprocess.call(command, shell=True)
        except Exception as e:
            self.api.notify("Gembird Actor Error", "Faied to switch socket. Please check configuration", type="danger", timeout=None)
            self.api.app.logger.error("Failed to switch Socket")

    def off(self):
        try:
            command = "sudo sispmctl -f " + str(self.socket_no)
            subprocess.call(command, shell=True)
        except Exception as e:
            self.api.notify("Gembird Actor Error", "Faied to switch socket. Please check configuration", type="danger", timeout=None)
            self.api.app.logger.error("Failed to switch Socket")




