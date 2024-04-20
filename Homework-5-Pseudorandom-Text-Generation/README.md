## Not-So-Random Text Generation

Making the computer generate text automatically is an interesting and challenging problem. A simplistic approach to do so is to randomly select a word from the dictionary, print it out on the screen and repeat. However, some words, such as 'the', 'a' and 'an', are used with a higher frequency than others. Not taking this frequency in account would lead to incomprehensible text.

In this assignment, you have to make a program which asks for the name of a text file from the user, reads every word in than text file and stores the frequency of each word, and then generates random text using that frequency. For example, assume that the computer is provided with the text file given below.

![](https://cdn.mathpix.com/cropped/2024_04_19_ec78db0d6692e4090cfbg-4.jpg?height=272&width=637&top_left_y=645&top_left_x=105)

Here, the file consists of five lines and 25 words. You program should read each line and then separate the words. For simplicity, we can assume that words are separated by non-alphanumeric characters. Therefore, all punctuations are to be ignored. To simplify further, your program should convert all words to lowercase. An extra processing step (that will help us later) is to use the newline character sequence (which is `\r\n` in windows) as a word. This will help us keep track of how many times a new line occurs on the average. As a result, your program should store the following information from the file above in list/array as:
| **index** | **string**           | **frequency** |
| :---- | :---------------- | :----|
| 0     | hickory           | 2    |
| 1     | dickory           | 2    |
| 2     | dock              | 2    |
| 3     | \r\n              | 5    |
| 4     | the               | 4    |
| 5     | mouse             | 2    |
| 6     | ran               | 2    |
| 7     | up                | 1    |
| 8     | clock             | 2    |
| 9     | struck            | 1    |
| 10    | one               | 1    |
| 11    | down              | 1    |

The easiest way to do so is to make two lists/arrays. One list/array would be an list/array of words (as strings) and the other of frequency of the corresponding word (as integers). For example, the word mouse, at index 4 in both lists/arrays, occurs 2 times in the text file. Every time you read a word, you should search for it in the string list/array. If found, you should increment the corresponding index in the frequency list/array. Otherwise you should add the word and its frequency (which is going to be 1 the first time) to the lists/arrays.

Your program should then display the total number of words, the word with the highest frequency (ignoring newlines), and the highest frequency. For instance, the output for our example text file would be: 

```
25 the 4
```

Now we can use this information in the lists/arrays to generate text. This is done by randomly selecting a word from all the words in the text file. This can be achieved by using the rand() function (the mod operator % will be handy here). Suppose this randomly selected number is 16 . Now we look up in the frequency list/array and select the word corresponding to this cumulative frequency. This can be achieved by adding the frequency of each word in the list/array until we reach this random number. In our example, it means selecting the word **mouse**. We output this word and then repeat the process by selecting another random number. Note that new line characters will automatically be selected as we counted them as a word. Here's some sample output for our text file. Also, there may occur some empty sentences. That is perfectly okay (Some people just don't say much).

```
mouse dickory dock hickory one ran

dock clock the ran clock up up the one

hickory mouse the dock

one

dickory

hickory ran up ran

clock hickory the mouse the clock the

ran

hickory the the dock mouse the

up struck one the the dickory clock dock dickory mouse the
```

**Submission:**
   - Push your Python Jupyter Notenook named `Submission.ipynb` at [programming-fundamentals/Homework-4-Pseudorandom-Text-Generation](https://github.com/programming-fundamentals/Homework-4-Pseudorandom-Text-Generation).
   - Ensure your code adheres to proper Python coding standards and includes necessary comments and documentation.

Best of luck!

PS: Some free books as available as text files from Project Gutenberg (http://www.gutenberg.org/) and you may want to use some your program. While the text generated here is usually grammatically incorrect, the selection technique (using frequencies) can be extended further to include probabilities of finding TWO words instead of one. For students who find this interesting, an interesting article is available in the book Programming Pearls by Jon Bentley. (http://www.cs.belllabs.com/cm/cs/pearls/sec153.html)
