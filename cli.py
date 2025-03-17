from models import Case, Suspect, Evidence, Detective, CriminalRecord
from database import Session
from colorama import Fore, Style, init
from tabulate import tabulate
import time
import random
from datetime import datetime
from sqlalchemy.sql.expression import func
from faker import Faker 
# Initialize Faker
fake = Faker()

init(autoreset=True)  # Initialize colorama for colored output

def print_header(title):
    """Prints a formatted section header."""
    print(Fore.CYAN + "\n" + "=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50 + "\n" + Style.RESET_ALL)

def main():
    """Main menu loop for the system."""
    while True:
        print_header("📌 Crime Investigation & Case Management System")
        print(Fore.YELLOW + "1️⃣ Manage Cases")
        print(Fore.YELLOW + "2️⃣ Manage Suspects")
        print(Fore.YELLOW + "3️⃣ Manage Evidence")
        print(Fore.YELLOW + "4️⃣ Manage Detectives")
        print(Fore.YELLOW + "5️⃣ Manage Criminal Records")
        print(Fore.RED + "0️⃣ Exit")
        
        choice = input(Fore.GREEN + "Enter your choice: ")
        
        if choice == "1":
            case_menu()
        elif choice == "2":
            suspect_menu()
        elif choice == "3":
            evidence_menu()
        elif choice == "4":
            detective_menu()
        elif choice == "5":
            criminal_record_menu()
        elif choice == "0":
            print(Fore.RED + "🚪 Exiting the system. Goodbye!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

### **Case Management**
def case_menu():
    """Manages cases in the system."""
    while True:
        print_header("📂 Case Management")
        print("1️⃣ Add a New Case")
        print("2️⃣ View All Cases")
        print("3️⃣ Find Case by ID")
        print("4️⃣ Delete Case")
        print("5️⃣ Generate Random Case (Using Faker)")
        print("0️⃣ Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            crime_type = input("Enter crime type: ")
            status = input("Enter status (Open/Closed): ")
            location = input("Enter location: ")
            date = input("Enter date (YYYY-MM-DD): ")
            Case.create(crime_type, status, location, date)
            print(Fore.GREEN + "✅ Case added successfully!")
        
        elif choice == "2":
            cases = Case.get_all()
            if cases:
                print(Fore.BLUE + tabulate([[c.id, c.crime_type, c.status, c.location, c.date] for c in cases],
                                          headers=["ID", "Crime Type", "Status", "Location", "Date"],
                                          tablefmt="grid"))
            else:
                print(Fore.RED + "❌ No cases found.")
        
        elif choice == "3":
            case_id = input("Enter Case ID: ")
            case = Case.find_by_id(int(case_id)) if case_id.isdigit() else None
            if case:
                print(Fore.GREEN + f"✅ Found Case: {case.crime_type}, Status: {case.status}, Location: {case.location}, Date: {case.date}")
            else:
                print(Fore.RED + "❌ Case not found.")

        elif choice == "4":
            case_id = input("Enter Case ID to delete: ")
            if case_id.isdigit():
                Case.delete(int(case_id))
                print(Fore.GREEN + "✅ Case deleted successfully!")
            else:
                print(Fore.RED + "❌ Invalid ID.")
        
        elif choice == "5":
            generate_random_case()
        
        elif choice == "0":
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

def generate_random_case():
    """Creates and adds a random unsolved case to the database using Faker."""
    try:
        crime_types = ["Robbery", "Murder", "Kidnapping", "Fraud", "Burglary", "Assault", "Arson", "Cybercrime"]
        statuses = ["Open", "Under Investigation", "Closed"]

        crime_type = random.choice(crime_types)
        location = fake.address()  # Generate a realistic address
        status = random.choice(statuses)
        date = fake.date_between(start_date="-5y", end_date="today").strftime("%Y-%m-%d")  # Random past date

        new_case = Case.create(crime_type=crime_type, status=status, location=location, date=date)
        print(Fore.GREEN + f"✅ Case added: {crime_type}, Status: {status}, Location: {location}, Date: {date}")
    except Exception as e:
        print(Fore.RED + f"\n❌ Error generating case: {str(e)}\n")

    # Pause before returning to menu
    input(Fore.YELLOW + "Press Enter to return to the menu...")


def suspect_menu():
    """Manages suspects in the system."""
    while True:
        print_header("🚔 Suspect Management")
        print("1️⃣ Add a Suspect")
        print("2️⃣ View All Suspects")
        print("3️⃣ Find Suspect by ID")
        print("4️⃣ Delete Suspect")
        print("5️⃣ Generate Random Suspect")
        print("0️⃣ Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter suspect's name: ")
            age = input("Enter suspect's age: ")
            alibi = input("Enter suspect's alibi (or leave blank): ")
            case_id = input("Enter associated Case ID: ")

            if not age.isdigit():
                print(Fore.RED + "❌ Invalid age. Please enter a number.")
                continue
            if not case_id.isdigit():
                print(Fore.RED + "❌ Invalid Case ID. Please enter a number.")
                continue

            Suspect.create(name=name, age=int(age), alibi=alibi if alibi else None, case_id=int(case_id))
            print(Fore.GREEN + "✅ Suspect added successfully!")

        elif choice == "2":
            suspects = Suspect.get_all()
            if suspects:
                print(Fore.BLUE + tabulate(
                    [[s.id, s.name, s.age, s.alibi if s.alibi else "N/A", s.case_id] for s in suspects],
                    headers=["ID", "Name", "Age", "Alibi", "Case ID"],
                    tablefmt="grid"))
            else:
                print(Fore.RED + "❌ No suspects found.")

        elif choice == "3":
            suspect_id = input("Enter Suspect ID: ")
            if suspect_id.isdigit():
                suspect = Suspect.find_by_id(int(suspect_id))
                if suspect:
                    print(Fore.GREEN + f"✅ Found Suspect: {suspect.name}, Age: {suspect.age}, Alibi: {suspect.alibi if suspect.alibi else 'N/A'}, Case ID: {suspect.case_id}")
                else:
                    print(Fore.RED + "❌ Suspect not found.")
            else:
                print(Fore.RED + "❌ Invalid ID. Please enter a number.")

        elif choice == "4":
            suspect_id = input("Enter Suspect ID to delete: ")
            if suspect_id.isdigit():
                Suspect.delete(int(suspect_id))
            else:
                print(Fore.RED + "❌ Invalid ID. Please enter a number.")

        elif choice == "5":
            generate_random_suspect()

        elif choice == "0":
            break

        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

def generate_random_suspect():
    """Creates and adds a random suspect using Faker."""
    try:
        name = fake.name()
        age = random.randint(18, 65)
        alibi = fake.sentence()
        case_id = random.randint(1, 100)  # Assuming case IDs range from 1-100

        new_suspect = Suspect.create(name=name, age=age, alibi=alibi, case_id=case_id)
        print(Fore.GREEN + f"✅ Suspect added: {name}, Alibi: {alibi}, case_id: {case_id}")

    except Exception as e:
        print(Fore.RED + f"\n❌ Error generating suspect: {str(e)}\n")

    input(Fore.YELLOW + "Press Enter to return to the menu...")


def evidence_menu():
    """Manages evidence in the system."""
    while True:
        print_header("🔍 Evidence Management")
        print("1️⃣ Add Evidence")
        print("2️⃣ View All Evidence")
        print("3️⃣ Find Evidence by ID")
        print("4️⃣ Delete Evidence")
        print("5️⃣ Generate Random Evidence")
        print("0️⃣ Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            case_id = input("Enter Case ID: ")
            description = input("Enter evidence description: ")
            found_location = input("Enter evidence location: ")

            if not case_id.isdigit():
                print(Fore.RED + "❌ Invalid Case ID. Please enter a number.")
                continue

            Evidence.create(description=description, found_location=found_location, case_id=int(case_id))
            print(Fore.GREEN + "✅ Evidence added successfully!")

        elif choice == "2":
            evidences = Evidence.get_all()
            if evidences:
                print(Fore.BLUE + tabulate(
                    [[e.id, e.case_id, e.description, e.found_location] for e in evidences],
                    headers=["ID", "Case ID", "Description", "Found Location"],
                    tablefmt="grid"))
            else:
                print(Fore.RED + "❌ No evidence found.")

        elif choice == "3":
            evidence_id = input("Enter Evidence ID: ")
            if evidence_id.isdigit():
                evidence = Evidence.find_by_id(int(evidence_id))
                if evidence:
                    print(Fore.GREEN + f"✅ Found Evidence: Case ID: {evidence.case_id}, Description: {evidence.description}, Location: {evidence.found_location}")
                else:
                    print(Fore.RED + "❌ Evidence not found.")
            else:
                print(Fore.RED + "❌ Invalid ID. Please enter a number.")

        elif choice == "4":
            evidence_id = input("Enter Evidence ID to delete: ")
            if evidence_id.isdigit():
                Evidence.delete(int(evidence_id))
            else:
                print(Fore.RED + "❌ Invalid ID. Please enter a number.")

        elif choice == "5":
            generate_random_evidence()

        elif choice == "0":
            break

        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

def generate_random_evidence():
    """Creates and adds a random piece of evidence."""
    session = Session()
    
    cases = session.query(Case).all()
    if not cases:
        print(Fore.RED + "❌ No cases found! Please add a case first.")
        return
    
    random_case = random.choice(cases)

    descriptions = ["Bloody knife", "Fingerprint on glass", "Security footage", "DNA sample", "Footprint at the scene"]
    locations = ["Living room", "Kitchen", "Parking lot", "Abandoned house", "Office building"]
    
    random_description = random.choice(descriptions)
    random_location = random.choice(locations)

    try:
        Evidence.create(description=random_description, found_location=random_location, case_id=random_case.id)
        print(Fore.GREEN + f"✅ Random evidence '{random_description}' added to case {random_case.id} at {random_location}.")
    except Exception as e:
        print(Fore.RED + f"\n❌ Error adding evidence: {str(e)}\n")

    session.close()
    input(Fore.YELLOW + "Press Enter to return to the menu...")


def detective_menu():
    """Manages detectives in the system."""
    while True:
        print_header("🕵️ Detective Management")
        print("1️⃣ Add a Detective")
        print("2️⃣ View All Detectives")
        print("3️⃣ Find Detective by ID")
        print("4️⃣ Delete Detective")
        print("5️⃣ Generate Random Detective")
        print("0️⃣ Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter detective's name: ").strip()
            rank = input("Enter detective's rank (default: 'Junior'): ").strip() or "Junior"
            solved_cases = input("Enter solved cases (default: 0): ").strip() or "0"

            if not solved_cases.isdigit():
                print(Fore.RED + "❌ Invalid input for solved cases. Please enter a number.")
                continue

            Detective.create(name=name, rank=rank, solved_cases=int(solved_cases))
            print(Fore.GREEN + f"✅ Detective '{name}' added successfully!")

        elif choice == "2":
            detectives = Detective.get_all()
            if detectives:
                print(Fore.BLUE + tabulate(
                    [[d.id, d.name, d.rank, d.solved_cases] for d in detectives],
                    headers=["ID", "Name", "Rank", "Solved Cases"],
                    tablefmt="grid"
                ))
            else:
                print(Fore.RED + "❌ No detectives found.")

        elif choice == "3":
            detective_id = input("Enter Detective ID: ").strip()
            if detective_id.isdigit():
                detective = Detective.find_by_id(int(detective_id))
                if detective:
                    print(Fore.GREEN + f"✅ Found Detective: {detective.name}, Rank: {detective.rank}, Solved Cases: {detective.solved_cases}")
                else:
                    print(Fore.RED + "❌ Detective not found.")
            else:
                print(Fore.RED + "❌ Invalid input. Please enter a valid number.")

        elif choice == "4":
            detective_id = input("Enter Detective ID to delete: ").strip()
            if detective_id.isdigit():
                Detective.delete(int(detective_id))
            else:
                print(Fore.RED + "❌ Invalid input. Please enter a valid number.")

        elif choice == "5":
            generate_random_detective()

        elif choice == "0":
            break

        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

def generate_random_detective():
    """Creates and adds a random detective."""
    names = ["James Carter", "Sarah Connor", "John Wick", "Emily Watson", "Mark Spencer"]
    ranks = ["Junior", "Senior", "Chief", "Inspector"]
    
    random_name = random.choice(names)
    random_rank = random.choice(ranks)
    random_solved_cases = random.randint(0, 50)

    try:
        Detective.create(name=random_name, rank=random_rank, solved_cases=random_solved_cases)

        session = Session()
        detective = session.query(Detective).filter_by(name=random_name).first()
        session.close()

        if detective:
            print(Fore.GREEN + f"✅ Detective '{detective.name}' (Rank: {detective.rank}, Solved Cases: {detective.solved_cases}) added successfully!")
        else:
            print(Fore.RED + "❌ Error: Detective was not found in the database after creation.")

    except Exception as e:
        print(Fore.RED + f"\n❌ Error generating detective: {str(e)}\n")

    input(Fore.YELLOW + "Press Enter to return to the menu...")


def criminal_record_menu():
    """Manages criminal records in the system."""
    while True:
        print_header("⚖️ Criminal Record Management")
        print("1️⃣ Add a Criminal Record")
        print("2️⃣ View All Criminal Records")
        print("3️⃣ Find Criminal Record by ID")
        print("4️⃣ Delete Criminal Record")
        print("5️⃣ Generate Random Criminal Record")
        print("0️⃣ Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            suspect_id = input("Enter Suspect ID: ").strip()
            if not suspect_id.isdigit():
                print(Fore.RED + "❌ Invalid Suspect ID. Please enter a valid number.")
                continue

            previous_crimes = input("Enter previous crimes: ").strip()
            sentence = input("Enter sentence: ").strip()

            if not previous_crimes or not sentence:
                print(Fore.RED + "❌ Previous crimes and sentence cannot be empty.")
                continue

            CriminalRecord.create(int(suspect_id), previous_crimes, sentence)
            print(Fore.GREEN + f"✅ Criminal record for Suspect ID {suspect_id} added successfully!")

        elif choice == "2":
            records = CriminalRecord.get_all()
            if records:
                print(Fore.BLUE + tabulate(
                    [[r.id, r.suspect_id, r.previous_crimes, r.sentence] for r in records],
                    headers=["ID", "Suspect ID", "Previous Crimes", "Sentence"],
                    tablefmt="grid"
                ))
            else:
                print(Fore.RED + "❌ No criminal records found.")

        elif choice == "3":
            record_id = input("Enter Criminal Record ID: ").strip()
            if record_id.isdigit():
                record = CriminalRecord.find_by_id(int(record_id))
                if record:
                    print(Fore.GREEN + f"✅ Found Record: Suspect ID: {record.suspect_id}, Crimes: {record.previous_crimes}, Sentence: {record.sentence}")
                else:
                    print(Fore.RED + "❌ Criminal record not found.")
            else:
                print(Fore.RED + "❌ Invalid input. Please enter a valid number.")

        elif choice == "4":
            record_id = input("Enter Criminal Record ID to delete: ").strip()
            if record_id.isdigit():
                CriminalRecord.delete(int(record_id))
            else:
                print(Fore.RED + "❌ Invalid input. Please enter a valid number.")

        elif choice == "5":
            generate_random_criminal_record()

        elif choice == "0":
            break

        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

def generate_random_criminal_record():
    """Creates and adds a random criminal record."""
    session = Session()

    try:
        # Fetch a random suspect from the database
        suspect = session.query(Suspect).order_by(func.random()).first()

        if not suspect:
            print(Fore.RED + "❌ Error: No suspects found. Please add a suspect first.")
            input(Fore.YELLOW + "Press Enter to return to the menu...")
            return  # Exit function if no suspect is found

        # Generate random crime details
        previous_crimes = fake.sentence()
        sentence = fake.sentence()

        # Create and commit the new criminal record
        CriminalRecord.create(suspect_id=suspect.id, previous_crimes=previous_crimes, sentence=sentence)

        # Retrieve the newly added criminal record
        new_record = session.query(CriminalRecord).filter_by(suspect_id=suspect.id).first()

        if new_record:
            print(Fore.GREEN + f"✅ Random Criminal Record Added: Suspect ID: {new_record.suspect_id}, Crimes: {new_record.previous_crimes}, Sentence: {new_record.sentence}")
        else:
            print(Fore.RED + "❌ Error: Criminal record creation failed!")

    except Exception as e:
        print(Fore.RED + f"\n❌ Error generating criminal record: {str(e)}\n")

    finally:
        session.close()  # Ensure session is closed to prevent memory leaks

    input(Fore.YELLOW + "Press Enter to return to the menu...")


if __name__ == "__main__":
    main()
