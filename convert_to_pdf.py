import os
import pdfkit
import sys
options = {
  "enable-local-file-access": None
}
if __name__ == '__main__':
    if len(sys.argv) == 2:
        html_filename = os.path.splitext(sys.argv[1])[0] + '.html'
        if not html_filename in os.listdir("./output"):
          print(f"Unable to find {html_filename}!")
        else:
          fn = f"./output/{html_filename}"
          pdfkit.from_file(fn, fn.replace(".html", ".pdf"), options=options)
    else:
        files = [i for i in os.listdir("./output") if i.endswith('.html')]
        if not files:
          print("Ensure you have run your html conversion script first.")
        else:
          for fn in files:
              fn = f"./output/{fn}"
              pdfkit.from_file(fn, fn.replace(".html", ".pdf"), options=options)