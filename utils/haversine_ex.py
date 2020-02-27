# Use haversine (https://github.com/mapado/haversine) to check 2D distance
import haversine
p1 = (21.3109379275,-157.888570247)
p2 = (21.3100789254,-157.888191105)
print haversine.haversine(p1,p2,unit=haversine.Unit.METERS)
