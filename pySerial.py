# import serial
# import threading
# import tkinter as tk


# class SerialMonitorGUI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.text = tk.Text(self.root)
#         self.text.pack()

#         self.serial_port = serial.Serial(port='COM42', baudrate=115200)

#         self.thread = threading.Thread(target=self.read_serial_data)
#         self.thread.start()

#         self.root.mainloop()

#     def read_serial_data(self):
#         while True:
#             data = self.serial_port.readline()
#             data_string = str(data, 'UTF-8')

#             self.text.insert('end', data_string)
#             self.text.update()

# if __name__ == '__main__':
#     serial_monitor_gui = SerialMonitorGUI()
import serial
# import serial.tools.list_ports

# com_ports = list(serial.tools.list_ports.comports())

# for port in com_ports:
#     print(f"Port: {port.device}, Description: {port.description}")


serial_port = serial.Serial(port='COM3', baudrate=115200)

while True:
    data = serial_port.readline()
    data_string = str(data, 'UTF-8')

    print(data_string)

    # Add a delay between sending each byte
    import time
    time.sleep(0.01)
