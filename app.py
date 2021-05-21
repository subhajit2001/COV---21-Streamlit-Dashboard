#importing all libraries
import sys
from pages import sidebar
from pages import home
from pages import country
from pages import India
from pages import state
from pages import test

sys.path.insert(0, './pages')

def main():
    
    page_selected = sidebar.sidebar_elements()

    #state names to codes dictionary
    #page 1
    if page_selected == 'Home':
        home.home_elements()
    #page 2
    elif page_selected == 'Country Dashboard':
        country.country_elements()
    #page 3
    elif page_selected == 'India Dashboard':
        India.india_elements()
    #page 4
    elif page_selected == 'State Dashboard':
        state.state_elements()
    #page 5    
    elif page_selected == 'Testing Data Dashboard':
        test.test()
if __name__ == "__main__":
    main()




