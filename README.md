# 😂 Memeify (Meme Generator App)
### CIS 298 - Winter 2025
### Group #19 - Angie Fakih, Jeneen Jadallah, Afrah Mohamed

## Project Overview 
Our group project is a Meme Generator called Memeify that pulls random quotes/jokes from an API and places them onto meme templates. We are using popular Python libraries like Pillow, requests, and Tkinter to create a fun and interactive program. Users will be able to select templates, generate memes, and share them. 

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

## Project Commit Log

| Commit # | Title                                               | Description                                                                                 | Who                    |
|----------|-----------------------------------------------------|---------------------------------------------------------------------------------------------|------------------------|
| 1        | Initial Commit                                       | Project creation, selected topic, and got approval from professor                          | Afrah                  |
| 2        | Created `README.md`                                  | Set up basic structure and project description                                              | Afrah                  |
| 3        | Initial Project Structure                            | Created empty files: `fetch_api.py`, `image_editor.py`, `gui.py`                           | Angie, Jeneen, Afrah                |
| 4        | Updated `README.md`                                  | Added project overview and initial planning notes                                           | Angie, Jeneen, Afrah                |
| 5        | Added API Functionality - Initial Commit             | Implemented basic API call logic in `fetch_api.py`                                         | Afrah                  |
| 6        | Merged API Fetcher Pull Request                      | Merged PR #4 from `afrah30/api-fetcher` into main                                           | Afrah                  |
| 7        | Updated `README.md` Again                            | Logged commit progress and documented API integration                                       | Angie, Jeneen, Afrah   |
| 8        | Developed Image Editor Module                        | Implemented `wrap_text` and `create_meme` functions in `image_editor.py` using PIL         | Jeneen                 |
| 9        | Added Image Editor Functionalities                   | Integrated meme rendering with font, alignment, resizing, and color options                | Jeneen                 |
| 10       | Built CLI Entrypoint with `main.py`                  | Developed argument parsing, integrated API + image editor, and handled output saving       | Jeneen                 |
| 11       | Meme Generator GUI Functional                        | Enabled template selection, joke fetching, and font rendering in GUI                       | Angie                  |
| 12       | Refined UI + Dark Mode Toggle                        | Improved interface, added theme toggle, and allowed meme saving                            | Angie                  |
| 13       | Random Meme Generator Added                          | Created random meme generator pulling from `templates/` folder                             | Angie                  |
| 14       | Merged GUI Interface Branch                          | Merged `gui-interface` branch into `main`                                                  | Afrah                  |
| 15        | Refined Image Editor                                 | Improved text wrapping logic, adjusted font scaling, added layout fallbacks                | Jeneen                 |
| 16       | Final Merge After API Reset                          | Resolved final integration conflicts and reset API logic                                   | Afrah                  |
| 17       | GroupEval Forms Added                                | Added completed `GroupEval.docx` for each team member                                      | Angie, Jeneen, Afrah   |

## Libraries Used 
| Library         | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `requests`      | To fetch jokes or data from external APIs                               |
| `Pillow (PIL)`  | For image manipulation and rendering text onto images                   |
| `tkinter`       | For building the optional graphical user interface (GUI)                |
| `argparse`      | For command-line argument parsing in `main.py`                          |
| `os`            | For file and directory handling                                         |
| `datetime`      | To timestamp meme files during save                                     |
| `textwrap`      | To wrap long joke text into lines that fit inside the image             |
| `json`          | For parsing API responses                                               |
| `threading`     | For improving GUI responsiveness during API fetches 

## What We Learned

Throughout this project, our team gained hands-on experience working with a variety of popular and powerful Python libraries. Here are some of the key takeaways:

- **Pillow (PIL):** We learned how to manipulate images programmatically — including resizing, text rendering, font scaling, and drawing multiline text with strokes. This gave us a deeper understanding of how image processing works under the hood.

- **requests & APIs:** We learned how to fetch dynamic data from external APIs and handle JSON responses, helping us understand how backend systems communicate with applications.

- **argparse:** Building a CLI with customizable arguments showed us how to create flexible tools that can be run directly from the terminal, improving usability for different users.

- **Modular Design:** Splitting the project into separate modules (`api_fetcher.py`, `image_editor.py`, `main.py`, `gui.py`) helped us practice clean coding principles and maintainable architecture.

- **Version Control & GitHub Collaboration:** We practiced using branches, pull requests, and commit histories to work as a team, resolve merge conflicts, and document progress.

- **User Interfaces (GUI/CLI):** We explored both graphical and command-line interfaces, enhancing our understanding of user experience and interface design.

- **Teamwork & Communication:** We strengthened our collaboration skills by dividing responsibilities, reviewing each other’s code, and integrating our work into a unified application.

This project not only reinforced Python fundamentals but also taught us how to take an idea from concept to execution in a real-world development environment that is functional and fun!
