"""
PythonAnywhere deployment instructions for CareerPath AI Backend

1. Sign up at: https://www.pythonanywhere.com/registration/register/beginner/

2. After login, click "Files" tab

3. Upload these files from your backend folder:
   - main.py
   - requirements.txt
   - models.py (if exists)

4. Click "Consoles" → Start a new Bash console

5. Run these commands:
   pip3 install --user -r requirements.txt

6. Click "Web" tab → "Add a new web app"
   - Choose Manual configuration
   - Python 3.10

7. In the "Code" section:
   - Source code: /home/yourusername/
   - Working directory: /home/yourusername/
   - WSGI configuration file: Click to edit

8. Replace WSGI file content with:
   import sys
   path = '/home/yourusername'
   if path not in sys.path:
       sys.path.append(path)
   
   from main import app as application

9. Click "Reload" button

10. Your backend will be live at: https://yourusername.pythonanywhere.com

11. Copy this URL and send it to me - I'll update your frontend to use it!
"""