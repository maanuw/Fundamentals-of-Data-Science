## Project Description:
### Grain:
## Conceptual model:
![updated-model](../img/model.png)

## Dimensions and diemensional attributes:
### Publisher Dimension:
Publishers database is a list of all the video game publishers on Steam.
| Name                 | Type     | Description                                        |
|----------------------|----------|----------------------------------------------------|
| Name(PK)             | str      | Publisher Name                                     |
| Classification       | Category | Game Classification (e.g. AAA, Indie ...)          |
| Released_games       | int      | Number of Released Games                           |
| Unreleased_Games     | int      | Number of unreleased Games                         |
| Total_revenue        | float    | Total Revenue                                      |
| Avg_revenue_per_game | float    | The average game revenue                           |
| Med_revenue_per_game | float    | The Median of Game Revenue Distribution            |
| %_developed_in_house | float    | Percentage of games developed in house             |
| %_indie_releases     | float    | Percentage of releases form third-party Developers |
| Action               | float    | Percentage of releases of the Action genre         |
| Casual               | float    | Percentage of releases of the Casual genre         |
| Adventure            | float    | Percentage of releases of the Adventure genre      |
| Simulation          | float    | Percentage of releases of the Simulation genre     |
| Strategy             | float    | Percentage of releases of the Strategy genre       |
| RPG                  | float    | Percentage of releases of the RPG genre            |
| MMO                  | float    | Percentage of releases of the MMO genre            |
| Racing               | float    | Percentage of releases of the Racing genre         |
| Sports               | float    | Percentage of releases of the Sports genre         |
### Game Dimension:
### Console dimension
### Fact table:

## Assumptions:

## Issues and Challenges:
Publisher database contains only video games publisher from steam only.
