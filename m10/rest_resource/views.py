# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from models import E0, SP1, D1, I1
from django.conf import settings
import time, datetime
from glob import glob
from os.path import join
import csv

MODELS = dict(
    SP1 = SP1,
    E0 = E0,
    D1 = D1,
    I1 = I1,
    )

def main(request):
    csv_pattern = join(settings.CSV_DIR,'*/*.csv')
    csv_files = glob(csv_pattern)
    for f in csv_files:
        MODEL = f.split('/')[-2]
        if MODELS.has_key(MODEL):
            import_csv(f,MODELS[MODEL])
    return render(request,'main.html')

def import_csv(CSVFILE, MODEL):
    rownum = 0
    rows = []
    with open(CSVFILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            unicode_row = [x.decode('ISO-8859-1') for x in row]
            if rownum == 0:
                header = unicode_row
            else:
                rows.append(unicode_row)
            rownum += 1
    for r in rows:
        bulk = dict(zip(header,r))
        date_str = bulk['Date']
        if not date_str:
            continue
        if len(date_str.split('/')[-1]) == 2:
            tm_date = time.strptime(date_str, '%d/%m/%y')
        elif len(date_str.split('/')[-1]) == 4:
            tm_date = time.strptime(date_str, '%d/%m/%Y')
        fields = {}
        fields['Div'] = bulk['Div']
        fields['HomeTeam'] = bulk['HomeTeam']
        fields['AwayTeam'] = bulk['AwayTeam']
        fields['Date'] = datetime.date(tm_date.tm_year, tm_date.tm_mon, tm_date.tm_mday)
        if bulk.get('FTHG',None):
            fields['FTHG'] = int(bulk.get('FTHG',None))
        if bulk.get('FTAG',None):
            fields['FTAG'] = int(bulk.get('FTAG',None))
        if bulk.get('FTR',None):
            fields['FTR'] = bulk.get('FTR',None)
        if bulk.get('HTHG',None):
            fields['HTHG'] = int(bulk.get('HTHG',None))
        if bulk.get('HTAG',None):    
            fields['HTAG'] = int(bulk.get('HTAG',None))
        if bulk.get('HTR',None):    
            fields['HTR'] = bulk.get('HTR',None)
        if bulk.get('Referee',None):    
            fields['Referee'] = bulk.get('Referee',None)
        if bulk.get('HS',None):
            fields['HS'] = int(bulk.get('HS',None))
        if bulk.get('AS',None):
            fields['AS'] = int(bulk.get('AS',None))
        if bulk.get('HST',None):
            fields['HST'] = int(bulk.get('HST',None))
        if bulk.get('AST',None):
            fields['AST'] = int(bulk.get('AST',None))
        if bulk.get('HF',None):
            fields['HF'] = int(bulk.get('HF',None))
        if bulk.get('AF',None):
            fields['AF'] = int(bulk.get('AF',None))
        if bulk.get('HC',None):
            fields['HC'] = int(bulk.get('HC',None))
        if bulk.get('AC',None):
            fields['AC'] = int(bulk.get('AC',None))
        if bulk.get('HY',None):
            fields['HY'] = int(bulk.get('HY',None))
        if bulk.get('AY',None):
            fields['AY'] = int(bulk.get('AY',None))
        if bulk.get('HR',None):
            fields['HR'] = int(bulk.get('HR',None))
        if bulk.get('AR',None):
            fields['AR'] = int(bulk.get('AR',None))
        if bulk.get('B365H',None):
            fields['B365H'] = float(bulk.get('B365H',None))
        if bulk.get('B365D',None):
            fields['B365D'] = float(bulk.get('B365D',None))
        if bulk.get('B365A',None):
            fields['B365A'] = float(bulk.get('B365A',None))
        '''a = dict(
            Div = bulk['Div'],
            #Date = strptime(bulk['Date'], '%d/%m/%y'),
            Date = datetime.date(y,m,d),
            HomeTeam = bulk['HomeTeam'],
            AwayTeam = bulk['AwayTeam'],
            FTHG = int(bulk.get('FTHG',None)),
            FTAG = int(bulk.get('FTAG',None)),
            FTR = bulk.get('FTR',None),
            HTHG = int(bulk.get('HTHG',None)),
            HTAG = int(bulk.get('HTAG',None)),
            HTR = bulk.get('HTR',None),
            HS = int(bulk.get('HS',None)),
            AS = int(bulk.get('AS',None)),
            HST = int(bulk.get('HST',None)),
            AST = int(bulk.get('AST',None)),
            HF = int(bulk.get('HF',None)),
            AF = int(bulk.get('AF',None)),
            HC = int(bulk.get('HC',None)),
            AC = int(bulk.get('AC',None)),
            HY = int(bulk.get('HY',None)),
            AY = int(bulk.get('AY',None)),
            HR = int(bulk.get('HR',None)),
            AR = int(bulk.get('AR',None)),
            B365H = float(bulk.get('B365H',None)),
            B365D = float(bulk.get('B365D',None)),
            B365A = float(bulk.get('B365A',None)),
            )'''
        #print fields
        new_row = MODEL(**fields)
        new_row.save()