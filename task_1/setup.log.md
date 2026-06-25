# Setup

## 1. Getting to the required location

cd /d/Aditya/COLLEGE/Coding/Synergy_StudentProject

## 2. Creating a directory

mkdir Synergy_TP
cd Synergy_TP

## 3. Initialize Git

git init

## 4. Creating the necessary files and folders

mkdir task_1
cd task_1

mkdir src
mkdir data

touch README.md
touch requirements.txt
touch setup_log.md
touch linux_commands.md
touch src/hello.py
touch data/sample.txt

## 5. Activating the virtual environment

python -m venv myenv
source myenv/Scripts/activate

## 6. Installing some packages

pip install numpy pandas matplotlib seaborn

## 7. Creating requirements.txt

pip freeze > requirements.txt

## 9. Git Commands

git status
git add .
git commit -m "Completed Task 1"

git remote add origin https://github.com/AdityaGuptaMIT/Synergy_TP.git

git branch -M main
git push -u origin main

