# Password Validator
Checks if passwords stored in a text file meet certain security requirements.  
It reads passwords from an input file (passwords.txt), validates them according to specified rules such as:
- minimum length,
- the presence of uppercase letters,
- numbers,
- and special characters   

and writes only the valid passwords to an output file (safe.txt).   
Invalid passwords are logged with error messages for debugging or review purposes.  

## Key Features:
- **Input Handling**: Reads passwords from a text file.
- **Validation**: Uses custom rules (e.g., length, character types) to ensure password security.
- **Error Handling**: Catches and logs validation errors.
- **Output**: Writes valid passwords to a new file for safe use.

It’s designed for automating password checks from large lists, ensuring only strong passwords are kept.

## Project Overview:
**Goal**: The project validates a password by running it through multiple checks, ensuring that it meets security standards like length, character variety (numbers, uppercase, lowercase, special characters), and even checking if it has been compromised in a data breach (using the Have I Been Pwned API).  
**Validators**: Each validation criterion is encapsulated in its own class, which makes the design flexible and easy to extend.

## Key Components:
1. **Abstract Validator Class**:
Validator: Serves as the abstract base class for all validators. It forces each subclass to implement the is_valid() method.
2. **Validators**:
- HasNumberValidator: Checks if the password contains a number
- HasUpperCharacterValidator: Checks if there is at least one uppercase letter
- HasLowerCharacterValidator: Checks for at least one lowercase letter
- HasSpecialCharacterValidator: Ensures the presence of at least one special character
- LengthValidator: Ensures the password meets a minimum length requirement (default 8 characters)
- HaveIbeenPwndValidator: Uses the Have I Been Pwned API to check if the password has been exposed in a data breach
3. **PasswordValidator Class**:
PasswordValidator: Takes the password as input and sequentially runs it through all validators. If the password passes all checks, it’s considered valid.

