# Crime Investigation & Case Management System

## Overview
The Crime Investigation & Case Management System is a Python-based command-line interface (CLI) application designed to assist law enforcement agencies in managing crime investigations and case records. The system provides features such as case tracking, suspect management, evidence logging, and report generation.

## Features
- Case Management: Add, update, and track crime cases.
- Suspect Management: Store details of suspects and link them to cases.
- Evidence Logging: Record evidence and attach it to relevant cases.
- Officer Management: Assign investigating officers to cases.
- Report Generation: Generate reports on case progress.

## Technologies Used
- Python: Core programming language.
- SQLAlchemy: Database management and ORM.
- Pipenv: Virtual environment and dependency management.
- SQLite: Database storage.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Amaaaarrrrrr/crime_sqlproject.git
   cd crime_sqlproject
   ```

2. Activate virtual environment using Pipenv:
   ```bash
   pipenv shell
   ```

3. Install dependencies:
   ```bash
   pipenv install
   ```

4. Run the application:
   ```bash
   python cli.py
   ```

## Usage
- Follow the CLI prompts to perform various actions such as adding cases, suspects, evidence, and generating reports.
- Ensure all required fields are provided when adding new records.

## Database Setup
- The application uses **SQLite** as the default database.
- The database schema is managed using **SQLAlchemy**.
- If needed, migrate the database by running:
  ```bash
  python database.py
  ```

## Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

## Contact
- **Developer:** Joy Mutanu  
- **GitHub:** [Amaaaarrrrrr](https://github.com/Amaaaarrrrrr)  

