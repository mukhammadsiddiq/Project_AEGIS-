import network_security
import data_encryption
import vulnerability_scanning
import intrusion_detection
import logging_reporting


def main():
    while True:
        print("Welcome to Project AEGIS")
        print("1. Network Security")
        print("2. Data Encryption")
        print("3. Vulnerability Scanning")
        print("4. Intrusion Detection")
        print("5. Logging and Reporting")
        choice = input("Select an option: ")
        if choice == '1':
            network_security.monitor_network()
            continue
        elif choice == '2':
            data_encryption.menu()
            continue
        elif choice == '3':
            vulnerability_scanning.scan_network()
            continue
        elif choice == '4':
            intrusion_detection.detect_intrusion()
            continue
        elif choice == '5':
            logging_reporting.generate_report()
            continue
        else:
            print("Invalid option")
            break


if __name__ == "__main__":
    main()
