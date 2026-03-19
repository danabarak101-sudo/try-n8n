# 1. שימוש בתמונה רשמית של פייתון 3.11 (גרסת slim לחסכון במקום)
FROM python:3.11-slim

# קביעת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# העתקת קובץ הדרישות (אם קיים) והתקנתו
# במידה ואין לך requirements.txt, נתקין ישירות את pytest
COPY requirements.txt* .
RUN pip install --no-cache-dir pytest && \
    if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# העתקת כל קבצי הפרויקט לתוך הקונטיינר
COPY . .

# הגדרת פקודת ברירת המחדל להרצת הטסטים
CMD ["pytest", "-vs", "test_func.py"]
