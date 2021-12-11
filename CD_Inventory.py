#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# NWoodward, 2021-Dec-10, added code to create CD Inventory using classes
# NWoodward, 2021-Dec-11, changed file title, review error handling, fix delete method
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt' #text storage file
lstOfCDObjects = [] 

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    #--Fields--#
    cd_id = None
    cd_title = ''
    cd_artist = ''
    
    #--Constructor--#
    def __init__(self, cdID: int, title: str, artist: str):
        """Instantiate a new CD with ID, title, and artist values""" 
        #---Attributes---#
        self.__cd_id = int(cdID)
        self.__cd_title = str(title)
        self.__cd_artist = str(artist)
    
    #--Properties--#
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, cdID):
        if str(cdID).isnumeric():
            self.__cd_id = int(cdID)
        else:
            raise Exception('CD ID must be a number.')
    
    # CD Title
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, title):
        if str(title).isnumeric():
            raise Exception('Please enter a string, not a number.')
        else:
            self.__cd_title = str(title)
        
    # CD Artist
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, artist):
        if str(artist).isnumeric():
            raise Exception('Please enter a string, not a number.')
        else:
            self.__cd_artist = str(artist)
    
    #--Methods--#
    def __str__(self):
        """Format CD object data into a readable string output"""
        return '{}, {}, {}\n'.format(self.__cd_id, self.__cd_title, self.__cd_artist)

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from a text file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name, lst_Inventory): -> (a list of CD objects)

    """

    #--Methods--#
    @staticmethod
    def load_inventory(file_name: str, lst_Inventory: list) -> list:
        """Method to process data from a text file to a list of CD objects.
    
        Args:
            file_name (string): name of file used to read data from
            lst_Inventory (list of objects): list that holds CD objects
        
        Returns:
            lst_Inventory (list of objects): list that holds CD objects
        """
        lst_Inventory = [] 
        try:
            with open(file_name, 'r') as objFile:
                for line in objFile:
                    data = line.strip().split(',')
                    cd = CD(data[0],data[1],data[2])
                    lst_Inventory.append(cd)
        except EOFError as e:
            print('File is blank. Please add CD\'s')
            lst_Inventory = []
        finally:
            return lst_Inventory           

    @staticmethod
    def save_inventory(file_name: str, lst_Inventory: list) -> None:
        """Method to write data from a list of objects to a text file.
        
        Writes data from the list identified by lst_Inventory into a text file
        identified by file_name.
        
        Args:
            file_name (string): name of file used to read data from
            lst_Inventory (list of objects): list that holds CD objects
            
        Returns:
            None.
        """
        try:
            with open(file_name, 'w') as objFile:
                for obj in lst_Inventory:
                    cd = obj.__str__()
                    objFile.write(cd)
        except Exception as e:
            print(type(e))

class DataProcessor:
    """Methods for processing data"""
    
    def add_cd(cd, lst_Inventory: list):
        """ Method that allows user to add a CD to the inventory in memory. The CD must be 
            saved, choice 's', in order for the CD to be written to a text file.
        
        Args:
            cd (object): CD object 
            lst_Inventory (list of objects): list that holds CD objects
            
        Returns:
            lst_Inventory (list of objects): list that holds CD objects
        """
        lst_Inventory.append(cd)
        return lst_Inventory
       
    @staticmethod
    def del_cd(lst_Inventory, cdID):
        """Method that allows user to delete a CD from the inventory in memory.
        
        Args:
            lst_Inventory (list of objects): list that holds CD objects
            cdID: ID number of the CD the user would like to delete
        
        Returns:
            message: Message to the user to tell them if their attempt to delete a CD was successful
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lst_Inventory:
            intRowNr += 1
            if row.cd_id == cdID:
                del lst_Inventory[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            message = print('The CD was removed')
        else:
            message = print('Could not find this CD!')
        return message

# -- PRESENTATION (Input/Output) -- #
class IO:
    """ Handling Input/Output"""
    
    #--Methods--#
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user.
        
        Args:
            None
        Returns:
            None.
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(lst_Inventory: list) -> None:
        """Displays current inventory to the screen

        Args:
            lst_Inventory (list of objects): list that holds CD objects

        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            print(row)
        print('======================================')
        
    @staticmethod
    def get_cd():
        """ Method to enable user to add a new CD to in memory to a list of CD objects 
        
        Args:
            None.
        
        Returns:        
            cdID (string): ID number entered by user
            artist (string): Artist name input by user
            title (string): CD title input by user
        
        """
        try:
            cdID = input('Enter ID: ').strip()
            cdID = int(cdID)
            title = input('What is the CD\'s title? ').strip()
            artist = input('What is the Artist\'s name? ').strip()
            return cdID, title, artist
        except ValueError as e:
            print('Please enter a whole number. You entered {}'.format(cdID))
            print(type(e))

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
try:
    lstOfCDObjects = FileIO.load_inventory(strFileName,lstOfCDObjects)
except Exception as e:
    print(type(e))
    

while True:
    # Display menu to user
    IO.print_menu()
    choice = IO.menu_choice()
    
    # let user exit program
    if choice == 'x':
        break
    
    # show user current inventory
    if choice == 'i':
        try:
            IO.show_inventory(lstOfCDObjects)
        except TypeError as e:
            print('The CD Inventory is blank. Please add content.')
            print(type(e))
        finally:
            continue #start loop back at top
            
    # let user add data to the inventory
    elif choice == 'a':
        try:
            cdID, title, artist = IO.get_cd()
            cd = CD(cdID, title, artist)
            lstOfCDObjects = DataProcessor.add_cd(cd,lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        except Exception as e:
            print(type(e))
        finally:
            continue #start loop back at top
        
    # let user save inventory to file
    elif choice == 's':
        try:
            IO.show_inventory(lstOfCDObjects)
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            if strYesNo == 'y':
                FileIO.save_inventory(strFileName, lstOfCDObjects)
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.') 
        except Exception as e:
            print(type(e))
        finally:
            continue  # start loop back at top.
        
    # let user load inventory from file
    elif choice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName,lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # let user delete data from inventory
    elif choice == 'd':
        IO.show_inventory(lstOfCDObjects)
        cdID = int(input('Which Id would you like to delete?').strip())
        DataProcessor.del_cd(lstOfCDObjects, cdID)
        print() ## Add extra space for layout
        IO.show_inventory(lstOfCDObjects)
        continue

    else:
        print('General Error')
