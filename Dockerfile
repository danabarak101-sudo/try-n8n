# 1. שימוש בתמונה רשמית של פייתון 3.11 (גרסת slim לחסכון במקום)
FROM python:3.11-slim

# 2. הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# 3. העתקת קובץ הדרישות (requirements) קודם כל
# זה עוזר ל-Docker להשתמש במטמון (Cache) ולא להתקין הכל מחדש בכל שינוי קוד
COPY requirements.txt .

# 4. התקנת הספריות הדרושות (כמו requests)
RUN pip install --no-cache-dir -r requirements.txt

# 5. העתקת שאר קבצי הקוד מהמחשב שלך לתוך הקונטיינר
COPY . .

# 6. הגדרת משתנה סביבה כדי שהפלט של פייתון יודפס מיד לטרמינל (מעולה ל-Logs)
ENV PYTHONUNBUFFERED=1

# 7. הפקודה שתרוץ כשהקונטיינר עולה
CMD ["python", "main.py"]
