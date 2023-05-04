#!/bin/bash

# Define function to print menu options
print_menu() {
    echo ""
    echo "==================================="
    echo "         TANK RUNNER BASH          "
    echo "==================================="
    echo "  [0] Exit"
    echo "  [1] Project Introduction"
    echo "  [2] File Integrity Check Helper"
    echo "  [3] Dependency Check Helper"
    echo "  [4] Credits"
    echo "  [5] How to run the game"
    echo "==================================="
    echo ""
}

# Check authentication 
check_authentication () {
    if [ "$1" == "$2" ]; then 
        echo "authenticated"
    else 
        echo "failed authentication"
    fi 
}

# Print introduction info
echo "Welcome to the Project Main Menu."

# Print menu options
print_menu

# Prompt user to enter a menu option
read -p "Enter the number of your selection: " option
echo ""
echo "==================================="

# Loop through menu options until user chooses to exit
while [ $option -ne 0 ]; do
    case $option in
        1)
            echo "Project Introduction:"
            echo ""
            echo "The project at it’s core will be a 2D game that will utilize Python and the PyGame library to create essentially the entire game. Our intended game is meant to mimic those such as the Google dinosaur game, with some mechanics inspired by space invaders. Given our groups experience with PyGame and 2D game development, it is very possible to accomplish our intended game mechanics. On the creative side of development, there are various websites/software available that will make the creation of modes/sound effects/etc. much easier to create and import. A project such as this one heavily relies on proper workflow to ensure productivity and communication throughout our entire team. Below is a rough sketch on how we would like our game to function. The green in the sketch represents the bounds of the game, the red represents obstacles the user encounters, and the blue represents the user-controlled tank and it’s canon shooting. Like any other game’s development process, we are currently in it’s pre-production and features are subject to change as we progress."
            ;;
        2)
            echo "File Integrity Check Helper:"
            echo ""
            check_main=$(sha1sum main.py)
            main_file=$"c7967df59976ac01af179055dd712f0aed85529c  main.py"
            check_requirement=$(sha1sum requirements.txt)
            requirements_file=$"848a4d865d60604b43f6233d583284a5b927c905  requirements.txt"
            check_sound=$(sha1sum assets/audio/esm_8_bit_game_over_1_arcade_80s_simple_alert_notification_game.mp3)
            sound_file=$"c64851cb1cbb07e3c0a88da1e8cc58396e7e36a5  assets/audio/esm_8_bit_game_over_1_arcade_80s_simple_alert_notification_game.mp3"
            check_bear0=$(sha1sum assets/bear/Bear0.png)
            bear0_file=$"2675a19f12f6b647e58f02f74a092e147cfe4218  assets/bear/Bear0.png"
            echo Check main.py ...;
            check_authentication "$check_main" "$main_file";
            echo ;
            echo Check requirements.txt ...; 
            check_authentication "$check_requirement" "$requirements_file"
            echo ;
            echo Check esm_8_bit_game_over_1_arcade_80s_simple_alert_notification_game.mp3 ...; 
            check_authentication "$check_sound" "$sound_file"
            echo ;
            echo check assets ...;
            check_authentication "$check_bear0" "$bear0_file"
            echo ;
            ;;
        3)
            echo "Dependency Check Helper:"
            echo ""
            # Check if Python3 is installed
            if ! command -v python3 &> /dev/null
            then
                echo "Python3 could not be found"
                echo "You can install Python3 with the following command: sudo apt install python3"
                exit 1
            fi
            
            # Check if virtual environment is installed
            if ! command -v python3 -m venv &> /dev/null
            then
                echo "Virtual environment could not be found"
                echo "You can install virtual environment with the following command: sudo apt install python3-venv"
                exit 1
            fi
            
            # Check if PyGame module is installed
            if ! command python3 -m pygame.version &> /dev/null
            then
                echo "PyGame module could not be found"
                echo "You can install PyGame module with the following command: sudo apt-get install python3-pygame"
                exit 1
            fi
            
            # Exit message
            echo "All dependencies are installed"
            ;;
        4)
            echo "Credits:"
            echo ""
            echo "THIS PROJECT WAS CREATED BY:"
            echo "  - Mario Linares and Michael Rojas"
            ;;
        5)
            echo "How to run the game:"
            echo ""
            echo "1. python3 -m venv venv (create virtual environment)"
            echo "2. source venv/bin/activate (activate virtual environment)"
            echo "3. pip install -r requirements.txt (install dependencies)"
            echo "4. python3 main.py (run game)"
            echo "5. deactivate (deactivate virtual environment once done)"
            ;;
        *)
            echo "Invalid option. Please enter a valid option."
            echo ""
            ;;
    esac

    # Print menu options again
    print_menu

    # Prompt user to enter another menu option
    read -p "Enter the number of your selection: " option
    echo ""
    echo "==================================="
done

# Exit message
echo "Exiting Project Main Menu. Goodbye!"
echo ===================================
