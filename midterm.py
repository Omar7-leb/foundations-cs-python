#1----------------------------------------------------------------
def open_tab(browser, title, url): #add a new tab to the list of tabs (browser) with title and url
    new_tab = {
        'Title': title,
        'URL': url
    }
    browser.append(new_tab)
    print("Tab with title: " + title + " and url: " + url + " has been opened successfully")
#2----------------------------------------------------------------
def close_tab(browser, index=None):
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
        
#3----------------------------------------------------------------
# ressources : https://pypi.org/project/beautifulsoup4/  , https://youtu.be/bargNl2WeN4?si=89vXLRg0LHvksZgo

from bs4 import BeautifulSoup # library for pulling data out of HTML and XML files
import requests # library for making HTTP requests
def DisplayTabContent(browser, index=None):
    if not browser: #if browser is empty
        print("No tabs to display")
        return

    if index is None:
        index = -1  # Display the last opened tab by default

    if 0 <= index < len(browser):
        tab = browser[index]
        url = tab['URL']
        try:
            response = requests.get(url) #sends an HTTP GET request to the specified URL
            response.raise_for_status()  # Check if the request was successful
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser') #parse the infos in html format
            # You can print or process the HTML content as needed
            print(f"Displaying content of tab at index {index} with title: {tab['Title']}")
            print(soup.prettify())  # Print prettified HTML content
        except requests.RequestException as e: # class requests contain all the request exceptions  ressources : https://requests.readthedocs.io/en/latest/_modules/requests/exceptions/
            print(e)
    else:
        print("Invalid index")
        
#4--------------------------------------------------------
def print_titles(browser):
    if not browser:
        print("No titles to print")
    else:
        for item in browser:
            print(item['Title'])

                
#5--------------------------------------------------------
def Open_nested_tab(browser, parent_index):
    if not browser:
        raise ValueError("browser is empty! You cannot create nested tabs")
    
    if parent_index is not None and 0 <= parent_index < len(browser):
        parent_tab = browser[parent_index]  # parent tab
    else:
        print("Invalid parent index. Creating nested tabs under the last opened tab.") #by default
        parent_tab = browser[-1]

    nested_tabs = []
    num_tabs = int(input("Enter the number of nested tabs you want to create: "))
    
    for i in range(num_tabs):
        title = input(f"Enter the title for nested tab {i + 1}: ")
        url = input(f"Enter the URL for nested tab {i + 1}: ")
        new_tab = {'Title': title, 'URL': url} #the new nested tab
        nested_tabs.append(new_tab)

    if 'NestedTabs' not in parent_tab: # if it is the first nested tab
        parent_tab['NestedTabs'] = []  # Create the 'NestedTabs' key if not present

    parent_tab['NestedTabs'].extend(nested_tabs)  # Extend the list of nested tabs
    
    print(f"{num_tabs} nested tabs created under the parent tab at index {parent_index}")

            
        
def main():
    browser = []
    file = "input.txt"
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
            open_tab(browser, title, url)
        elif user_input == 2:
            try:
                index = int(input("Please enter the index: "))
            except ValueError:
                print("Invalid input for the index. Using the default: closing the last tab.")
                index = None

            close_tab(browser, index)
            
        elif user_input == 3:
             index = int(input("Please enter the index to display content (or press Enter for last tab): "))
             DisplayTabContent(browser, index)
        
        elif user_input == 4:
            print_titles(browser)
            
        elif user_input == 5:
            parent_index = int(input("Please enter the index of the parent tab: "))
            Open_nested_tab(browser, parent_index)
            
            
        elif user_input == 9:
            break
        else:
            print("Invalid input. Please choose an option from 1 to 9.")

if __name__ == "__main__":
    main()
