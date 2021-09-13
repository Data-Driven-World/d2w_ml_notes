import os
import pdfkit
options = {
  "enable-local-file-access": None
}
if __name__ == '__main__':
    files = [i for i in os.listdir("./output") if i.endswith('.html')]
    if not files:
      print("Ensure you have run your html conversion script first.")
    else:
      for fn in files:
          fn = f"./output/{fn}"
          pdfkit.from_file(fn, fn.replace(".html", ".pdf"), options=options)