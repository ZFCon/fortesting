from django.shortcuts import render

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def pdf_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    
    p.drawText('hi, how are you ?')
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(-1, -1, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

#Import the easy_pdf rendering
from easy_pdf.rendering import render_to_pdf_response

#Here's the detail view function
def detail_to_pdf(request):
    template = 'index.html'
    context = {}
    return render_to_pdf_response(request,template,context)