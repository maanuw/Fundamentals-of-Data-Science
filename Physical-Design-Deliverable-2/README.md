## Deliverable 2 - Physical Design
Converting the conceptual design from the first deliverable into a physical design by following the ETL(Extraction, Transform and Load) data staging steps.
Populated the Data Mart as follows:
- Extracting data from various sources. (Check out the reference section of this document)
- Transformation: Data cleaning (handling missing values, typos, and outliers, removing duplicates, converting data types etc.) 
transforming the data into a format that can be used for analysis (i.e., normalizing or scaling the data), data integration, data discretization (i.e., converting continuous data into discrete data by grouping it into bins or categories), Feature engineering (i.e., creating new features from existing data that may be more relevant or useful for analysis). This step may also involve aggregating or summarizing data.
- Loading: Loading the final integrated dataset.
Finally creating the the data mart using a Database Management system. (Postgres).

## Implementation
- We sourced our data as shown in the References section.
- As per our conceptual design we have three main dimensions that we performed ETL implementation for `Game`, `Console` and `Publisher`
- Our Working and explaination for the Extraction and transformation for the dimensions is available here:
- [Publisher Dimention](https://github.com/maanuw/Fundamentals-of-Data-Science/blob/main/Physical-Design-Deliverable-2/transformation/Publisher.ipynb)
- [Game Dimension](https://github.com/maanuw/Fundamentals-of-Data-Science/blob/main/Physical-Design-Deliverable-2/transformation/game.ipynb)

## Challenges
- The domain chosen by our team surprisingly has very scarcely available open source data.
- Our team had to source data from multiple sources in order for us to be able to converge these data points into our data mart.
- Our sourced data required alot of preprocessing.
- We had to find methods to deal with missing data as explained in the Game Dimension notebook.

## Dimensions and Fact table on DBMS
- DBMS used postgres and pgadmin

## Updated conceptual Design as per new physical design
![updated-model](/Users/mpatel4/Desktop/school/CSI_4142/project/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/Screen Shot 2023-03-25 at 12.40.36 AM.png)
## References
List of data sources used for each dimension of our conceptual design.
- Game Dimension
    - `Physical-Design-Deliverable-2/assets/games/vgsales.csv` : [Data Source](https://www.kaggle.com/datasets/gregorut/videogamesales)
    - `Physical-Design-Deliverable-2/assets/games/imdb-videogames.csv` : [Data Source](https://www.kaggle.com/datasets/muhammadadiltalay/imdb-video-games?select=imdb-videogames.csv)
    - `Physical-Design-Deliverable-2/assets/games/hltb.jsonlines` : [Data Source](https://www.kaggle.com/datasets/baraazaid/how-long-to-beat-video-games)
- Publisher Dimension
    - `Physical-Design-Deliverable-2/assets/publisher/` : [Data Source](https://www.kaggle.com/datasets/andreshg/videogamescompaniesregions?select=video-games-developers.csv)
- Console Dimension 
    - `Physical-Design-Deliverable-2/assets/console/` : [Data Source](https://www.kaggle.com/datasets/jaimepazlopes/game-console-manufactor-and-sales)
