# 🔍 Selenium UI Test with Brave + DuckDuckGo

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-green)](https://www.selenium.dev/)
[![Brave](https://img.shields.io/badge/Brave-Browser-orange)](https://brave.com/)

</div>

---

## 📋 Description

**Selenium UI Search Test** automates a real user search experience on [DuckDuckGo](https://duckduckgo.com) using the **Brave browser** via Selenium WebDriver.

🎯 **Main Objective:**  
Validate the end-to-end behavior of a search operation using modern browser automation tools.

---

## 🛠️ Tech Stack

| Tool                         | Purpose                                     |
| ---------------------------- | ------------------------------------------- |
| 🐍 Python                    | Test automation scripting                   |
| 🧪 Selenium                  | UI automation framework                     |
| 🦁 Brave Browser             | Chromium-based privacy-focused browser      |
| 🧰 GitHub Actions (optional) | CI integration for automated test execution |

---

## 📁 Project Structure

```
selenium_duckduckgo_test/
│
├── test_search.py          # Main Selenium test script (Brave + DuckDuckGo)
├── requirements.txt        # Python dependencies (Selenium)
├── results.txt             # Output file with search result titles
└── README.md               # Project documentation (this file)
```

---

## 🚀 How to Run the Test

### 📦 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 🧪 2. Run the test script

```bash
python test_search.py
```

The script will:

- Open Brave browser
- Navigate to DuckDuckGo
- Perform a search for **"DevOps testing"**
- Extract and display the top results
- Save results to `results.txt`
- Print total duration of the test

---

## 📄 Sample Output

```
🔎 Resultados encontrados: 10
1. What is DevOps? | IBM
2. DevOps testing explained | Atlassian
...
📄 Resultados guardados en 'resultados.txt'
✅ Prueba funcional completada correctamente.
⏱ Tiempo total de ejecución: 4.82 segundos
```

---

## 🔐 Important Notes

- Make sure `chromedriver.exe` is in your system's PATH.
- Brave must be installed at:

```
C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe
```

- You can change the search term directly in `test_search.py`.

---

## ✅ Best Practices Applied

| ✅  | Principle          | Implementation                      |
| --- | ------------------ | ----------------------------------- |
| ✅  | Real browser test  | Brave used with real search site    |
| ✅  | Wait strategies    | Uses explicit waits (WebDriverWait) |
| ✅  | Result persistence | Saves results in `results.txt`      |
| ✅  | Timing included    | Reports total test duration         |

## 🖼️ Screenshots

During the test, the script automatically captures a screenshot of the DuckDuckGo results page after performing the search.

| File Path                 | Purpose                                 |
| ------------------------- | --------------------------------------- |
| `screenshots/results.png` | Visual snapshot of the test result page |

## This screenshot is especially useful when running the test in **CI/CD environments** like GitHub Actions. It allows reviewers to validate the UI and confirm the test behavior visually.

> ✅ The folder is created dynamically by the script if it doesn't exist.

If you're using GitHub Actions, you can upload the screenshot as an artifact using:

```yaml
- name: 📤 Upload screenshot
  uses: actions/upload-artifact@v3
  with:
    name: screenshot
    path: screenshots
```

## 📜 License

```
This project is for educational purposes only.
Part of UI Automation & DevOps Training Module.
```

---

<div align="center">

⚙️ Built to learn real-world UI testing with modern automation tools.

</div>
