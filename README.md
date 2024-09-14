### Usage

To get 3 images of cheese,

```bash
python3 script/get_images_from_wikimedia.py cheese -take 3
```
will create a directory ```images/cheese``` with the image files below

| 1.jpg | 2.jpg    | 3.jpg    |
| :---:   | :---: | :---: |
| ![1](https://github.com/user-attachments/assets/0db16e0c-f405-4d57-8a31-72be307089f1) | ![2](https://github.com/user-attachments/assets/f7314cf9-ddbd-4096-8456-25860b6130ac)|![3](https://github.com/user-attachments/assets/3e625112-18d0-43e4-bde6-1d2bec2b3b25)|

and the ```attributions.json```,

```json
{
    "1": {
        "Attribution": "",
        "LicenseShortName": "Public domain",
        "LicenseUrl": "",
        "Artist": "<bdi><a href=\"https://en.wikipedia.org/wiki/en:Clara_Peeters\" class=\"extiw\" title=\"w:en:Clara Peeters\"><span title=\"Flemish painter (1594-1657)\">Clara Peeters</span></a>\n</bdi>"
    },
    "2": {
        "Attribution": "",
        "LicenseShortName": "Public domain",
        "LicenseUrl": "",
        "Artist": "Original photo by <a rel=\"nofollow\" class=\"external text\" href=\"http://pdphoto.org/\">John Sullivan</a>. Edit own work."
    },
    "3": {
        "Attribution": "This file is not in the public domain. Therefore you are requested to use the following next to the image if you reuse this file: \u00a9 <a href=\"//commons.wikimedia.org/wiki/User:Yann\" title=\"User:Yann\">Yann Forget</a>\u00a0/\u00a0<a class=\"external text\" href=\"https://commons.wikimedia.org\">Wikimedia Commons</a>",
        "LicenseShortName": "CC BY-SA 4.0",
        "LicenseUrl": "https://creativecommons.org/licenses/by-sa/4.0",
        "Artist": "<a href=\"//commons.wikimedia.org/wiki/User:Yann\" title=\"User:Yann\">Yann Forget</a>"
    }
}
```
### Rights

- (Output) Files downloaded are subject to any license listed in the ```{path}/{query}/attributions.json``` file.
- The source code is GPLv3
