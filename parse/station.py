from lib import pathhelper

class ObservationStation(object):
    attr_slots = ('name', 'longitude', 'latitude')
    def __init__(self, arg_list):
        name, longitude, latitude = arg_list
        self.name = str(name)
        self.longitude, self.latitude = float(longitude), float(latitude)

class LocationDB(object):
    def __init__(self):
        self.db = {}
        with open(pathhelper.station_path, 'r') as station:
            for line in station.readlines()[1:]:
                current_date = line.split()
                self.db[current_date[0]] = ObservationStation(current_date)
        
    def get(self, station_name):
        return self.db.get(station_name, None)
    
try:
    Location_db
except NameError:
    Location_db = LocationDB()
    
if __name__ == '__main__':
    print(Location_db.db)
