import pyproj

lat1, long1 = (37.8101274, -122.4104622)
lat2, long2 = (37.80237485, -122.405832766082)

geod = pyproj.Geod(ellps="WGS84")
angle1, angle2, distance = geod.inv(long1, lat1, long2, lat2)

print("Distance is {:0.2f} meters.".format(distance))
