# 🎨 Palette Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?logo=python)
![Clipboard](https://img.shields.io/badge/Clipboard-Supported-lightgrey?logo=clipboard)

A lightweight **color palette generator** built with **Python + Tkinter**.  
Easily generate, lock, copy, and navigate between color palettes with a simple GUI.

---

## ✨ Features
- 🎲 **Random Palette Generation** — create new 4-color palettes instantly.
- 🔒 **Lock Individual Colors** — keep certain colors fixed while shuffling the rest.
- 📋 **Copy Hex Codes** — click on any color’s hex label to copy it to your clipboard.
- ⏪ **Previous / Next Navigation** — cycle through your palette history like a browser.
- 🎨 **Live Preview** — see colors update instantly in the Tkinter canvas.

---

## 📷 Preview
![alt text](sample.mov)
---

## 🛠️ Installation

1. Clone this repository (or download the `.py` file):
   ```bash
   git clone https://github.com/yourusername/palette-generator.git
   cd palette-generator
   ```

2. Install dependencies:
   ```bash
   pip install pyperclip
   ```

3. Run the app:
   ```bash
   python palette_generator.py
   ```

---

## 🎮 Usage Guide
- **Change Colors** → generates a new random palette.
- **Click Hex Code** → copies the hex code to your clipboard.
- **🔓 / 🔒 Button** → toggle lock state of each color.
- **Previous / Next** → navigate palette history.
- Locked colors remain the same when generating new palettes.

---

## 📂 Project Structure
```bash
palette-generator/
│── palette_generator.py   # main Python script (Tkinter app)
│── README.md              # documentation
```

---

## 💡 Possible Future Enhancements
- Export palettes as:
  - PNG image (swatches)
  - JSON / text files
- Support custom number of blocks (more than 4 colors).
- Auto-generate complementary / gradient palettes.
- Dark mode theme for the GUI.
- Save favorite palettes to a local database.

---

## 🤝 Contributing
Pull requests and ideas are welcome!  
If you’d like to contribute:
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-new`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to branch (`git push origin feature-new`)
5. Open a Pull Request 🎉

---

## 📜 License
This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute it.

---

## 👤 Author
**Mohamed Boualamallah**  
📧 Email: mohamedboualamallah@icloud.com  
🌐 LinkedIn: https://linkedin.com/in/mohamedboualamallah
