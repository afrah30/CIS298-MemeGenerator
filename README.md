# 😂 Memeify (Meme Generator App)
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

## 📦 Project Commit Log

| Commit # | Title                                               | Description                                                                                 | Who           |
|----------|-----------------------------------------------------|---------------------------------------------------------------------------------------------|---------------|
| 1        | Initial Commit                                       | Project creation, selected topic, and got approval from professor                          |               | Afrah
| 2        | Created `README.md`                                  | Set up basic structure and project description                                              |               | Afrah
| 3        | Initial Project Structure                            | Created empty files: `fetch_api.py`, `image_editor.py`, `gui.py`                           |               | Angie
| 4        | Updated `README.md`                                  | Added project overview and initial planning notes                                           |               | Jeneen
| 5        | Added API Functionality - Initial Commit             | Implemented basic API call logic in `fetch_api.py`                                         |               |Afrah
| 6        | Merged API Fetcher Pull Request                      | Merged PR #4 from `afrah30/api-fetcher` into main                                           |               | Afrah
| 7        | Updated `README.md` Again                            | Logged commit progress and documented API integration                                       |               | Angie, Jeneen, Afrah
| 8        | Added Image Editor Functionalities                   | Integrated image manipulation functions into `image_editor.py`                             |               | Jeneen
| 9        | Meme Generator GUI Functional                        | Enabled template selection, joke fetching, and font rendering in GUI                       |               | Angie
| 10       | Refined UI + Dark Mode Toggle                        | Improved interface, added theme toggle, and allowed meme saving                            |               | Angie
| 11       | Random Meme Generator Added                          | Created random meme generator pulling from `templates/` folder                             |               | Angie
| 12       | Merged GUI Interface Branch                          | Merged `gui-interface` branch into `main`                                                  |               | Angie
| 13       | Final Merge After API Reset                          | Resolved final integration conflicts and reset API logic                                   |               | Afrah
| 14       | GroupEval Forms Added                                | Added completed `GroupEval.docx` for each team member                                      |               | Angie, Jeneen, Afrah

## Libraries Used 

| Library         | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `requests`      | To fetch jokes or data from external APIs                               |
| `Pillow (PIL)`  | For image manipulation and rendering text onto images                   |
| `tkinter`       | For building the graphical user interface (GUI)                         |
| `random`        | For randomizing meme templates                                          |
| `os`            | For handling file paths and directory management                        |
| `io`            | For handling in-memory files (e.g., saving images without writing temp) |


