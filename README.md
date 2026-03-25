# 📊 AI-model-monitoring-dashboard - Track AI Models Live Easily

[![Download AI-model-monitoring-dashboard](https://img.shields.io/badge/Download-AI--model--monitoring--dashboard-brightgreen)](https://github.com/Issal9405/AI-model-monitoring-dashboard)

---

## 📋 What Is AI-model-monitoring-dashboard?

AI-model-monitoring-dashboard helps you watch your AI model in real-time. It uses FastAPI, Python, and Power BI. The dashboard tracks prediction accuracy, system health, and other important stats. This way, you can see how your AI model performs right now and fix problems fast.

You don't need to know coding. The tool works on Windows computers. You get clear charts and data updates as your AI works.

---

## 💻 System Requirements

- Windows 10 or later  
- At least 4 GB RAM  
- 500 MB free disk space  
- Internet connection for setup and data updates  
- Power BI Desktop installed (free from Microsoft) for visual reports  
- Python 3.8 or later (included in setup if needed)  

If you don't have Power BI, download it here: https://powerbi.microsoft.com/desktop

---

## 🚀 Getting Started: How to Download and Run on Windows

You can get the files you need and start the dashboard in a few easy steps. This guide assumes you have a Windows PC with basic skills like clicking and typing.

### Step 1: Download the Dashboard Files

Click the big green button below to visit the download page on GitHub:

[![Download AI-model-monitoring-dashboard](https://img.shields.io/badge/Download-AI--model--monitoring--dashboard-blue)](https://github.com/Issal9405/AI-model-monitoring-dashboard)

On the GitHub page:

- Look for a **Releases** section or the main code files.
- If you see a button labeled **Code** or **Download ZIP**, click it.
- Choose **Download ZIP** to save all files to your computer.

### Step 2: Extract the Downloaded Files

- Find the ZIP file in your Downloads folder.
- Right-click the ZIP file and pick **Extract All**.
- Choose a folder where you want these files saved.
- Wait for the extraction to finish.

### Step 3: Install Python (If Needed)

- Check if Python is installed:  
  Open the **Start** menu and type `cmd`. Open Command Prompt.  
  Type `python --version` and press Enter.  
  If you see a version number (like Python 3.9), you have Python. Skip this step.  
- If not installed:  
  Go to https://www.python.org/downloads/windows/  
  Download the latest version for Windows (look for Windows installer).  
  Run the installer and make sure to check **Add Python to PATH** during setup.

### Step 4: Install Required Python Packages

- Open Command Prompt again.  
- Type the following command and press Enter:  
  `pip install -r requirements.txt`  
- This installs all software parts the dashboard needs to work.

### Step 5: Start the Dashboard Software

- In Command Prompt, go to where you saved the files. For example:  
  `cd C:\Users\YourName\Downloads\AI-model-monitoring-dashboard`  
- Start the app by typing:  
  `python main.py`  
- The FastAPI server will run on your PC and show a message with a web address like `http://127.0.0.1:8000`.

### Step 6: Open the Dashboard in Your Web Browser

- Open your browser (like Chrome or Edge).  
- Type the address shown in the Command Prompt (example: `http://127.0.0.1:8000`) and press Enter.  
- You should see the AI model monitoring interface with charts and numbers.

---

## 📊 Using the Dashboard

The dashboard shows you:

- Prediction metrics (accuracy, errors, spam detection rates)  
- System performance (CPU, memory use)  
- Real-time updates for fast decisions  

You can refresh the page anytime to get the latest data. The Power BI reports connect automatically if you set them up.

---

## 🔧 Power BI Report Setup (Optional)

Power BI adds advanced graphs and reports to help you understand data deeply.

1. Open Power BI Desktop on your PC.  
2. Click **Get Data** and choose **Web**.  
3. Enter the API address shown when the app runs (e.g., `http://127.0.0.1:8000/api/data`).  
4. Load the data and build reports.  
5. Save the report file if you want to open it later.

---

## ⚙️ Common Troubleshooting Tips

- If the dashboard won’t start, check Python installation and package installs.  
- Close any other software using port 8000 or change the port number in `main.py`.  
- Ensure your firewall allows the app to access the network.  
- For errors about missing files, confirm you extracted the ZIP completely.  
- Restart your PC if the software behaves oddly.

---

## 🛠 Technical Details

- Built with Python and FastAPI for the backend server.  
- Uses Pandas and Joblib for data handling and model storage.  
- SQLite stores model prediction information locally.  
- Power BI connects to the server API to show reports in real-time.  
- Designed for spam detection but can adapt to other models easily.

---

## 📂 File Structure

- `main.py` — Starts the monitoring server  
- `requirements.txt` — Lists the Python packages needed  
- `model.joblib` — Saved AI model data  
- `data/` — Folder for logs or reports  
- `README.md` — This user guide  

---

## 📥 Download Link Again

Visit this page to download everything you need:  

[Download AI-model-monitoring-dashboard](https://github.com/Issal9405/AI-model-monitoring-dashboard)