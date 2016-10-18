# -*- coding: utf-8 -*-


import logging
import smtplib
import stringutils

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def compose_addr(name, email):
    if name is not None and len(name) > 0:
        return '%s <%s>' % (Header(name, 'utf-8'), email)
    else:
        return stringutils.ensure_ascii(email)


def compose_header(headstr):
    return Header(headstr, 'utf-8')


def compose_email(from_email, from_name, to_email, to_name, subject, body, reply_to=''):
    msg = MIMEMultipart('alternative')
    msg['From'] = compose_addr(from_name, from_email)
    msg['To'] = compose_addr(to_name, to_email)
    if reply_to:
        msg['Reply-to'] = reply_to
    msg['Subject'] = compose_header(subject)
    html = '<html><body>%s</body></html>' % body
    part_text = MIMEText(body, 'plain', 'utf-8')
    part_html = MIMEText(html, 'html', 'utf-8')
    msg.attach(part_text)
    msg.attach(part_html)
    return msg


def send(server, port, ssl, auth_user, auth_pass, sender, from_email, from_name,
        to_email, to_name, subject, body, reply_to=''):
    send_result = {}
    try:
        if ssl:
            if port == 0:
                port = 465
            smtp = smtplib.SMTP_SSL(server, port)
        else:
            if port == 0:
                port = 25
            smtp = smtplib.SMTP(server, port)
        smtp.set_debuglevel(False)
        if auth_user and auth_pass:
            smtp.login(auth_user, auth_pass)
        msg = compose_email(from_email, from_name, to_email, to_name, subject, body, reply_to)
        try:
            send_result = smtp.sendmail(sender, to_email, msg.as_string())
        finally:
            smtp.close()
        if len(send_result) == 0:
            return True
        femails = send_result.keys()
        # only one reciever once
        #assert(len(femails) == 1)
        femail = femails[0]
        einfo = send_result[femail]
        logging.warning('Failed in sending %s to %s[code: %d, info: %s]' % 
                (msg.as_string(), femail, einfo[0], einfo[1]))
    except Exception as e:
        logging.error(e)
    return False


if __name__ == '__main__':
    import datetime
    send('smtp.163.com', 25, False, 'icewaver@163.com', '********',
            'icewaver@163.com', 'icewaver@163.com', 'icewaver',
            '451661587@qq.com', '酸雨', '测试邮件',
            '这时一封测试邮件，你能看见吗？ %s' % (datetime.datetime.now()))
