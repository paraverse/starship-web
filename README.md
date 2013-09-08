# Starship: Enterprise Data Analytics

## API Endpoints

### Github Globe (/github-globe/)

Provides data about the locations of Github users around the world.

Each data point contains a location in the form of geographic coordinates
and a magnitude which represents the population at the location relative to other locations.

Currently, only the 1000 most populous locations are listed, however this is subject to change.

Example format:

```json
[
  {
    "magnitude" : 1.0,
    "coordinates" : {
      "latitude" : "45.00",
      "longitude" : "90.00"
  }
]
```

### Server Usage Data (/server-farm/)

Provides fake usage data about a server cluster over time.

All numbers are floats in the interval (0, 1) and represent the percent of the resource used.

```json
[
  [
    {
      "cpu" : 1.0,
      "ram" : 1.0,
      "network" : 1.0,
      "disk" : 1.0
    }
  ]
]
```


