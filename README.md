## Repository for two Meeting Scheduling Problem (MSP) solving approaches.

- **1st solver**: [lingoSolver.lg4](lingoSolver.lg4) is a LINGO program that uses Branch & Bound algorithm to solve the example instance.
- **2nd solver**: [MSP.py](MSP.py) is a Python-based program that uses Backtracking to iterate over all the possible solutions of the example instance.

### Requirements:
- **1st solver**: [LINGO 18.0](https://www.lindo.com/index.php/products/lingo-and-optimization-modeling)
- **2nd solver**: [Python 3.8](https://www.python.org/)

### 1st Solver Usage:
- Run [lingoSolver.lg4](lingoSolver.lg4) in LINGO and execute the Solve function.

### 2nd Solver Usage:
- Clone this repository and execute [MSP.py](MSP.py) in terminal.

```Python
python MSP.py
```
- **Input**: See [exampleInstance.dat](exampleInstance.dat) for input details.
- **Output**: See [exampleOutput.dat](exampleOutput.dat) for output details.