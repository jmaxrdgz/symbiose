class DataPacket:
    def __init__(self, reader_name, data):
        self.reader_name = reader_name
        self.data = data

    def __repr__(self):
        return f"DataPacket(reader_name={self.reader_name}, data={self.data})"
