def OpenTab(browser, title, url): #add a new tab to the list of tabs (browser) with title and url
    new_tab = {
        'Title': title,
        'URL': url
    }
    browser.append(new_tab)
    print("Tab with title: " + title + " and url: " + url + " has been opened successfully")
    print(browser)

def CloseTab(browser, index=None):
    if not browser: # if the list is empty
        raise ValueError("Browser is empty! You cannot close a tab.")
    
    if index is not None and 0 <= index < len(browser):
        browser.pop(index)
        print(f"Tab with index {index} has been closed successfully")
    elif index is None: #if the index field is empty
        if browser:
            browser.pop()
            print("Last tab has been closed successfully")
        else:
            print("No tabs to close.")
    else: #incorrect input
        print("You should enter a correct index")

def main():
    browser = []
    print("Hello user, choose an option from the following options:")
    while True:
        try:
            user_input = int(input("1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit\nPlease choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Continue to the next iteration of the loop

        if user_input == 1:
            title = input("Please enter the title: ")
            url = input("Please enter the url: ")
            OpenTab(browser, title, url)
        elif user_input == 2:
            try:
                index = int(input("Please enter the index: "))
            except ValueError:
                print("Invalid input for the index. Using the default: closing the last tab.")
                index = None

            CloseTab(browser, index)
            
        elif user_input == 9:
            break
        else:
            print("Invalid input. Please choose an option from 1 to 9.")

if __name__ == "__main__":
    main()
