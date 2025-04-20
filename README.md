# Meme Generator  
### CIS 298 - Winter 2025
### Group #19 - Angie Fakih, Jeneen Jadallah, Afrah Mohamed

## Project Overview 
Our group project is a Meme Generator that pulls random quotes/jokes from an API and places them onto meme templates. We are using popular Python libraries like Pillow, requests, and Tkinter to create a fun and interactive program. Users will be able to select templates, generate memes, and share them. 

## Tasks & Roles 
We've split the project into three major tasks, and each group member is working on one of them: 

1. API Fetcher (Afrah): Write code to fetch random jokes/quotes from an API. Handle errors and ensure the text returned is clean and ready for use in the meme.

2. Image Editor (Jeneen): Use the Pillow library to add the fetched quote/joke onto a meme template. Handle resizing, positioning, and saving the generated meme.

3. GUI (Angie): Build a user interface (GUI) where users can select a meme template, input a quote, and generate the meme. The interface will allow for seamless meme creation.

## Branching & Workflow
We have structured our work with separate branchs for each task. This allows each team member to work independently on their part without interfering with others' progress. 
- Main Branch: Holds the final project and working meme generator. This is where all pull requests were merged.
- API Fetcher Branch: Afrah worked on this branch.
- Image Editor Branch: Jeneen worked on this branch.
- GUI Branch: Angie worked on this branch.

## Commit Breakdown 
1. Initial Commit
- Description: Set up the basic project structure, including the main.py file, requirements.txt, and the folders for each task (API fetcher, image editor, and GUI).
- We created three separate branches for each team member to work on their role/part of the project.
- We separated the tasks into GitHub issues and assigned each teammate to their specific task. Each teammate will focus on their respective modeule while tracking progress through issues.

2. Added API functionality (initial version) 
- Implemented the API functionality in its corresponding folder and then tested it in the main.py file.
- Successful implementation was proven with debugging and fallback messages in case of errors.
- Joke successfully printed in the console after being fetched from online API.

## Libraries Used 
- Pillow: For image manipulation and meme generation
- requests: To fetch random quotes/jokes from the API.
- Tkinter: For building the GUI.
- random, os, io: For basic functionality like randomizing meme captions and handling files.

## Next Steps 
***We will continue working on our assigned tasks, commit our progress regularly, and merge everything into the main branch. We'll be updating the README as we go to reflect our progess.***
