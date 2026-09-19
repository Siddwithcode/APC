class Printer:
    def print_doc(self): print("Printing document...")
class Scanner:
    def scan_doc(self): print("Scanning document...")
class MultifunctionDevice(Printer, Scanner): pass
mfd = MultifunctionDevice()
mfd.print_doc()
mfd.scan_doc()
