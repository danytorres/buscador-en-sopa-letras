[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3142768&assignment_repo_type=AssignmentRepo)
# Word Search Exercise

This challenge involves finding words in an 8x8 grid. Given a string of 64 *letters* and a string of words to find, convert the string to an 8x8 array, and return `true` if _all_ words in the string can be found in the array. Return `false` otherwise. Words can be read in any direction (horizontally, vertically or diagonally).

You should write the code inside the curly braces, where it says `Your amazing code here`.

## Examples

```python
letters = "PSUWHATSLPACKAGENYOLRDVLFINGEZBMIREHQNJOATBVGYESJDUWUESTPSTICKEY"
words = ["stick", "most", "key", "vein", "yes", "package", "tube", "target", "elm", "spy"]
```

This would give the list below:

```python
[
  ["P", "S", "U", "W", "H", "A", "T", "S"],
  ["L", "P", "A", "C", "K", "A", "G", "E"],
  ["N", "Y", "O", "L", "R", "D", "V", "L"],
  ["F", "I", "N", "G", "E", "Z", "B", "M"],
  ["I", "R", "E", "H", "Q", "N", "J", "O"],
  ["A", "T", "B", "V", "G", "Y", "E", "S"],
  ["J", "D", "U", "W", "U", "E", "S", "T"],
  ["P", "S", "T", "I", "C", "K", "E", "Y"]
]
```

You would return `true` as all words can be found:

```python
[
  ["_", "S", "_", "_", "_", "_", "T", "_"],
  ["_", "P", "A", "C", "K", "A", "G", "E"],
  ["N", "Y", "_", "_", "R", "_", "_", "L"],
  ["_", "I", "_", "G", "_", "_", "_", "M"],
  ["_", "_", "E", "_", "_", "_", "_", "O"],
  ["_", "T", "B", "V", "_", "Y", "E", "S"],
  ["_", "_", "U", "_", "_", "E", "_", "T"],
  ["_", "S", "T", "I", "C", "K", "_", "_"]
]
```

## Local Test

For testing your code you must run: 

```sh
pytest
```

## Notes:

- You can read the test files, so you can have an idea of what is the expected result, but **do not edit them** please.

- Words must be contained inside the grid, without wrapping over columns/rows.

- **Check for map, slice, wrap python functions** in your solution.

If you have any doubts, feel free to ask 😊

Good luck! 🚀

Made with 💚 for Hackademy 🇲🇽.