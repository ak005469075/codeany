## 有CVE-2023-33733的代码记录

尝试的分析就是出现在Reportlab库中的Paragraph.py上吧，具体的也分析不会

```python
# routes.py
from flask import render_template, request, flash, redirect, url_for, send_file, current_app
from flask_login import login_user, login_required, logout_user
from datetime import date
from io import BytesIO
from reportlab.lib.rl_safe_eval import BadCode
import os
from models import User
from utils import (
    add_paragraph,
    get_document_template,
    build_document,
    restart_server,
    validate_input,
    allowed_file,
)

# Routes for login and logout
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            if password == user.password:
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash('User authentication error.', 'danger')
        else:
            flash('User not found.', 'danger')

    return render_template('index.html')

# @app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Protected route (dashboard) requiring authentication

@login_required
def dashboard():
    try:
        return render_template('dashboard.html')
    except BadCode as e:
        restart_server()
        return render_template('dashboard.html')

# @app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except BadCode as e:
        restart_server()
        return render_template('index.html')

@login_required
def leaveRequest():
    stream_file = BytesIO()
    content = []
    user_signature = None
    title_for_pdf = "Leave Request"
    
    if request.method == 'POST':
        time_interval = request.form['time_interval']
        request_made = request.form['leave_request']
        user_input = request.form['user_input']
        user_signature = request.files['signature']
        
        if not request_made:
            flash('Please specify Contact Phone Number.', 'warning')
        elif not validate_input(user_input):
            pass
        elif user_signature and not allowed_file(user_signature.filename):
            flash('The uploaded file must be a valid image file (jpg, jpeg, png).', 'warning')
        elif not user_signature:
            flash("Please sign your report!", "warning")
        elif user_signature and allowed_file(user_signature.filename): 
            add_paragraph(time_interval, request_made, user_input, content, user_signature, title_for_pdf)
            doc = get_document_template(stream_file)
            build_document(doc, content)
            stream_file.seek(0)

            response = send_file(stream_file, as_attachment=False, download_name='output.pdf')

            signature_path = os.path.join(current_app.config['UPLOAD_FOLDER'], user_signature.filename)
            os.remove(signature_path)

            return response
    
    try:
      return render_template('leave.html')
    except BadCode as e:
      restart_server()
      return render_template('leave.html')

@login_required
def trainingRequest():
    stream_file = BytesIO()
    content = []
    user_signature = None
    title_for_pdf = "Training Request"
    
    if request.method == 'POST':
        time_interval = request.form['time_interval']
        request_made = request.form['training_request']
        user_input = request.form['user_input']
        user_signature = request.files['signature']
        
        if not request_made:
            flash('Please specify requested training.', 'warning')
        elif not validate_input(user_input):
            pass
        elif user_signature and not allowed_file(user_signature.filename):
            flash('The uploaded file must be a valid image file (jpg, jpeg, png).', 'warning')
        elif not user_signature:
            flash("Please sign your report!", "warning")
        elif user_signature and allowed_file(user_signature.filename): 
            add_paragraph(time_interval, request_made, user_input, content, user_signature, title_for_pdf)
            doc = get_document_template(stream_file)
            build_document(doc, content)
            stream_file.seek(0)

            response = send_file(stream_file, as_attachment=False, download_name='output.pdf')

            signature_path = os.path.join(current_app.config['UPLOAD_FOLDER'], user_signature.filename)
            os.remove(signature_path)

            return response
    
    try:
      return render_template('training.html')
    except BadCode as e:
      restart_server()
      return render_template('training.html')

@login_required    
def homeOfficeRequest():
    stream_file = BytesIO()
    content = []
    user_signature = None
    title_for_pdf = "Home Office Request"
    
    if request.method == 'POST':
        time_interval = request.form['time_interval']
        request_made = request.form['home_office_request']
        user_input = request.form['user_input']
        user_signature = request.files['signature']
        
        if not request_made:
            flash('Please specify Home Office address.', 'warning')
        elif not validate_input(user_input):
            pass
        elif user_signature and not allowed_file(user_signature.filename):
            flash('The uploaded file must be a valid image file (jpg, jpeg, png).', 'warning')
        elif not user_signature:
            flash("Please sign your report!", "warning")
        elif user_signature and allowed_file(user_signature.filename): 
            add_paragraph(time_interval, request_made, user_input, content, user_signature, title_for_pdf)
            doc = get_document_template(stream_file)
            build_document(doc, content)
            stream_file.seek(0)

            response = send_file(stream_file, as_attachment=False, download_name='output.pdf')

            signature_path = os.path.join(current_app.config['UPLOAD_FOLDER'], user_signature.filename)
            os.remove(signature_path)

            return response
    
    try:
      return render_template('homeoffice.html')
    except BadCode as e:
      restart_server()
      return render_template('homeoffice.html')

@login_required    
def travelApprovalForm():
    stream_file = BytesIO()
    content = []
    user_signature = None
    title_for_pdf = "Travel Approval Form"
    
    if request.method == 'POST':
        time_interval = request.form['time_interval']
        request_made = request.form['travel_request']
        user_input = request.form['user_input']
        user_signature = request.files['signature']
        
        if not request_made:
            flash('Please specify Travel destination.', 'warning')
        elif not validate_input(user_input):
            pass
        elif user_signature and not allowed_file(user_signature.filename):
            flash('The uploaded file must be a valid image file (jpg, jpeg, png).', 'warning')
        elif not user_signature:
            flash("Please sign your report!", "warning")
        elif user_signature and allowed_file(user_signature.filename): 
            add_paragraph(time_interval, request_made, user_input, content, user_signature, title_for_pdf)
            doc = get_document_template(stream_file)
            build_document(doc, content)
            stream_file.seek(0)

            response = send_file(stream_file, as_attachment=False, download_name='output.pdf')

            signature_path = os.path.join(current_app.config['UPLOAD_FOLDER'], user_signature.filename)
            os.remove(signature_path)

            return response
    
    try:
      return render_template('travel.html')
    except BadCode as e:
      restart_server()
      return render_template('travel.html')

```

上面是 request_made 存储恶意语句的内容，主要是为什么上传时将payload放到request_made = request.form['training_request']上时，可以被正确解析，触发漏洞

这里以TrainingRequest为例

```python
add_paragraph(time_interval, request_made, user_input, content, user_signature, title_for_pdf)
doc = get_document_template(stream_file)
build_document(doc, content)
stream_file.seek(0)

response = send_file(stream_file, as_attachment=False, download_name='output.pdf')
```
上面是由表单内容转pdf的主要代码，可以看到有个add_paragraph函数

```python
# utils.py
from flask import flash, current_app
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from io import BytesIO
from datetime import date
import os
from models import db, User

def create_database():
    db.create_all()
    if not User.query.filter_by(username='blakeb').first():
        db.session.add(User(username='blakeb', password='ThisCanB3typedeasily1@'))
    if not User.query.filter_by(username='claudias').first():
        db.session.add(User(username='claudias', password='007poiuytrewq'))
    if not User.query.filter_by(username='alexanderk').first():
        db.session.add(User(username='alexanderk', password='HotP!fireguard'))

    db.session.commit()
#函数在这里
def add_paragraph(time, request, text, content, user_signature, title_for_pdf):
    styles = getSampleStyleSheet()
    story = [Paragraph(title_for_pdf, styles['Title'])]
    
    logo_path = Image('c:\\users\\blake\\documents\\app\\static\\css\\images\\logo.png', width=1.1*inch, height=1*inch)
    logo_path.hAlign= 'RIGHT'
    content.append(logo_path)
    story.append(Paragraph(f"<b>Time Interval:</b> <br/>{time}", styles['BodyText'], encoding='utf-8'))
    story.append(Paragraph(f"<b>Data Field:</b> <br/>{request}", styles['BodyText'], encoding='utf-8'))
    story.append(Paragraph(f"<b>Justification:</b> <br/>{text}", styles['BodyText'], encoding='utf-8'))
    
    story.append(Spacer(1, 0.305*inch))
    story.append(Paragraph("<br/><i>This document attests to the accuracy of the provided information, and by signing, the undersigned acknowledges and assumes responsibility for the veracity of the information herein.</i>",styles['Normal']))
    
    story.append(Spacer(3, 0.8*inch))
    dateTime = Paragraph(f"Date<br/>{date.today()}", styles['Normal'])
    dateTime.hAlign= 'LEFT'
    story.append(dateTime)
 
    sign = Paragraph(f"Signed by management:<br/>", styles['Normal'])
    sign.hAlign= 'RIGHT'
    story.append(sign)
    sign_path = Image('c:\\users\\blake\\documents\\app\\static\\css\\images\\signature.svg.png', width=1*inch, height=1*inch)
    sign_path.hAlign= 'LEFT'
    story.append(sign_path)
    signature_path = os.path.join(current_app.config['UPLOAD_FOLDER'], user_signature.filename)
    user_signature.save(signature_path)
    signature = Image(signature_path, width=1*inch, height=1*inch)
    signature.hAlign= 'RIGHT'
    story.append(signature)
        
    content.extend(story)

def get_document_template(stream_file: BytesIO):
    return SimpleDocTemplate(stream_file)

def build_document(document, content, **props):
    document.build(content, **props)

def restart_server():
#    os.system('''echo | set /p clean="#">> app.py"''')
#    os.system('''powershell -C "(Get-Content app.py -Raw) -replace '^#|#$', ''| Set-Content app.py -NoNewLine"''')
    return

def validate_input(user_input):
    if user_input == '<p><br></p>':
        flash('Please provide a justification for the request','warning')
        return False
    elif len(user_input) >= 301:
        flash('Character limit exceeded. Please provide a concise justification!', 'warning')
        return False
    return True

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

```

```python
story.append(Paragraph(f"<b>Data Field:</b> <br/>{request}", styles['BodyText'], encoding='utf-8'))
```

主要问题还是在reportlab库中的Paragraph.py里
根据https://github.com/c53elyas/CVE-2023-33733提供的自用poc(本python库中如果存在漏洞，就会执行命令)
调试时发现一开始是将构造的语句按\n进行分割了，经过split，还有文章段落拼接处理什么的

算了，分析不明白，哎

CVE-2023-33733 https://github.com/c53elyas/CVE-2023-33733
https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb#port-139
