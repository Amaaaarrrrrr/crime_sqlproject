from models import Case, Suspect, Evidence, Detective, CriminalRecord
from database import Session
from colorama import Fore, Style, init
from tabulate import tabulate
import time

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

        elif choice == "0":
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

### **Suspect Management**
def suspect_menu():
    """Manages suspects in the system."""
    while True:
        print_header("👤 Suspect Management")
        print("1️⃣ Add a Suspect")
        print("2️⃣ View All Suspects")
        print("3️⃣ Find Suspect by ID")
        print("4️⃣ Delete Suspect")
        print("0️⃣ Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter suspect's name: ")
            age = input("Enter suspect's age: ")
            alibi = input("Enter alibi (if any): ")
            case_id = input("Enter associated Case ID: ")
            Suspect.create(name, int(age), alibi, int(case_id))
            print(Fore.GREEN + "✅ Suspect added successfully!")

        elif choice == "2":
            suspects = Suspect.get_all()
            if suspects:
                print(Fore.BLUE + tabulate([[s.id, s.name, s.age, s.alibi, s.case_id] for s in suspects],
                                           headers=["ID", "Name", "Age", "Alibi", "Case ID"],
                                           tablefmt="grid"))
            else:
                print(Fore.RED + "❌ No suspects found.")

        elif choice == "3":
            suspect_id = input("Enter Suspect ID: ")
            suspect = Suspect.find_by_id(int(suspect_id)) if suspect_id.isdigit() else None
            if suspect:
                print(Fore.GREEN + f"✅ Found Suspect: {suspect.name}, Age: {suspect.age}, Alibi: {suspect.alibi}")
            else:
                print(Fore.RED + "❌ Suspect not found.")

        elif choice == "4":
            suspect_id = input("Enter Suspect ID to delete: ")
            if suspect_id.isdigit():
                Suspect.delete(int(suspect_id))
                print(Fore.GREEN + "✅ Suspect deleted successfully!")
            else:
                print(Fore.RED + "❌ Invalid ID.")

        elif choice == "0":
            break
        else:
            print(Fore.RED + "❌ Invalid choice.")

### **Evidence Management**
def evidence_menu():
    """Manages evidence records."""
    while True:
        print_header("🔎 Evidence Management")
        print("1️⃣ Add Evidence")
        print("2️⃣ View All Evidence")
        print("3️⃣ Find Evidence by ID")
        print("4️⃣ Delete Evidence")
        print("0️⃣ Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter evidence description: ")
            found_location = input("Enter location where evidence was found: ")
            case_id = input("Enter associated Case ID: ")
            Evidence.create(description, found_location, int(case_id))
            print(Fore.GREEN + "✅ Evidence added successfully!")

        elif choice == "2":
            evidences = Evidence.get_all()
            if evidences:
                print(Fore.BLUE + tabulate([[e.id, e.description, e.found_location, e.case_id] for e in evidences],
                                           headers=["ID", "Description", "Found Location", "Case ID"],
                                           tablefmt="grid"))
            else:
                print(Fore.RED + "❌ No evidence found.")

        elif choice == "3":
            evidence_id = input("Enter Evidence ID: ")
            evidence = Evidence.find_by_id(int(evidence_id)) if evidence_id.isdigit() else None
            if evidence:
                print(Fore.GREEN + f"✅ Found Evidence: {evidence.description}, Found at: {evidence.found_location}")
            else:
                print(Fore.RED + "❌ Evidence not found.")

        elif choice == "4":
            evidence_id = input("Enter Evidence ID to delete: ")
            if evidence_id.isdigit():
                Evidence.delete(int(evidence_id))
                print(Fore.GREEN + "✅ Evidence deleted successfully!")
            else:
                print(Fore.RED + "❌ Invalid ID.")

        elif choice == "0":
            break
        else:
            print(Fore.RED + "❌ Invalid choice.")



def detective_menu():
    """Manages detectives in the system."""
    while True:
        print_header("🕵️ Detective Management")
        print("1️⃣ Add a Detective")
        print("2️⃣ View All Detectives")
        print("3️⃣ Find Detective by ID")
        print("4️⃣ Delete Detective")
        print("0️⃣ Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter detective's name: ")
            rank = input("Enter detective's rank (default: 'Junior'): ") or "Junior"
            solved_cases = input("Enter solved cases (default: 0): ") or 0
            Detective.create(name, rank, int(solved_cases))
            print(Fore.GREEN + "✅ Detective added successfully!")

        elif choice == "2":
            detectives = Detective.get_all()
            if detectives:
                print(Fore.BLUE + tabulate([[d.id, d.name, d.rank, d.solved_cases] for d in detectives],
                                           headers=["ID", "Name", "Rank", "Solved Cases"],
                                           tablefmt="grid"))
            else:
                print(Fore.RED + "❌ No detectives found.")

        elif choice == "3":
            detective_id = input("Enter Detective ID: ")
            detective = Detective.find_by_id(int(detective_id)) if detective_id.isdigit() else None
            if detective:
                print(Fore.GREEN + f"✅ Found Detective: {detective.name}, Rank: {detective.rank}, Solved Cases: {detective.solved_cases}")
            else:
                print(Fore.RED + "❌ Detective not found.")

        elif choice == "4":
            detective_id = input("Enter Detective ID to delete: ")
            if detective_id.isdigit():
                Detective.delete(int(detective_id))
                print(Fore.GREEN + "✅ Detective deleted successfully!")
            else:
                print(Fore.RED + "❌ Invalid ID.")

        elif choice == "0":
            break
        else:
            print(Fore.RED + "❌ Invalid choice.")

def criminal_record_menu():
    """Manages criminal records in the system."""
    while True:
        print_header("⚖️ Criminal Record Management")
        print("1️⃣ Add a Criminal Record")
        print("2️⃣ View All Criminal Records")
        print("3️⃣ Find Criminal Record by ID")
        print("4️⃣ Delete Criminal Record")
        print("0️⃣ Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            suspect_id = input("Enter Suspect ID: ")
            previous_crimes = input("Enter previous crimes: ")
            sentence = input("Enter sentence: ")
            CriminalRecord.create(int(suspect_id), previous_crimes, sentence)
            print(Fore.GREEN + "✅ Criminal record added successfully!")

        elif choice == "2":
            records = CriminalRecord.get_all()
            if records:
                print(Fore.BLUE + tabulate([[r.id, r.suspect_id, r.previous_crimes, r.sentence] for r in records],
                                           headers=["ID", "Suspect ID", "Previous Crimes", "Sentence"],
                                           tablefmt="grid"))
            else:
                print(Fore.RED + "❌ No criminal records found.")

        elif choice == "3":
            record_id = input("Enter Criminal Record ID: ")
            record = CriminalRecord.find_by_id(int(record_id)) if record_id.isdigit() else None
            if record:
                print(Fore.GREEN + f"✅ Found Record: Suspect ID: {record.suspect_id}, Crimes: {record.previous_crimes}, Sentence: {record.sentence}")
            else:
                print(Fore.RED + "❌ Criminal record not found.")

        elif choice == "4":
            record_id = input("Enter Criminal Record ID to delete: ")
            if record_id.isdigit():
                CriminalRecord.delete(int(record_id))
                print(Fore.GREEN + "✅ Criminal record deleted successfully!")
            else:
                print(Fore.RED + "❌ Invalid ID.")

        elif choice == "0":
            break
        else:
            print(Fore.RED + "❌ Invalid choice.")




if __name__ == "__main__":
    main()
