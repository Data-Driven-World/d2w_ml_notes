import os
import pdfkit
options = {
  "enable-local-file-access": None
}
if __name__ == '__main__':
    files = [i for i in os.listdir() if i.endswith('.html')]
    for fn in files:
        pdfkit.from_file(fn, fn.replace(".html", ".pdf"), options=options)