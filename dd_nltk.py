import nltk
import os

# تحديد مسار مجلد التنزيل (اختياري)
# إذا لم تحدد مسارًا، سيتم التنزيل إلى المسار الافتراضي لـ NLTK
download_dir = os.path.expanduser("~/.nltk_data") # مثال لمسار في مجلد المستخدم
# أو مسار نسبي داخل مشروعك:
# download_dir = "nltk_data"
os.makedirs(download_dir, exist_ok=True) # إنشاء المجلد إذا لم يكن موجودًا


# تنزيل الموارد المطلوبة (استبدل هذه القائمة باحتياجات تطبيقك)
resources = [
    "punkt",
    "stopwords",
    "wordnet",
    "averaged_perceptron_tagger",
    "vader_lexicon", # مثال لمورد إضافي
    "omw-1.4" # مورد إضافي ضروري ل wordnet في الإصدارات الحديثة
]

for resource in resources:
    try:
        nltk.data.find(f"tokenizers/{resource}")
        print(f"Resource '{resource}' already downloaded.")
    except LookupError:
        print(f"Downloading resource '{resource}'...")
        nltk.download(resource, download_dir=download_dir)
        print(f"Resource '{resource}' downloaded successfully.")

print("Finished downloading NLTK resources.")
