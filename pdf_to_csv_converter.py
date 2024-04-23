import fitz
import csv


def pdf_to_csv_single_sheet_unique_headers(pdf_path, csv_path ):
  c=1
  headers_seen = set()
  with fitz.open(pdf_path) as doc, open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for page_number, page in enumerate(doc): 
      tables = page.find_tables()
      for tab in tables: 
        table_data = tab.extract()
        if c==1:
            writer.writerows(table_data)
            headers_seen.update(table_data[0])
            c=2
        else:
          writer.writerows(table_data[1:])
          headers_seen.update(table_data[0])

pdf_path = "pdf_redemption.pdf"  # When working in Visual code we can use direct file names if not use the path of the files
csv_path = "csv_redemption.csv"  

pdf_path1 = "pdf_purchase.pdf"
csv_path1 = "csv_purchase.csv"
  
pdf_to_csv_single_sheet_unique_headers(pdf_path, csv_path)
pdf_to_csv_single_sheet_unique_headers(pdf_path1, csv_path1)
