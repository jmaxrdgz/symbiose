import serial
from serial.tools import list_ports

class CommunicationInterface:
    def connect(self):
        raise NotImplementedError

    def read(self, total_bytes):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class SerialCommunication(CommunicationInterface):
    def __init__(self, port:str=None, baudrate:int=115200):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

        self.connect()

    def connect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()

        if self.port is None:
            ports = list(list_ports.comports())
            if ports:
                self.port = ports[0].device
            else:
                print("Aucun port série disponible.")
                return

        try:
            self.ser = serial.Serial(self.port, self.baudrate)
            print(f"Connected to serial port: {self.port}")
        except serial.SerialException as e:
            print(f"Erreur de connexion au port série: {e}")

    def read(self, total_bytes):
        if self.ser.in_waiting >= total_bytes:
            return self.ser.read(total_bytes)
        else:
            return None

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()


class BluetoothCommunication(CommunicationInterface):
    def connect(self):
        # Implémenter la connexion Bluetooth
        pass

    def read(self, total_bytes):
        # Implémenter la lecture Bluetooth
        pass

    def close(self):
        # Implémenter la fermeture Bluetooth
        pass


class WiFiCommunication(CommunicationInterface):
    def connect(self):
        # Implémenter la connexion Wi-Fi
        pass

    def read(self, total_bytes):
        # Implémenter la lecture Wi-Fi
        pass

    def close(self):
        # Implémenter la fermeture Wi-Fi
        pass