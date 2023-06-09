# Fundamentals-of-Data-Science
Design and implementation of a data mart, as well as the exploration of this data mart using online analytic processing (OLAP), information visualization and data mining.

Contributors
- Manav Patel
- Moumin Farah
- Othmane Ayoub


## [Deliverable 1 - Conceptual Design](https://github.com/maanuw/Fundamentals-of-Data-Science/tree/main/Conceptual-Design-Deliverable-1)
Implement a dimensional model detailing initial design of the project Data Mart
- Declaration of grain for the Data Mart.
- Detailed conceptualization of the dimensions and dimensional attributes.
- Detailed conceptualization of the measures and facts attributes.
- Detailed explaination of assumptions carried on.

## [Deliverable 2 - Physical Design](https://github.com/maanuw/Fundamentals-of-Data-Science/tree/main/Physical-Design-Deliverable-2)
Converting the conceptual design from the first deliverable into a physical design by following the ETL(Extraction, Transform and Load) data staging steps.
Populated the Data Mart as follows:
- Extracting data from various sources. (Check out the reference section of this document)
- Transformation: Data cleaning (handling missing values, typos, and outliers, removing duplicates, converting data types etc.) 
transforming the data into a format that can be used for analysis (i.e., normalizing or scaling the data), data integration, data discretization (i.e., converting continuous data into discrete data by grouping it into bins or categories), Feature engineering (i.e., creating new features from existing data that may be more relevant or useful for analysis). This step may also involve aggregating or summarizing data.
- Loading: Loading the final integrated dataset.
Finally creating the the data mart using a Database Management system. (Postgres).

## [Deliverable 3 - OLAP Vizualisation](https://github.com/maanuw/Fundamentals-of-Data-Science/tree/main/OLAP-Vizualisation-Data-Mining-Deliverable-3)

- Part A.1. Standard OLAP operations – 8 queries in total
- Part A.2. Explorative operation
- Part B. BI dashboard and Information Visualization

## [Deliverable 4 - Data Mining](https://github.com/maanuw/Fundamentals-of-Data-Science/tree/main/Data-Mining-Deliverable-4)
- [Part a + c: Data exploration and outliers detection](https://github.com/maanuw/Fundamentals-of-Data-Science/blob/main/Data-Mining-Delivrable-4/Phase4-a%2Bc.ipynb)

- [Part-B Classification (Supervised Learning)](https://github.com/maanuw/Fundamentals-of-Data-Science/blob/main/Data-Mining-Deliverable-4/Part-B-classification-supervised-learning.ipynb) 

## References
List of data sources used for each dimension of our conceptual design.
- Game Dimension
    - `Physical-Design-Deliverable-2/assets/games/vgsales.csv` : [Data Source](https://www.kaggle.com/datasets/gregorut/videogamesales)
    - `Physical-Design-Deliverable-2/assets/games/imdb-videogames.csv` : [Data Source](https://www.kaggle.com/datasets/muhammadadiltalay/imdb-video-games?select=imdb-videogames.csv)
    - `Physical-Design-Deliverable-2/assets/games/hltb.jsonlines` : [Data Source](https://www.kaggle.com/datasets/baraazaid/how-long-to-beat-video-games)
- Publisher Dimension
    - `Physical-Design-Deliverable-2/assets/publisher/` : [Data Source](https://vginsights.com/publishers-database)
- Console Dimension 
    - `Physical-Design-Deliverable-2/assets/console/` : [Data Source](https://www.kaggle.com/datasets/jaimepazlopes/game-console-manufactor-and-sales)
