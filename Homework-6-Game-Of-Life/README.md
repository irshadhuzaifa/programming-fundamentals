## Conway's Game of Life

The Game of Life is a simulation originally conceived by the British mathematician J. H. Conway in 1970 and popularized by Martin Gardner in his Scientific American column. The game models the life cycle of bacteria using a two-dimensional grid of cells. Given an initial pattern, the game simulates the birth and death of future generations of cells using a set of simple rules. In this assignment you will implement a simplified version of Conway's simulation and a basic user interface for watching the bacteria grow over time.

The game is basically a simulation played on a grid. Each grid location is either empty or occupied by a single living cell (`X`). A location's neighbours are any cells in the surrounding eight adjacent locations. In the example at right, the shaded middle location has three neighbours containing living cells. A cell that is on the border of the grid has fewer than eight neighbours. For example,

![](https://cdn.mathpix.com/cropped/2024_04_19_ec78db0d6692e4090cfbg-1.jpg?height=173&width=214&top_left_y=754&top_left_x=1801)

the top-right `X` cell in the example at right has only three neighbouring cells, and only one of them contains a living cell (the shaded cell), so it has one living neighbour.

The simulation starts with an initial pattern of cells on the grid and computes successive generations of cells according to the following rules:

- A location that has zero or one neighbours will be empty in the next generation. If a cell was there, it dies.
- A location with two neighbours is stable. If it had a cell, it still contains a cell. If it was empty, it's still empty.
- A location with three neighbours will contain a cell in the next generation. If it was unoccupied before, a new cell is born. If it currently contains a cell, the cell remains.
- A location with four or more neighbours will be empty in the next generation. If there was a cell in that location, it dies of overcrowding.

The births and deaths that transform one generation to the next all take effect simultaneously. When you are computing a new generation, new births/deaths in that generation don't impact other cells in that generation. Any changes (births or deaths) in a given generation `k` start to have effect on other neighbouring cells in generation `k+1`.

Check your understanding of the game rules by looking at the following example at right. The two patterns at right should alternate forever.

![](https://cdn.mathpix.com/cropped/2024_04_19_ec78db0d6692e4090cfbg-2.jpg?height=300&width=680&top_left_y=110&top_left_x=1057)

Here is a second example. The pattern at right does not change on each iteration, because each cell has exactly three living neighbours. This is called a "stable" pattern or a "still life".

![](https://cdn.mathpix.com/cropped/2024_04_19_ec78db0d6692e4090cfbg-2.jpg?height=293&width=344&top_left_y=474&top_left_x=1129)

The grid of bacteria in your program gets its initial state from one of a set of provided input text files, which follow a particular format. When your program reads the grid file, you should re-prompt the user if the file specified does not exist. If it does exist, you may assume that all of its contents are valid. You do not need to write any code to handle a misformatted file. The behaviour of your program in such a case is not defined in this spec; it can crash, it can terminate, etc. You may also assume that the input file name typed by the user does not contain any spaces.

In each input file, the first two lines will contain integers $r$ and $c$ representing the number of rows and columns in the grid, respectively. The next lines of the file will contain the grid itself, a set of characters of size `r * c` with a line break (`\n`) after each row. Each grid character will be either a `-` (minus sign) for an empty dead cell, or an `X` (uppercase 'X') for a living cell. The input file might contain additional lines of information after the grid lines, such as comments by its author; any such content should be ignored by your program.

The input files will exist in the same working directory as your program. For example, the following text might be the contents of a file simple.txt, a `5 * 9` grid with 3 initially live cells:

![](https://cdn.mathpix.com/cropped/2024_04_19_ec78db0d6692e4090cfbg-2.jpg?height=322&width=1089&top_left_y=1693&top_left_x=125)

Your Game of Life program should begin by prompting the user for a file name and using that file's contents to set the initial state of your bacterial colony grid. Then it will allow the user to advance the colony through generations of growth. The user can type **t** to "tick" forward the bacteria simulation by one generation, or a to begin an animation loop that ticks forward the simulation by several generations, once every 50 milliseconds, **s** to save the loaded file, or **q** to quit.

It is tempting to try to write your entire program and then try to compile and run it; we do not recommend that strategy. Instead, you should develop your program incrementally: Write a small piece of functionality, then test/debug it until it works, then move on to another small piece. This way you are always making small consistent improvements to a base of working code. Here is a possible list of steps to develop a solution:

1. Intro: Get your basic project running, and write code to print the introductory welcome message.
2. File input: Write code to prompt for a file name, and open and print that file's lines to the console. Once this works, try reading the individual grid cells and turning them into a Grid object. Print the Grid's state on the console just to see if it has the right data in it. Use a simple test case, e.g. `simple.txt`.
3. Grid display: Write code to print the current state of the grid, without modifying that state.
4. Updating to next generation: Write code to advance the grid from one generation to the next. Insert cout statements to print important values as you go through your loops and code. Try printing out what indexes your code is examining, along with your count of how many neighbours each cell has, to make sure you are counting them properly.
5. Overall menu and animation: Implement the program's main menu and the animation feature. If all of the preceding steps are finished and work properly, this should not be as difficult to get working.

When you are trying to advance the bacteria from one generation to the next, you cannot do this `in place" by modifying your grid as you loop over it. Doing so will change the cells and their neighbours and break the neighbour counts for nearby cells. So you will need to create a temporary second grid. Your existing grid represents the current generation of bacteria, and you can create a second temporary second grid that allows you to compute and store the next generation without changing the current one. Once you have filled the second grid with the next generation's cell information, you can copy its contents back into the original grid and discard the temporary copy.

One tricky part of this assignment is that the edges of the grid have to be handled with care, because you don't want your code to try to access a grid index that is out of bounds. Your algorithm for examining cells and counting neighbours should handle edges and inner cells elegantly and without redundancy as much as possible. _Some students try to achieve this by creating an extra layer around the grid; for example, a `5 * 9` input file will be put into a `7 * 11` Grid object. We do not want you to solve the problem in this way, for several reasons: it avoids some of the challenges of the assignment; it wastes memory; and it introduces other hacks and kludges in your code to adjust the indexes to work properly. Avoid an "extra row/column" solution._

**Submission:**
   - Push your Python Jupyter Notenook named `Submission.ipynb` at [programming-fundamentals/Homework-6-Game-Of-Life](https://github.com/programming-fundamentals/Homework-6-Game-Of-Life).
   - Ensure your code adheres to proper Python coding standards and includes necessary comments and documentation.
