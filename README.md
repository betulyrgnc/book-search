### **Projenin yerelde çalışır hale getirilmesi ( Linux için )**

* virtualenv -p python3 BookSearch/env
* cd BookSearch
* source env/bin/activate
* git clone https://github.com/BeyzAksy/book-search.git
* cd book-search
* pip install -r requirements.txt
* python manage.py runserver

### **Projenin yerelde çalışır hale getirilmesi ( Windows için )**

* python -m venv BookSearch/env
* cd BookSearch
* env\Scripts\activate
* git clone https://github.com/BeyzAksy/book-search.git
* cd book-search
* pip install -r requirements.txt
* python manage.py runserver

NOT: Windows 10'da , Windows PowerShell tarafından bu senaryoların uygulanması bu sistemde devre dışıdır diyen bir hata alabilirsiniz. Bu durumda, başka bir Windows PowerShell'i, "Yönetici Olarak Çalıştır" seçeneğiyle açın. Bundan sonra sanal ortamınızı başlatmadan önce aşağıdaki komutları yazmayı deneyin:

C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
