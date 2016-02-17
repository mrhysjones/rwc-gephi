# Network analysis of the Rugby World Cup

Repository containing scripts, datasets, and some outputs from network analysis of Rugby World Cup data available from [Pick and Go! Test Match Results Database](http://www.lassen.co.nz/pickandgo.php)

### Python Scripts
To obtain the necessary data, two scripts have been implemented: 
- [get_rugby_data.py](python/get_rugby_data.py) - Parses the HTML from a given results page using the BeautifulSoup package. Outputs a csv file in the form *TeamA,TeamB,ScoreA,ScoreB,TriesA,TriesB* 

- [convert_csv_gdf.py](python/convert_csv_gdf.py) - Processes the generated csv file and creates a GDF representation. Finds unique teams/fixtures in the data and calculates attributes such as total scores, total tries, and weights (number of fixtures betweens two teams)

Example usage can be found at the bottom of the files

### Datasets
The following GDF files can be loaded directly into a [Gephi](https://gephi.org/) workspace 
#### [Rugby World Cup 1987](datasets/rwc_1987.gdf)
Obtained from [http://www.lassen.co.nz/pickandgo.php?fyear=1987&tyear=1987&teama=ALL&tourn=WC#hrh](http://www.lassen.co.nz/pickandgo.php?fyear=1987&tyear=1987&teama=ALL&tourn=WC#hrh). 

Involves 16 teams (nodes) and 32 unique fixtures between them (edges)

#### [Rugby World Cup 2015](datasets/rwc_2015.gdf)
Obtained from [http://www.lassen.co.nz/pickandgo.php?fyear=2015&tyear=2015&teama=ALL&tourn=WC#hrh](http://www.lassen.co.nz/pickandgo.php?fyear=2015&tyear=2015&teama=ALL&tourn=WC#hrh).

Involves 20 teams (nodes) and 48 unique fixtures between them (edges)
#### [All Rugby World Cup data](datasets/rwc_all.gdf)
Obtained from [http://www.lassen.co.nz/pickandgo.php?fyear=1987&tyear=1987&teama=ALL&tourn=WC#hrh](http://www.lassen.co.nz/pickandgo.php?fyear=1987&tyear=2015&teama=ALL&tourn=WC#hrh). 

Involves 25 teams (nodes) and 164 unique fixtures between them (edges)

### Gephi visualisations 
Rugby World Cup 1987 - ForceAtlas 2 layout, with node colour being ranked by total score </br>
<img src="gephi/rwc_1987-forceatlas2.png" alt="Rugby World Cup 1987 Visualisation" width=500 height=500></br>

Rugby World Cup 2015 - Fruchterman Reingold layout with node colour being ranked by total tries and node size being scaled to total score</br>
<img src="gephi/rwc_2015-reingold.png" alt="Rugby World Cup 2015 Visualisation" width=500 height=500></br>

All Rugby World Cups - ForceAtlas 2 layout, with node colour being ranked by total score </br>
<img src="gephi/rwc_all-forceatlas2.png" alt="Rugby World Cup 2015 Visualisation" width=500 height=500>

