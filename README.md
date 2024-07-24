# **Amazon-Health-AI Setup and Usage Guide**

## **Overview**

The Amazon-Health-AI application is built using Flask, a popular web framework for Python. This application leverages trained machine learning models to make predictions in Ghanaian Cedis. The project directory is structured as follows:

- **Folders:**
  - `static` (for static files like CSS, JavaScript, images)
  - `templates` (for HTML templates using Jinja2)

- **Files:**
  - `requirements.txt` (list of Python libraries needed)
  - `app.py` (the main Flask application code)
  - `Health-AI.ipynb` (Jupyter Notebook used for training models)

### **Project Structure**

1. **Templates Folder:**
   - `index.html`: This is the main template file for the application. It uses Jinja2, a templating engine for Python, to render dynamic content in HTML.

2. **Health-AI.ipynb:**
   - Contains the code for training the machine learning models. The models used include Gradient Boosting Regression and Decision Tree, which are applied to predict outcomes.

3. **app.py:**
   - Contains the core Flask application code. It uses Flask to create web routes and `pickle` to load and utilize the trained models for predictions.

4. **requirements.txt:**
   - Lists all necessary Python libraries and their versions required to run the application. It ensures that all dependencies are installed.

### **Installation and Setup**

1. **Install Python and Pip:**
   - Ensure Python is installed on your system. Pip is a package manager for Python, which you'll need to install the required libraries.

   - **For Windows:** Follow the guide [here](https://www.w3schools.com/python/python_pip.asp).
   - **For Linux (Ubuntu):** Follow the guide [here](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/).
   - **For macOS:** Follow the guide [here](https://phoenixnap.com/kb/install-pip-mac).

2. **Install Required Libraries:**
   - Once Pip is installed, navigate to the project directory in your terminal and install the libraries listed in `requirements.txt` by running:

     ```bash
     pip3 install -r requirements.txt
     ```

3. **Run the Flask Application:**
   - After installing the necessary libraries, you can start the Flask application by navigating to the directory containing `app.py` and running:

     ```bash
     sudo python3 app.py
     ```

   - This command will start the Flask server, which will be accessible via `http://localhost:80` in your web browser.

4. **Handling Port Conflicts:**
   - If you encounter an `OSError: [Errno 98] Address already in use`, it indicates that port 80 is currently in use by another application. You can change the port number in the `app.py` file to a different port (e.g., 5000) by modifying the last line of the code:

     ```python
     app.run(host='0.0.0.0', port=5000)
     ```

### **Production Use**

- For production environments, ensure to bind the Flask application to `0.0.0.0` so it can be accessed from any network interface. Update the last line in `app.py` to:

  ```python
  app.run(host='0.0.0.0')
  ```

### **Testing**

- The application has been tested on Linux Ubuntu and Linux Mint systems. Ensure your setup mirrors these environments for optimal results.



### **Additional Notes**

- Make sure that all dependencies listed in `requirements.txt` are correctly installed to avoid runtime errors.
- Check firewall settings and network configurations if you have trouble accessing the application.

---

