# ISEP-TMDEI-Thesis_Project

This file includes the user manual and an instruction manual on how to setup and run the software manually, since it is necessary an API key and a specific headset for the software to be fully working with the control of a person's thoughts.


## User manual

For manual movement, and the software follows the gaming standard keys for movement (WASD - respectively Front, Left, Back, Right), having the user the need to **select the "keyboard input" checkbox for it to work**.

To generate movement with thoughts, **selection of the "brainwave input" checkbox is necessary**, and the user will have to see their surroundings and visualize pulling into and pushing away from them to move forwards and backwards, while to move (rotate) left or right the user will have to visualize himself rotating, with the surrounding rotating in the other direction.


## Instruction manual
### Initial setup
As the initial setup you have to make sure you have the latest version of python 3 installed.

Following this, you have to install the necessary modules for the software to run properly with the following command:

```bash
pip install -r requirements.txt
```

After having this necessary modules installed, you should be able to move into the Server directory and try one of the Test files or run the prototype Software:


> For the test files (insert only one of the following lines each time)
> ```bash
> $ python keyboardInput_Test.py
> $ python motor_Test.py
> $ python LiveAdvance.py  # This will not work since no emotiv API key is applied here.
> ```


> For the prototype software (Since no emotiv API key is applied by default, only manual control will be available)
> ```bash
> $ python main.py
> ```

**Note: If an emotiv API key is available, you should create a file (inside the Server Directory) named `cortexClient.txt` and insert the client Id and the client Secret respectively in consecutive seperate lines.**

