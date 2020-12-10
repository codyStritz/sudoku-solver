from solver import *
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.app import runTouchApp
from kivy.core.window import Window

Window.keyboard_anim_args = {'d':.2, 't':'in_out_expo'}
Window.softinput_mode = "below_target"

    
class Manager(ScreenManager):
    pass

class Instr(Screen):
    my_text = "[b]About this program:[/b]\n"\
              "This program can give you either a full solution to a sudoku"\
              " puzzle or, if you just need a hint, you can choose for it to reveal the answers to specific squares."\
              "\n\n[b]Instructions:[/b]\n\n"\
              "[b]Full Solution:[/b]"\
              "\nClick on the squares and enter the original numbers provided by your sudoku puzzle. Once you"\
              " have entered all of the provided numbers and the grid matches the grid of your puzzle (only "\
              "the numbers originally given at the start of the puzzle), just press the [b]Solve[/b] button."\
              "\n\n[b]Get Hints:[/b]\n"\
              "Start by entering the original numbers provided by your sudoku puzzle into the corresponding squares on the grid."\
              " Next, place any LETTER (a,b,c..etc.) into any square(s) for which you would like the answer to be revealed."\
              " Lastly, just press the [b]Hints[/b] button.\n\n"\
              "[b]Start Over:[/b]\n"\
              "Press the [b]Clear[/b] button at anytime to clear the grid and start over!"\
              "\n\n[b]Notes:[/b]\nAll numbers entered must be between 1 and 9. Any numbers larger than 9 or less than 1 will be "\
              "seen as a blank square.\n\n"
              
    
class Solver(Screen):
    
    # Row 0
    box_00 = ObjectProperty(None)
    box_01 = ObjectProperty(None)
    box_02 = ObjectProperty(None)
    box_03 = ObjectProperty(None)
    box_04 = ObjectProperty(None)
    box_05 = ObjectProperty(None)
    box_06 = ObjectProperty(None)
    box_07 = ObjectProperty(None)
    box_08 = ObjectProperty(None)
    # Row 1
    box_10 = ObjectProperty(None)
    box_11 = ObjectProperty(None)
    box_12 = ObjectProperty(None)
    box_13 = ObjectProperty(None)
    box_14 = ObjectProperty(None)
    box_15 = ObjectProperty(None)
    box_16 = ObjectProperty(None)
    box_17 = ObjectProperty(None)
    box_18 = ObjectProperty(None)
    # Row 2
    box_20 = ObjectProperty(None)
    box_21 = ObjectProperty(None)
    box_22 = ObjectProperty(None)
    box_23 = ObjectProperty(None)
    box_24 = ObjectProperty(None)
    box_25 = ObjectProperty(None)
    box_26 = ObjectProperty(None)
    box_27 = ObjectProperty(None)
    box_28 = ObjectProperty(None)
    # Row 3
    box_30 = ObjectProperty(None)
    box_31 = ObjectProperty(None)
    box_32 = ObjectProperty(None)
    box_33 = ObjectProperty(None)
    box_34 = ObjectProperty(None)
    box_35 = ObjectProperty(None)
    box_36 = ObjectProperty(None)
    box_37 = ObjectProperty(None)
    box_38 = ObjectProperty(None)
    # Row 4
    box_40 = ObjectProperty(None)
    box_41 = ObjectProperty(None)
    box_42 = ObjectProperty(None)
    box_43 = ObjectProperty(None)
    box_44 = ObjectProperty(None)
    box_45 = ObjectProperty(None)
    box_46 = ObjectProperty(None)
    box_47 = ObjectProperty(None)
    box_48 = ObjectProperty(None)
    # Row 5
    box_50 = ObjectProperty(None)
    box_51 = ObjectProperty(None)
    box_52 = ObjectProperty(None)
    box_53 = ObjectProperty(None)
    box_54 = ObjectProperty(None)
    box_55 = ObjectProperty(None)
    box_56 = ObjectProperty(None)
    box_57 = ObjectProperty(None)
    box_58 = ObjectProperty(None)
    # Row 6
    box_60 = ObjectProperty(None)
    box_61 = ObjectProperty(None)
    box_62 = ObjectProperty(None)
    box_63 = ObjectProperty(None)
    box_64 = ObjectProperty(None)
    box_65 = ObjectProperty(None)
    box_66 = ObjectProperty(None)
    box_67 = ObjectProperty(None)
    box_68 = ObjectProperty(None)
    # Row 7
    box_70 = ObjectProperty(None)
    box_71 = ObjectProperty(None)
    box_72 = ObjectProperty(None)
    box_73 = ObjectProperty(None)
    box_74 = ObjectProperty(None)
    box_75 = ObjectProperty(None)
    box_76 = ObjectProperty(None)
    box_77 = ObjectProperty(None)
    box_78 = ObjectProperty(None)
    # Row 8
    box_80 = ObjectProperty(None)
    box_81 = ObjectProperty(None)
    box_82 = ObjectProperty(None)
    box_83 = ObjectProperty(None)
    box_84 = ObjectProperty(None)
    box_85 = ObjectProperty(None)
    box_86 = ObjectProperty(None)
    box_87 = ObjectProperty(None)
    box_88 = ObjectProperty(None)

    

    def solveButton(self):

        boxes = [self.box_00, self.box_01, self.box_02, self.box_03, self.box_04, self.box_05, self.box_06, self.box_07, self.box_08,
             self.box_10, self.box_11, self.box_12, self.box_13, self.box_14, self.box_15, self.box_16, self.box_17, self.box_18,
             self.box_20, self.box_21, self.box_22, self.box_23, self.box_24, self.box_25, self.box_26, self.box_27, self.box_28,
             self.box_30, self.box_31, self.box_32, self.box_33, self.box_34, self.box_35, self.box_36, self.box_37, self.box_38,
             self.box_40, self.box_41, self.box_42, self.box_43, self.box_44, self.box_45, self.box_46, self.box_47, self.box_48,
             self.box_50, self.box_51, self.box_52, self.box_53, self.box_54, self.box_55, self.box_56, self.box_57, self.box_58,
             self.box_60, self.box_61, self.box_62, self.box_63, self.box_64, self.box_65, self.box_66, self.box_67, self.box_68,
             self.box_70, self.box_71, self.box_72, self.box_73, self.box_74, self.box_75, self.box_76, self.box_77, self.box_78,
             self.box_80, self.box_81, self.box_82, self.box_83, self.box_84, self.box_85, self.box_86, self.box_87, self.box_88]


        for box in boxes:
            board[boxes.index(box)//9][boxes.index(box)%9] = box.text
            if box.foreground_color[0] == .8:       # If currently red, turn black
                box.foreground_color = [0,0,0,1]
        
        
        #Check for non-numeric characters or numbers where n<1 or n>9 and then convert board to int
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not (board[i][j]).isdigit() or not int(board[i][j]) <= 9 or not int(board[i][j]) >= 1:
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])

        
        # Board Arrays
        # Board Rows: board is already 2d array of rows

        # Board Columns
        board_cols = [[row[0]for row in board], [row[1]for row in board], [row[2] for row in board],
                        [row[3] for row in board], [row[4] for row in board], [row[5] for row in board],
                        [row[6] for row in board], [row[7] for row in board], [row[8] for row in board]]

        # Board Sectors
        board_sec1 = [board[0][0], board[0][1], board[0][2], 
                board[1][0], board[1][1], board[1][2], 
                board[2][0], board[2][1], board[2][2]]
        board_sec2 = [board[0][3], board[0][4], board[0][5], 
                board[1][3], board[1][4], board[1][5], 
                board[2][3], board[2][4], board[2][5]]
        board_sec3 = [board[0][6], board[0][7], board[0][8], 
                board[1][6], board[1][7], board[1][8], 
                board[2][6], board[2][7], board[2][8]]
        board_sec4 = [board[3][0], board[3][1], board[3][2], 
                board[4][0], board[4][1], board[4][2], 
                board[5][0], board[5][1], board[5][2]]
        board_sec5 = [board[3][3], board[3][4], board[3][5], 
                board[4][3], board[4][4], board[4][5], 
                board[5][3], board[5][4], board[5][5]]
        board_sec6 = [board[3][6], board[3][7], board[3][8], 
                board[4][6], board[4][7], board[4][8], 
                board[5][6], board[5][7], board[5][8]]
        board_sec7 = [board[6][0], board[6][1], board[6][2], 
                board[7][0], board[7][1], board[7][2], 
                board[8][0], board[8][1], board[8][2]]
        board_sec8 = [board[6][3], board[6][4], board[6][5], 
                board[7][3], board[7][4], board[7][5], 
                board[8][3], board[8][4], board[8][5]]
        board_sec9 = [board[6][6], board[6][7], board[6][8], 
                board[7][6], board[7][7], board[7][8], 
                board[8][6], board[8][7], board[8][8]]
        board_sectors = [board_sec1, board_sec2, board_sec3, board_sec4, board_sec5, board_sec6, board_sec7, 
                    board_sec8, board_sec9]


        # Input Box Arrays
        # Input box rows
        box_rows = [[self.box_00, self.box_01, self.box_02, self.box_03, self.box_04, self.box_05, self.box_06, self.box_07, self.box_08],
             [self.box_10, self.box_11, self.box_12, self.box_13, self.box_14, self.box_15, self.box_16, self.box_17, self.box_18],
             [self.box_20, self.box_21, self.box_22, self.box_23, self.box_24, self.box_25, self.box_26, self.box_27, self.box_28],
             [self.box_30, self.box_31, self.box_32, self.box_33, self.box_34, self.box_35, self.box_36, self.box_37, self.box_38],
             [self.box_40, self.box_41, self.box_42, self.box_43, self.box_44, self.box_45, self.box_46, self.box_47, self.box_48],
             [self.box_50, self.box_51, self.box_52, self.box_53, self.box_54, self.box_55, self.box_56, self.box_57, self.box_58],
             [self.box_60, self.box_61, self.box_62, self.box_63, self.box_64, self.box_65, self.box_66, self.box_67, self.box_68],
             [self.box_70, self.box_71, self.box_72, self.box_73, self.box_74, self.box_75, self.box_76, self.box_77, self.box_78],
             [self.box_80, self.box_81, self.box_82, self.box_83, self.box_84, self.box_85, self.box_86, self.box_87, self.box_88]]

        # Input box columns
        box_cols = [[self.box_00, self.box_10, self.box_20, self.box_30, self.box_40, self.box_50, self.box_60, self.box_70, self.box_80],
                [self.box_01, self.box_11, self.box_21, self.box_31, self.box_41, self.box_51, self.box_61, self.box_71, self.box_81],
                [self.box_02, self.box_12, self.box_22, self.box_32, self.box_42, self.box_52, self.box_62, self.box_72, self.box_82],
                [self.box_03, self.box_13, self.box_23, self.box_33, self.box_43, self.box_53, self.box_63, self.box_73, self.box_83],
                [self.box_04, self.box_14, self.box_24, self.box_34, self.box_44, self.box_54, self.box_64, self.box_74, self.box_84],
                [self.box_05, self.box_15, self.box_25, self.box_35, self.box_45, self.box_55, self.box_65, self.box_75, self.box_85],
                [self.box_06, self.box_16, self.box_26, self.box_36, self.box_46, self.box_56, self.box_66, self.box_76, self.box_86],
                [self.box_07, self.box_17, self.box_27, self.box_37, self.box_47, self.box_57, self.box_67, self.box_77, self.box_87],
                [self.box_08, self.box_18, self.box_28, self.box_38, self.box_48, self.box_58, self.box_68, self.box_78, self.box_88]]

        # Input box sectors
        box_sectors = [[self.box_00, self.box_01, self.box_02, self.box_10, self.box_11, self.box_12, self.box_20, self.box_21, self.box_22],
                [self.box_03, self.box_04, self.box_05, self.box_13, self.box_14, self.box_15, self.box_23, self.box_24, self.box_25],
                [self.box_06, self.box_07, self.box_08, self.box_16, self.box_17, self.box_18, self.box_26, self.box_27, self.box_28],
                [self.box_30, self.box_31, self.box_32, self.box_40, self.box_41, self.box_42, self.box_50, self.box_51, self.box_52],
                [self.box_33, self.box_34, self.box_35, self.box_43, self.box_44, self.box_45, self.box_53, self.box_54, self.box_55],
                [self.box_36, self.box_37, self.box_38, self.box_46, self.box_47, self.box_48, self.box_56, self.box_57, self.box_58],
                [self.box_60, self.box_61, self.box_62, self.box_70, self.box_71, self.box_72, self.box_80, self.box_81, self.box_82],
                [self.box_63, self.box_64, self.box_65, self.box_73, self.box_74, self.box_75, self.box_83, self.box_84, self.box_85],
                [self.box_66, self.box_67, self.box_68, self.box_76, self.box_77, self.box_78, self.box_86, self.box_87, self.box_88]]


        # Checking for multiples of any number in rows, columns, or sectors
        mult = False    # Whether there are multiples in a row, column, sectors
        # Check Rows for Multiples
        for i in range(1,10):
            for j in range(9):
                # Check multiples in rows
                mult_count = 0
                for square in board[j]:
                    if square == i:
                        mult_count += 1
                if mult_count >= 2:
                    for box in box_rows[j]:
                        if box.text == str(i):
                            box.foreground_color = [.8,0,0,1] # red
                    mult = True
                # Check multiples in columns
                mult_count = 0
                for square in board_cols[j]:
                    if square == i:
                        mult_count += 1
                if mult_count >= 2:
                    for box in box_cols[j]:
                        if box.text == str(i):
                            box.foreground_color = [.8,0,0,1] # red
                    mult = True
                # Check multiples in sectors
                mult_count = 0
                for square in board_sectors[j]:
                    if square == i:
                        mult_count += 1
                if mult_count >= 2:
                    for box in box_sectors[j]:
                        if box.text == str(i):
                            box.foreground_color = [.8,0,0,1] # red
                    mult = True
       
        # If no multiples, solve the board
        if mult == False:
            solve(board)
            for box in boxes:
                box.text = str(board[boxes.index(box)//9][boxes.index(box)%9])
       
    

    def clearButton(self):

        boxes = [self.box_00, self.box_01, self.box_02, self.box_03, self.box_04, self.box_05, self.box_06, self.box_07, self.box_08,
             self.box_10, self.box_11, self.box_12, self.box_13, self.box_14, self.box_15, self.box_16, self.box_17, self.box_18,
             self.box_20, self.box_21, self.box_22, self.box_23, self.box_24, self.box_25, self.box_26, self.box_27, self.box_28,
             self.box_30, self.box_31, self.box_32, self.box_33, self.box_34, self.box_35, self.box_36, self.box_37, self.box_38,
             self.box_40, self.box_41, self.box_42, self.box_43, self.box_44, self.box_45, self.box_46, self.box_47, self.box_48,
             self.box_50, self.box_51, self.box_52, self.box_53, self.box_54, self.box_55, self.box_56, self.box_57, self.box_58,
             self.box_60, self.box_61, self.box_62, self.box_63, self.box_64, self.box_65, self.box_66, self.box_67, self.box_68,
             self.box_70, self.box_71, self.box_72, self.box_73, self.box_74, self.box_75, self.box_76, self.box_77, self.box_78,
             self.box_80, self.box_81, self.box_82, self.box_83, self.box_84, self.box_85, self.box_86, self.box_87, self.box_88]

        for box in boxes:
            box.text = ""
            box.foreground_color = [0,0,0,1] #black

        


    def hintsButton(self):

        boxes = [self.box_00, self.box_01, self.box_02, self.box_03, self.box_04, self.box_05, self.box_06, self.box_07, self.box_08,
             self.box_10, self.box_11, self.box_12, self.box_13, self.box_14, self.box_15, self.box_16, self.box_17, self.box_18,
             self.box_20, self.box_21, self.box_22, self.box_23, self.box_24, self.box_25, self.box_26, self.box_27, self.box_28,
             self.box_30, self.box_31, self.box_32, self.box_33, self.box_34, self.box_35, self.box_36, self.box_37, self.box_38,
             self.box_40, self.box_41, self.box_42, self.box_43, self.box_44, self.box_45, self.box_46, self.box_47, self.box_48,
             self.box_50, self.box_51, self.box_52, self.box_53, self.box_54, self.box_55, self.box_56, self.box_57, self.box_58,
             self.box_60, self.box_61, self.box_62, self.box_63, self.box_64, self.box_65, self.box_66, self.box_67, self.box_68,
             self.box_70, self.box_71, self.box_72, self.box_73, self.box_74, self.box_75, self.box_76, self.box_77, self.box_78,
             self.box_80, self.box_81, self.box_82, self.box_83, self.box_84, self.box_85, self.box_86, self.box_87, self.box_88]


        for box in boxes:
            board[boxes.index(box)//9][boxes.index(box)%9] = box.text
            if box.foreground_color[0] == .8:       # If currently red, turn black
                box.foreground_color = [0,0,0,1]
        

    
        # Check for non-numeric characters or integers where n<1 or n>9 and then convert board to int
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not (board[i][j]).isdigit() or not int(board[i][j]) <= 9 or not int(board[i][j]) >= 1:
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])
        
        
        # Board Arrays
        # Board Rows: board is already 2d array of rows

        # Board Columns
        board_cols = [[row[0]for row in board], [row[1]for row in board], [row[2] for row in board],
                        [row[3] for row in board], [row[4] for row in board], [row[5] for row in board],
                        [row[6] for row in board], [row[7] for row in board], [row[8] for row in board]]

        # Board Sectors
        board_sec1 = [board[0][0], board[0][1], board[0][2], 
                board[1][0], board[1][1], board[1][2], 
                board[2][0], board[2][1], board[2][2]]
        board_sec2 = [board[0][3], board[0][4], board[0][5], 
                board[1][3], board[1][4], board[1][5], 
                board[2][3], board[2][4], board[2][5]]
        board_sec3 = [board[0][6], board[0][7], board[0][8], 
                board[1][6], board[1][7], board[1][8], 
                board[2][6], board[2][7], board[2][8]]
        board_sec4 = [board[3][0], board[3][1], board[3][2], 
                board[4][0], board[4][1], board[4][2], 
                board[5][0], board[5][1], board[5][2]]
        board_sec5 = [board[3][3], board[3][4], board[3][5], 
                board[4][3], board[4][4], board[4][5], 
                board[5][3], board[5][4], board[5][5]]
        board_sec6 = [board[3][6], board[3][7], board[3][8], 
                board[4][6], board[4][7], board[4][8], 
                board[5][6], board[5][7], board[5][8]]
        board_sec7 = [board[6][0], board[6][1], board[6][2], 
                board[7][0], board[7][1], board[7][2], 
                board[8][0], board[8][1], board[8][2]]
        board_sec8 = [board[6][3], board[6][4], board[6][5], 
                board[7][3], board[7][4], board[7][5], 
                board[8][3], board[8][4], board[8][5]]
        board_sec9 = [board[6][6], board[6][7], board[6][8], 
                board[7][6], board[7][7], board[7][8], 
                board[8][6], board[8][7], board[8][8]]
        board_sectors = [board_sec1, board_sec2, board_sec3, board_sec4, board_sec5, board_sec6, board_sec7, 
                    board_sec8, board_sec9]


        # Input Box Arrays
        # Input box rows
        box_rows = [[self.box_00, self.box_01, self.box_02, self.box_03, self.box_04, self.box_05, self.box_06, self.box_07, self.box_08],
             [self.box_10, self.box_11, self.box_12, self.box_13, self.box_14, self.box_15, self.box_16, self.box_17, self.box_18],
             [self.box_20, self.box_21, self.box_22, self.box_23, self.box_24, self.box_25, self.box_26, self.box_27, self.box_28],
             [self.box_30, self.box_31, self.box_32, self.box_33, self.box_34, self.box_35, self.box_36, self.box_37, self.box_38],
             [self.box_40, self.box_41, self.box_42, self.box_43, self.box_44, self.box_45, self.box_46, self.box_47, self.box_48],
             [self.box_50, self.box_51, self.box_52, self.box_53, self.box_54, self.box_55, self.box_56, self.box_57, self.box_58],
             [self.box_60, self.box_61, self.box_62, self.box_63, self.box_64, self.box_65, self.box_66, self.box_67, self.box_68],
             [self.box_70, self.box_71, self.box_72, self.box_73, self.box_74, self.box_75, self.box_76, self.box_77, self.box_78],
             [self.box_80, self.box_81, self.box_82, self.box_83, self.box_84, self.box_85, self.box_86, self.box_87, self.box_88]]

        # Input box columns
        box_cols = [[self.box_00, self.box_10, self.box_20, self.box_30, self.box_40, self.box_50, self.box_60, self.box_70, self.box_80],
                [self.box_01, self.box_11, self.box_21, self.box_31, self.box_41, self.box_51, self.box_61, self.box_71, self.box_81],
                [self.box_02, self.box_12, self.box_22, self.box_32, self.box_42, self.box_52, self.box_62, self.box_72, self.box_82],
                [self.box_03, self.box_13, self.box_23, self.box_33, self.box_43, self.box_53, self.box_63, self.box_73, self.box_83],
                [self.box_04, self.box_14, self.box_24, self.box_34, self.box_44, self.box_54, self.box_64, self.box_74, self.box_84],
                [self.box_05, self.box_15, self.box_25, self.box_35, self.box_45, self.box_55, self.box_65, self.box_75, self.box_85],
                [self.box_06, self.box_16, self.box_26, self.box_36, self.box_46, self.box_56, self.box_66, self.box_76, self.box_86],
                [self.box_07, self.box_17, self.box_27, self.box_37, self.box_47, self.box_57, self.box_67, self.box_77, self.box_87],
                [self.box_08, self.box_18, self.box_28, self.box_38, self.box_48, self.box_58, self.box_68, self.box_78, self.box_88]]

        # Input box sectors
        box_sectors = [[self.box_00, self.box_01, self.box_02, self.box_10, self.box_11, self.box_12, self.box_20, self.box_21, self.box_22],
                [self.box_03, self.box_04, self.box_05, self.box_13, self.box_14, self.box_15, self.box_23, self.box_24, self.box_25],
                [self.box_06, self.box_07, self.box_08, self.box_16, self.box_17, self.box_18, self.box_26, self.box_27, self.box_28],
                [self.box_30, self.box_31, self.box_32, self.box_40, self.box_41, self.box_42, self.box_50, self.box_51, self.box_52],
                [self.box_33, self.box_34, self.box_35, self.box_43, self.box_44, self.box_45, self.box_53, self.box_54, self.box_55],
                [self.box_36, self.box_37, self.box_38, self.box_46, self.box_47, self.box_48, self.box_56, self.box_57, self.box_58],
                [self.box_60, self.box_61, self.box_62, self.box_70, self.box_71, self.box_72, self.box_80, self.box_81, self.box_82],
                [self.box_63, self.box_64, self.box_65, self.box_73, self.box_74, self.box_75, self.box_83, self.box_84, self.box_85],
                [self.box_66, self.box_67, self.box_68, self.box_76, self.box_77, self.box_78, self.box_86, self.box_87, self.box_88]]
        
        
        
        # Checking for multiples of any number in rows, columns, or sectors
        mult = False    # Whether there are multiples in a row, column, sectors
        # Check Rows for Multiples
        for i in range(1,10):
            for j in range(9):
                # Check multiples in rows
                mult_count = 0
                for square in board[j]:
                    if square == i:
                        mult_count += 1
                if mult_count >= 2:
                    for box in box_rows[j]:
                        if box.text == str(i):
                            box.foreground_color = [.8,0,0,1] # red
                    mult = True
                # Check multiples in columns
                mult_count = 0
                for square in board_cols[j]:
                    if square == i:
                        mult_count += 1
                if mult_count >= 2:
                    for box in box_cols[j]:
                        if box.text == str(i):
                            box.foreground_color = [.8,0,0,1] # red
                    mult = True
                # Check multiples in sectors
                mult_count = 0
                for square in board_sectors[j]:
                    if square == i:
                        mult_count += 1
                if mult_count >= 2:
                    for box in box_sectors[j]:
                        if box.text == str(i):
                            box.foreground_color = [.8,0,0,1] # red
                    mult = True
        
        
        # If no multiples, give hints
        if mult == False:
            solve(board)
            for box in boxes:
                if box.text.isalpha():
                    box.text = str(board[boxes.index(box)//9][boxes.index(box)%9])
                    box.foreground_color = [.2,.4,1,1] # Blue


sm = Builder.load_file('sudo.kv')
class SudoApp(App):
    def build(self):
        return sm

if __name__=='__main__':
    SudoApp().run()
