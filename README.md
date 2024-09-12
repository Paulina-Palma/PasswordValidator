# Password Validator
Checks if passwords stored in a text file meet certain security requirements.  
It reads passwords from an input file (passwords.txt), validates them according to specified rules (such as minimum length, the presence of uppercase letters, numbers, and special characters), and writes only the valid passwords to an output file (safe.txt).   
Invalid passwords are logged with error messages for debugging or review purposes.  

## Key Features:
- **Input Handling**: Reads passwords from a text file.
- **Validation**: Uses custom rules (e.g., length, character types) to ensure password security.
- **Error Handling**: Catches and logs validation errors.
- **Output**: Writes valid passwords to a new file for safe use.

It’s designed for automating password checks from large lists, ensuring only strong passwords are kept.
