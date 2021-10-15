@ECHO OFF
if not exist ".\output" mkdir output
for %%f in (*.ipynb) do (
    echo %%f
    python -m jupyter nbconvert %%f --to html --output-dir ./output
)
python convert_to_pdf.py

