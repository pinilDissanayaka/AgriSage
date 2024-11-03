import os
import random

# List of backend-related commit messages
commit_messages = [
    "Implement new API endpoint",
    "Optimize database queries",
    "Refactor code structure",
    "Add error handling",
    "Improve logging",
    "Update dependencies",
    "Implement authentication",
    "Fix data validation bug",
    "Enhance security features",
    "Optimize server response time",
    "Refactor configuration settings",
    "Add unit tests for new modules",
    "Fix race condition in async function",
    "Improve data serialization",
    "Enhance caching mechanisms",
]

# Path to the backend file you want to modify (e.g., app.py)
backend_file = "server.py"

def make_commit(days: int):
    if days < 1:
        return os.system("git push origin main")
    else:
        # Randomly select a number of commits for each day (between 1 and 3)
        num_commits = random.randint(1, 3)
        dates = f"{days} days ago"
        
        for _ in range(num_commits):
            # Modify the backend file by appending a comment to simulate a change
            with open(backend_file, "a") as file:
                file.write(f"# Commit made {dates}\n")

            os.system("git add " + backend_file)
            
            # Select a random backend-related commit message
            message = random.choice(commit_messages)
            os.system(f'git commit --date="{dates}" -m "{message}"')
        
        return make_commit(days - 1)

if __name__ == "__main__":
    # Ensure the file exists before starting
    if not os.path.exists(backend_file):
        with open(backend_file, "w") as file:
            file.write("# Backend Project\n\n# Initial setup\n\n")

    make_commit(120)