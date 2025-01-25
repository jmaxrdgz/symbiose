import threading
import numpy as np

from communication import (
    SerialCommunication,
    BluetoothCommunication,
    WiFiCommunication
)


class Reader(threading.Thread):
    """
    Reader class to read frames from a communication interface.

    Args:
        name (str): Name of the reader.
        dtype (type): Data type of the frame.
        fdim (tuple): Frame dimensions.
        com_type (str): Communication type.
        **kwargs: Additional arguments for the communication interface.
    """
    def __init__(self, name:str, dtype:type, fdim:tuple, com_type:str, **kwargs):
        super().__init__()
        self.name = name
        self.dtype = dtype
        self.fdim = fdim
        self.com = self._create_com(com_type, **kwargs)

    def _create_com(self, com_type, **kwargs):
        if com_type == 'serial':
            return SerialCommunication(kwargs['port'], kwargs['baudrate'])
        if com_type == 'bluetooth':
            return BluetoothCommunication() # TODO: Comming soon
        if com_type == 'wifi':
            return WiFiCommunication() # TODO: Comming soon

        raise ValueError(f"Unknown communication type: {com_type}")

    def __repr__(self):
        return f"Reader({self.name})"

    def __str__(self):
        info_str = (
            f"Reader(name={self.name}, "
            f"dtype={self.dtype}, "
            f"fdim={self.fdim}, "
            f"com_type={type(self.com).__name__})"
        )
        return info_str

    def next(self):
        """
        Read the next frame from the communication interface.
        Frame is shaped according to the fdim attribute and dtype.

        Returns:
            np.ndarray: The next frame.
        """
        n_bytes = np.prod(self.fdim) * self.dtype().itemsize
        frame_data = self.com.read(n_bytes)
        frame = np.array(frame_data, dtype=self.dtype).reshape(self.fdim)
        return frame
