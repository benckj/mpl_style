# The style of UZH in matplotlib

There are two ways of using it:
1. Online via github - use the following command in your script:
   ```
   import matplotlib.pyplot as plt 
   plt.style.use('https://raw.githubusercontent.com/benckj/mpl_style/main/uzh.mplstyle')
   ```
  
2. Download the repository and install it on your computer by executing the installation.py file:
   
   After the installation you can use the style in the following way:
   ```
   import matplotlib.pyplot as plt 
   plt.style.use('uzh')
   ```

## UZH Colors Dictionary

If you need to use explicitly a color from the [UZH-Farben](https://www.cd.uzh.ch/de/elements.html#UZH-Farben), you may find useful the following dictionary: keys are the official UZH color designations, while the item is the `str` HEX color value.
```
uzh_colors= {
    'UZH Blue': '#0028A5',
    'Blue 1': '#BDC9E8',
    'Blue 2': '#7596FF',
    'Blue 3': '#3062FF',
    'Blue 4': '#001E7C',
    'Blue 5': '#001452',
    'UZH Cyan': '#4AC9E3',
    'Cyan 1': '#DBF4F9',
    'Cyan 2': '#B7E9F4',
    'Cyan 3': '#92DFEE',
    'Cyan 4': '#1EA7C4',
    'Cyan 5': '#147082',
    'UZH Apple': '#A4D233',
    'Apple 1': '#ECF6D6',
    'Apple 2': '#DBEDAD',
    'Apple 3': '#C8E485',
    'Apple 4': '#7CA023',
    'Apple 5': '#536B18',
    'UZH Gold': '#FFC845',
    'Gold 1': '#FFF4DA',
    'Gold 2': '#FFE9B5',
    'Gold 3': '#FFDE8F',
    'Gold 4': '#F3AB00',
    'Gold 5': '#A27200',
    'UZH Orange': '#FC4C02',
    'Orange 1': '#FFDBCC',
    'Orange 2': '#FEB799',
    'Orange 3': '#FE9367',
    'Orange 4': '#BD3902',
    'Orange 5': '#7E2601',
    'UZH Berry': '#BF0D3E',
    'Berry 1': '#FBC6D4',
    'Berry 2': '#F78CAA',
    'Berry 3': '#F3537F',
    'Berry 4': '#08F0A2E',
    'Berry 5': '#60061F',
    'UZH Black': '#000000',
    'Grey 1': '#C2C2C2',
    'Grey 2': '#A3A3A3',
    'Grey 3': '#666666',
    'Grey 4': '#4D4D4D',
    'Grey 5': '#333333',
    'UZH White': '#FFFFFF',
    'Light Grey 1': '#FAFAFA',
    'Light Grey 2': '#EFEFEF',
    'Light Grey 3': '#E7E7E7',
    'Light Grey 4': '#E0E0E0',
    'Light Grey 5': '#D7D7D7'
}
```

-------------------------------------------------------------------------------
# Installing Fonts:
Execute the the font_installation.py (but first you have to put the fonts in the respective forlders).
Answer from: https://stackoverflow.com/questions/40290004/how-can-i-configure-matplotlib-to-be-able-to-read-fonts-from-a-local-path



