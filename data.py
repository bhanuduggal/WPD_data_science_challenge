import pandas as pd

class ReadRawData(object):
    
    def __init__(self,data_path='Dataset/'):
        self.data_path = data_path
    
    def set_file_path(self,task):
        demand_train = self.data_path + task + '/' + 'demand_train'+ "_" + task + ".csv"
        pv_train = self.data_path + task +  '/' + 'pv_train'+ "_" + task + ".csv"
        weather_train = self.data_path + task + '/' + 'weather_train'+ "_" + task + ".csv"
        return [demand_train, pv_train, weather_train]
    
    
    def create_training_dataframes(self,path):
        df = pd.read_csv(path).set_index('datetime')
        return df