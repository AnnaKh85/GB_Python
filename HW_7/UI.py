from this import d
import data
import logger as log

def data_view():
    d0,d1,d2,d3,d4,d5  = data.get_data(),data.get_data(),data.get_data()\
        ,data.get_data(),data.get_data(),data.get_data()
    d = d0,d1,d2,d3,d4,d5
    log.add_data(d)
    return d
