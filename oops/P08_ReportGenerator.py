class Report:
    def generate(self): pass
class PDFReport(Report):
    def generate(self): print("Generating PDF")
class ExcelReport(Report):
    def generate(self): print("Generating Excel")
class HTMLReport(Report):
    def generate(self): print("Generating HTML")
def generate_report(report_obj): report_obj.generate()
generate_report(PDFReport())
