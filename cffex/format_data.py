import pandas as pd
import zipfile
import os

def unzip_files(filespath = 'cffex_data', targetpath = 'unzip_data'):
    filenames = [x for x in os.listdir(filespath) if x[-3:] == 'zip']
    if not os.path.isdir(targetpath):
        os.mkdir(targetpath)

    for filename in filenames:
        zip_file = zipfile.ZipFile('cffex_data/{}'.format(filename))
        zip_file.extractall('{}/{}'.format(targetpath, filename[:-4]))

def format_dataframe(filespath = 'unzip_data', targetpath = 'formatted_data'):
    output_dict = {}
    if not os.path.isdir(targetpath):
        os.mkdir(targetpath)
        
    for month in [x for x in os.listdir(filespath) if not x.startswith('.')]:
        csv_names = os.listdir('{}/{}'.format(filespath, month))
        for csv in csv_names:
            #2020 data has different formatting
            date = csv[:-6]
            df = pd.read_csv('{}/{}/{}'.format(filespath, month,csv),
                            encoding='gbk', error_bad_lines=False)
            df = df.loc[~df['合约代码'].str.contains('计')] #exclude summary line
            df.set_index('合约代码', inplace = True)
            
            for contrat_code in df.index:
                #memory inefficient, but the dataset is small, so whatever
                data = df.loc[contrat_code]
                data.name = date
                output_dict[contrat_code] = output_dict.get(contrat_code, pd.DataFrame()).append(data)
    

    for key, value in output_dict.items():
        value.sort_index().to_csv('{}/{}.csv'.format(targetpath, key))
    
if __name__ == '__main__':
    unzip_files()
    format_dataframe()
