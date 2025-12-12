from pathlib import Path

# Define folder
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)  # Create folder if it doesn't exist

# Define file
hello_file = data_dir / "hello.txt"

# Write text to file
hello_file.write_text("Hello from Python!")

# Read content
content = hello_file.read_text()
print(content)
