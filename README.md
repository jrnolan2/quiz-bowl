# Quiz Bowl
A simple program that asks questions from the [QBReader database](https://www.qbreader.org/backups) in proportion to the number of people who ask for each category.

## How to Run
1. Download the most recent question set from the [QBReader database](https://www.qbreader.org/backups) Google Drive. Find the most recent tossups.json file.
2. Put tossups.json in the same folder as quizbowl.py
3. Fill in the number of people who want each category in the `category_weights.cfg` file
### Command line: quizbowl.py
4. Run quizbowl.py with Python
5. Press enter to go to the next question
### Web browser: app.py
4. Install Flask if not already installed with `pip install flask`
5. Run app.py with Python
6. Open `http://localhost:5001/` on your browser
7. Press "Show Answer" -> "Next Question" to reveal next question