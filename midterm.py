def main():
    browser = []
    print("Hello user , choose an option from the following options:")
    while True:
      print("1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
      try:
          user_input = int(input("Please choose an option : "))
      except ValueError:
          print("Invalid input. Please enter a number.")
    
if __name__ == "__main__":
    main()