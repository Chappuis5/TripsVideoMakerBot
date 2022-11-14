import os
import toml
import numpy as np

def checkFile(path):
    if os.path.isfile(path):
        return True
    else:
        return False
#def subMaker(bold, italic, font, font_size, pm_transp, out_transp, border_style, margin, length_limit, endpoint_sec):
def checkConfig():
        available_bold = [0,1]
        available_italic = [0,1]
        available_fonts = ['Roboto', 'Futura', 'LEMON MILK', 'Impact']
        available_outline_width = [1, 2, 3]
        available_font_sizes = [5, 10, 15, 20]
        available_pm_transp = ['00', '40', '80']
        available_out_transp = ['00', '40', '80']
        available_border_style = [1, 2, 3]
        available_margin = [50, 145, 165]
        available_length_limit = [1, 4,5,16]
        available_endpoint_sec = [0.25, 0.5, 0.75, 1]
        default_data = {
                        'settings': {
                                'bold': 1,
                                'italic': 0,
                                'outline_width': 2,
                                'font': 'Futura',
                                'font_size': 10,
                                'pm_transp': '80',
                                'out_transp': '80',
                                'border_style': 3,
                                'margin': 145,
                                'length_limit': 4,
                                'endpoint_sec': 0.25
                        }
                }
        if checkFile("./config.toml"):
                data = toml.load("./config.toml")
                boldness  = data['settings']['bold']
                if len(data['settings']) != 11:
                        print("Config file is not complete")
                        print("Writing default config file....")
                        with open("./config.toml", "w") as f:
                                toml.dump(default_data, f)
                else:
                        if boldness in available_bold:
                                print("OK") 
                        else:
                                print("Wrong bold value, check your config.toml")
                                exit()

                        italicness = data['settings']['italic']
                        if italicness in available_italic:
                                print("OK")
                        else:
                                print("Wrong italic value, check your config.toml")
                                exit()
                        outliness = data['settings']['outline_width']
                        if outliness in available_outline_width or (type(outliness) == int and outliness in range(1,5)):
                                print("OK")
                        else:
                                print("Wrong outline_width value, check your config.toml")
                                exit()
                        font = data['settings']['font']
                        if font in available_fonts or type(font) == str:
                                print("OK")
                        else:
                                print("Font is the wrong type")
                                exit()
                        font_size = data['settings']['font_size']
                        if font_size in available_font_sizes or (type(font_size) == int and font_size in range(5,50)):
                                print("OK")
                        else:
                                print("font_size is either not the wrong type or out of range")
                                exit()
                        pm_transp = data['settings']['pm_transp']
                        if pm_transp in available_pm_transp or (type(pm_transp) == str and len(pm_transp) == 2):
                                print("OK")
                        else:
                                print("pm_transp is either not the wrong type or out of range")
                                exit()
                        out_transp = data['settings']['out_transp']
                        if out_transp in available_out_transp or (type(out_transp) == str and len(out_transp) == 2):
                                print("OK")
                        else:
                                print("out_transp is either not the wrong type or out of range")
                                exit()

                        border_style = data['settings']['border_style']
                        if border_style in available_border_style:
                                print("OK")
                        else:
                                print("Wrong border style value, check config.toml")
                                exit()

                        margin = data['settings']['margin']

                        if margin in available_margin or (type(margin) == int and margin in range(0, 300)):
                                print("OK")
                        else:
                                print("margin is either not the wrong type or out of range")
                                exit()
                                
                        length_limit = data['settings']['length_limit']

                        if length_limit in available_length_limit or (type(length_limit) == int and length_limit in range(1,30)):
                                print("OK")
                        else:
                                print("Length limit is either not the wrong type or out of range")
                                exit()

                        endpoint_sec = data['settings']['endpoint_sec']

                        if endpoint_sec in available_endpoint_sec or (type(endpoint_sec) == float and endpoint_sec in np.arange(0, 3, 0.01)):
                                print("OK")
                        else:
                                print("Endpoint value is either not the wrong type or out of range")
                                exit()
        else:
                print("Config file not found")
                print("Creating config file")
                with open("./config.toml", "w") as f:
                        toml.dump(default_data, f)


        





        


