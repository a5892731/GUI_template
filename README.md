# GUI_template
base for tkinter standard GUI, with three state machines for the realization of your program.

![image](https://user-images.githubusercontent.com/71212857/220584675-bd8a1255-9772-497b-90fd-ba4747ad42ea.png)


State machines requirements:
1) Create your states in my_stetes.py file;
2) Create parent bodys for your steres in "stetes" folder dedicated to state machine;
3) in *_machine_loader.py file set "number_of_states" variable according to the number of states in current machine;
4) init all your states in "stetes_data_buffer.py" if you whant to share a data betwen states in program.
---------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/71212857/220585395-0714abd8-84ad-4e1d-9796-0198388f5fe4.png)

GUI:
1) to simplyfy your program use widgets from template files;
2) create new windows inyour program and init them in main.py file;
3) edit your menu in "_left_menu_bar.py" file.
4) init all your gui variables in "_gui_variables.py" file. This variables will be accesable to get/update in your state machine.
---------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/71212857/220587186-d325d287-3949-441b-b3a2-c2f3b92b58ce.png)
