def OpenTab(browser,title,url):
    new_tab = {
        'Title': title,
        'URL': url
    }
    browser.append(new_tab)
    print("Tab with title: " + title + " and url: " + url +" has been opened successfully") 

def main():
    browser = []
    print("Hello user , choose an option from the following options:")
    while True:
      print("1. Open Tab\n2. Close Tab\n3. Switch Tab\n4. Display All Tabs\n5. Open Nested Tab\n6. Clear All Tabs\n7. Save Tabs\n8. Import Tabs\n9. Exit")
      try:
          user_input = int(input("Please choose an option : "))
          if user_input == 1:
              title = input("Please enter the title: ")
              url = input("Please enter the url: ")
              OpenTab(browser, title, url)
          else:
              print("Invalid input. Please choose an option from 1 to 9.")
      except ValueError:
          print("Invalid input. Please enter a number.")
    
if __name__ == "__main__":
    main()