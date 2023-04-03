# AI Project 1: Maze Search

## Overview

This project is an implementation of search algorithms for a maze game. The game is implemented using the `pygame` library.

The code was developed in Python 3.10.

## Algorithms

The following algorithms are implemented:

* Breadth First Search
* Depth First Search
* Greedy Search
* Iterative Deepening Search
* A* Search
* Weighted A* Search
* Genetic Algorithm

## Heuristics

The following heuristics are implemented:

* Manhattan Distance
* Chebyshev Distance
* Euclidean Distance

## Code Structure

The code's arquitecture is based on the MVC (Model-View-Controller) pattern.
The code is structured as follows:

* `/algorithms/`: The search algorithms
* `/assets/`: The assets used in the program
* `/controller/`: The controller classes
* `/menu/`: The menu classes
* `/model/`: The model classes
* `/view/`: The view classes

## Running the Code

The code can be run from the command line using the following command:

```pyhton
python3 main.py [--statistics]
```

### Dependencies

The dependencies needed to run the code are present in the `requirements.txt` file. They can be installed using the following command:

```python
pip3 install -r requirements.txt
```

### Statistics

The `--statistics` flag can be used to print statistics about the search. The statistics are outputed to a `results.xlsx` file.

## Output

The output of the program is the game itself. The visualization is done using the `pygame` and `pygame_menu` libraries.

## Gameplay

### Choose maze and algorithm in the menu.
<img src="https://user-images.githubusercontent.com/72521279/229518097-cbafe654-3f7d-49f0-ad3d-37d2da3c5a55.PNG" width="600">

### Reach the end before the time runs out!
<img src="https://user-images.githubusercontent.com/72521279/229518149-0e227421-cf6c-4441-96a7-8d982ddc0a23.PNG" width="600">

### If you feel stuck, just press H and get a tip!
<img src="https://user-images.githubusercontent.com/72521279/229518192-de2a5322-273a-46e1-9516-d79598cc019a.PNG" width="600">

### Have a chosen search algorithm solve the maze for you.  
<img src="https://user-images.githubusercontent.com/72521279/229518199-e2a3eaaf-bff5-4448-a61e-899309551f06.PNG" width="600">

## Group Members

* Lia Vieira (up202005042@fe.up.pt)
* Marco André(up202004891@fe.up.pt)
* Ricardo Matos(up202007962@fe.up.pt)
