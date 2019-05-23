import pandas as pd
class Visualize:
    def __init__(self,filename):
        self.filename = filename


    def is_valid_filetype(self):
        if self.filename[-3:] == 'csv' or self.filename[-3:] == 'xls' or self.filename[-4:] == 'xlsx':
            return True
        return False


    def get_file_type(self):
        if self.filename[-3:] == 'csv':
            return "csv"
        elif self.filename[-3:] == 'xls':
            return "xls"
        elif self.filename[-4:] == 'xlsx':
            return "xlsx"
        else:
            return "invalid"


    def get_data_file(self):
        df = pd.DataFrame()
        ext = self.get_file_type()
        if ext == "xls" or ext == "xlsx":
            temp =  pd.ExcelFile(self.filename)
            df = pd.read_excel(temp,1)
            return df
        else:
            df = pd.read_csv(self.filename)
            return df
        return df