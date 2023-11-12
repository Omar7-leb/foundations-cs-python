#1----------------------------------------------------------------
import validators

def is_valid(url): #ressource: https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not
    return validators.url(url)

def open_tab(browser, title, url):
    if not title :
        print("Title is empty. Please provide a valid title")
        return
    
    if not is_valid(url):
        print("Invalid URL. Please enter a valid URL.")
        return

    new_tab = {
        'Title': title,
        'URL': url
    }
    browser.append(new_tab)
    print("Tab with title: " + title + " and url: " + url + " has been opened successfully")
#2----------------------------------------------------------------
def close_tab(browser, index=None):
    if not browser: # if the list is empty
        print("Browser is empty! There are no tabs to close.")
        return
        
    
    if index is not None and 0 <= index < len(browser):
        browser.remove(browser[index])
        print(f"Tab with index {index} has been closed successfully")
        
    elif index is None: #if the index field is empty
        if browser:
            browser.remove(browser[-1]) #remove the last tab in the browser
            print("Last tab has been closed successfully")
            
    else: #incorrect input
        print("You should enter a correct index")
        
#3----------------------------------------------------------------
# ressources : https://pypi.org/project/beautifulsoup4/  , https://youtu.be/bargNl2WeN4?si=89vXLRg0LHvksZgo

from bs4 import BeautifulSoup # library for pulling data out of HTML and XML files
import requests # library for making HTTP requests
def display_tab_content(browser, index=None):
    if not browser: #if browser is empty
        print("No tabs to display")
        return

    if index is None:
        index = -1  # Display the last opened tab by default

    if  -1 <= index < len(browser):
        tab = browser[index]
        url = tab['URL']
        
        try:
            response = requests.get(url) #sends an HTTP GET request to the specified URL
            response.raise_for_status()  # Check if the request was successful
            html_content = response.text
            if html_content:
                soup = BeautifulSoup(html_content, 'html.parser') #parse the infos in html format
                print(f"Displaying content of tab at index {index} with title: {tab['Title']}")
                print(soup.prettify())  # Print prettified HTML content
                
            else:
                print("HTML content is empty")
            
        except requests.RequestException as e: # class requests contain all the request exceptions  ressources : https://requests.readthedocs.io/en/latest/_modules/requests/exceptions/
            print(e)
    else:
        print("Invalid index")
        
#4--------------------------------------------------------
def print_titles(browser):
    if not browser:
        print("No titles to print")
    else:
        for tab in browser:
            print(tab['Title']) #print the title of parent tab
            nested_tabs = tab.get('NestedTabs', []) #retrieve the value associated with the key 'NestedTabs' in the dictionary tab 
            for nested_tab in nested_tabs:
                print(f"  {nested_tab['Title']}") #print the title of nested tabs
           
#5--------------------------------------------------------
def open_nested_tab(browser, parent_index):
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

#6------------------------------------------------
def clear_tabs(browser):
    if not browser: #if there is no browser
        print("There are no tabs to clear")
        return
    
    browser.clear() #clear the tabs
    print("All open tabs have been cleared")
    
#7----------------------------------------------
import json
def save_tabs(browser, file): #ressource: https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
    if not browser:
        print("No tabs to save.")
        return

    with open(file, 'w') as file:
        tabs_data = []
        for tab in browser:
            tab_data = {
                'Title': tab['Title'],
                'URL': tab.get('URL', ''),
                'NestedTabs': tab.get('NestedTabs', [])
            }
            tabs_data.append(tab_data)

        json.dump(tabs_data, file)

    print(f"Tabs saved to {file} successfully.")
    
#8----------------------------------------- 
def import_tabs(file):
        with open(file, 'r') as file:
            tabs_data = json.load(file)
            return tabs_data
               
        
def main():
    browser = []
    file = "file.json"
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
                index = int(input("Please enter the index (or press Enter for the last index): "))
            except ValueError:
                print("closing the last tab.")
                index = None

            close_tab(browser, index)
            
        elif user_input == 3:
            try:
                index = int(input("Please enter the index to display content (or press Enter for last tab): "))
            except ValueError:
                print("displaying the html content of the last tab.")
                index = None
                
            display_tab_content(browser, index)
             
        
        elif user_input == 4:
            print_titles(browser)
            
        elif user_input == 5:
            parent_index = int(input("Please enter the index of the parent tab: "))
            open_nested_tab(browser, parent_index)
        
        elif user_input == 6:
            clear_tabs(browser)
            
        elif user_input == 7:
            save_tabs(browser,file)
            
        elif user_input == 8:
            loaded_tabs = import_tabs(file)
            if loaded_tabs:
                browser.extend(loaded_tabs)
                print("Tabs loaded successfully.")
            
            
        elif user_input == 9:
            break
        else:
            print("Invalid input. Please choose an option from 1 to 9.")

if __name__ == "__main__":
    main()
