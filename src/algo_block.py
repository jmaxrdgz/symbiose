import threading
import queue

class AlgoBlock(threading.Thread):
    """
    Custom algorithm block to process data from readers.
    """
    def __init__(self):
        super().__init__()
        self.readers = {}
        self.data_queue = queue.Queue()
        self.running = False
        self.readers_data = {}

    def add_reader(self, reader):
        """
        Add a unique reader.
        """
        if reader not in self.readers:
            self.readers[reader] = {}
            reader.set_data_queue(self.data_queue)
            reader.start()
            print(f"Reader {reader} added.")
        else:
            print(f"Reader {reader} already exists.")

    def remove_reader(self, reader):
        """
        Remove a reader.
        """
        if reader in self.readers:
            reader.stop()
            del self.readers[reader]
            print(f"Reader {reader} removed.")
        else:
            print(f"Reader {reader} not found.")

    def get_reader(self, reader):
        """
        Access data from a specific reader.
        """
        return self.readers.get(reader, None)

    def run(self):
        """
        Run the algorithm block.
        """
        self.running = True
        while self.running:
            try:
                data_packet = self.data_queue.get(timeout=1)
                reader_name = data_packet.reader_name
                self.readers_data[reader_name] = data_packet.data
                self.process_data(**self.readers_data)
            except queue.Empty:
                continue

    def stop(self):
        """
        Stop the algorithm block.
        """
        self.running = False

    def process_data(self, **kwargs):
        """
        Custom algorithm to process data from readers.
        """
        raise NotImplementedError("Subclasses should implement this method with a custom algorithm.")

    def forward(self):
        """Forward data from readers to watchers."""
        for key, reader in self.readers.items():
            print(f"{key} : {reader.next()}")
