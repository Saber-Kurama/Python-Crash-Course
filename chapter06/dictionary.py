aline_0 = { "color": "red", "points": 5 }

print(aline_0["color"])

aline_0['x_position'] = 0;
aline_0['y_position'] = 25;
print(aline_0)

aline_0 = {}
aline_0['color'] = "green";
print(aline_0)
aline_0 = { "color": "green", "points": 5 }

del aline_0['color']

print(aline_0)

alien_0 = { "color1": "green", "points": 5 }
print(alien_0.get("color", "No color found"))