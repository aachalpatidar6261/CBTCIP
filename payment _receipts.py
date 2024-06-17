from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_receipt(receipt_data, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2.0, height - 40, "Transaction Receipt")
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2.0, height - 70, "Thank you for your purchase!")
    c.line(30, height - 80, width - 30, height - 80)
    text = c.beginText(40, height - 100)
    text.setFont("Helvetica", 12)

    for key, value in receipt_data.items():
        text.textLine(f"{key}: {value}")

    c.drawText(text)
    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(width / 2.0, 30, "Thank you for shopping with us!")
    c.save()

receipt_data = {
    "Receipt Number": "12345",
    "Date": "2024-06-17",
    "Customer Name": "John Doe",
    "Items Purchased": "Item A, Item B, Item C",
    "Total Amount": "$123.45",
    "Payment Method": "Credit Card"
}

create_receipt(receipt_data, "transaction_receipt.pdf")
