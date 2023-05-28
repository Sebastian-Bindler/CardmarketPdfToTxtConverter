# Import the required Module
import tabula
import csv
import glob
import os

targetPattern = r"input/*.pdf"
daten = glob.glob(targetPattern)
datenIndex = len(daten)

for f in glob.glob("output/*.txt"):
    os.remove(f)

for i in range (0 , datenIndex):
    filename = daten[i]
    print(filename)
    df = tabula.read_pdf(filename, pages='all')[0]
    tabula.convert_into(filename, filename.replace("pdf", "csv"), output_format="csv", pages='all')
    
    CsvToTxtFileName = filename.replace("pdf", "csv")
    OutputFileNameTxt = CsvToTxtFileName.replace("Einkauf_#", "")
    OutputFileNameTxt = OutputFileNameTxt.replace("input", "output")
    OutputFileNameTxt = OutputFileNameTxt.replace("csv", "txt")
    Bestellnummer = OutputFileNameTxt.replace(".txt", "")
    Bestellnummer = Bestellnummer.replace("output\\", "")
    
    with open(CsvToTxtFileName) as f:
        lis = []
        for line in csv.DictReader(f, fieldnames=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')):
            #print(line)
            lis.append(line)
           
        for i in lis:
            l = []
            i.update({'a': Bestellnummer})
            l.append(i['a'])
            l.append(i['b'])
            l.append(i['c'])
            l.append(i['d'])
            l.append(i['e'])
            l.append(i['f'])
            l.append(i['g'])
            l.append(i['i'])
            
            x = l[2].find("DE")
            
            if x != -1:
                l[2] = l[2].replace(" DE", "")
                l[3] = "DE"
                
            x = l[2].find("EN")
            if x != -1:
                l[2] = l[2].replace(" EN", "")
                l[3] = "EN"
                
            x = l[2].find("JP")
            if x != -1:
                l[2] = l[2].replace(" JP", "")
                l[3] = "JP"
                
            
            string = "{}	{}	{}	{}	{}	{}	{}	{}\n".format(l[0], l[1], l[2], l[3], l[4], l[5], l[6], str(l[7]).replace("EUR", ""))
            with open(OutputFileNameTxt, 'a') as fd:
                fd.write(string)
            fd.close()
        
    
    
