

class Analysis:
    """Returns the geographic and weekly capacity information of that location code"""
    def __init__(self, data):
        self.loc = data.get_loc_data()
        self.trips = data.get_trips_data()

    def find_loc_detail(self, user_input: str):
        """Find the location information including longitude, latitude and ownership"""
        loc = self.loc
        loc = loc.set_index("LocationCode")
        if user_input not in loc.index:
            return -1
        else:
            data = loc.loc[user_input]
            if data["FacilityOwnedByCarvana"] == 1:
                ownership = "Owned by Carvana"
            else:
                ownership = "Not Owned by Carvana"
            res = ["Lat: " + str(data["Latitude"]), "Long: " + str(data["Longitude"]), ownership]
        return res

    def find_trips_detail(self, user_input: str):
        """Find the weekly capacity information of that location"""
        trips = self.trips
        location_code = set(trips["Origin"].to_list() + trips["Destination"].to_list())
        if user_input not in location_code:
            return -1
        else:
            org = trips[trips["Origin"] == user_input].drop_duplicates().reset_index()
            des = trips[trips["Destination"] == user_input].drop_duplicates().reset_index()
            res_org = []
            res_des = []
            for i in range(org.shape[0]):
                temp_data = org.iloc[i]
                temp = temp_data["Origin"] + " to " + temp_data["Destination"] + " (" \
                       + str(temp_data["WeeklyCapacity"]) + " weekly capacity)"
                res_org.append(temp)
            for i in range(des.shape[0]):
                temp_data = des.iloc[i]
                temp = temp_data["Origin"] + " to " + temp_data["Destination"] + " (" \
                       + str(temp_data["WeeklyCapacity"]) + " weekly capacity)"
                res_des.append(temp)
            result = {"Origin Trips": res_org, "Destination Trips": res_des}
        return result
